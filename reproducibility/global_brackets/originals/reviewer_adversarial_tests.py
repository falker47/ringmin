#!/usr/bin/env python3
"""Adversarial tests. Mutates ONLY new scratch copies; never original evidence.

Loads packet modules for fixture construction and targeted regression tests.
The independent reviewer verifier is loaded separately for the test oracle.
Deliberately invalid reports produced by this script are NOT certificates.
"""
from __future__ import annotations
import argparse,copy,contextlib,hashlib,importlib.util,io,itertools,json,math,random,subprocess,sys,time,types
from fractions import Fraction as F
from pathlib import Path
sys.dont_write_bytecode=True

def need(x,msg):
    if not x:raise AssertionError(msg)
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
def memory_module(name,path,changes):
    source=path.read_text()
    for old,new in changes:
        need(old in source,'missing mutation target '+old);source=source.replace(old,new)
    mod=types.ModuleType(name);mod.__file__=str(path);exec(compile(source,str(path)+' [test-only memory copy]','exec'),mod.__dict__);return mod

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args();src=args.source;out=args.output_dir;out.mkdir(parents=True,exist_ok=False);start=time.perf_counter()
    review=load('reviewer_oracle',Path(__file__).with_name('reviewer_verify.py'))
    gen=load('packet_generator_for_test_fixtures',src/'ringmin_global_interval_replay.py')
    receipt=load('packet_arithmetic_for_tests',src/'windows_receipt_check.py')
    before={p.name:review.sha(p.read_bytes()) for p in src.iterdir() if p.is_file()}
    basew=review.read(src/'global_interval_replay_20260917T101809Z_3399172f.json')
    basel=review.read(src/'ringmin_global_interval_candidate.json')
    T=int(basew['certificate']['tau_upper_scaled'])
    def write_reports(name,mutate):
        folder=out/name;folder.mkdir()
        w,l=copy.deepcopy(basew),copy.deepcopy(basel)
        for r in (w,l):
            mutate(r['certificate']);r['certificate_sha256']=review.sha(review.canonical(r['certificate']))
        paths=[]
        for label,r in [('windows',w),('linux',l)]:
            p=folder/('DELIBERATELY_INVALID_'+label+'.json');p.write_text(json.dumps(r,indent=2)+'\n');paths.append(p)
        return folder,paths,w
    def check_mutant(name,mutate,expect_cross,expect_receipt):
        folder,paths,w=write_reports(name,mutate)
        commands={
          'crosschecker':[sys.executable,'-I','-S',str(src/'ringmin_global_interval_crosscheck.py'),'--certificate',str(paths[0])],
          'receipt':[sys.executable,'-I','-S',str(src/'windows_receipt_check.py'),'--windows',str(paths[0]),'--linux',str(paths[1]),'--script',str(src/'ringmin_global_interval_replay.py'),'--output',str(folder/'mutant_receipt_result.json')]}
        result={'name':name,'certificate_sha256':w['certificate_sha256'],'files_sha256':{p.name:review.sha(p.read_bytes()) for p in paths}}
        for label,cmd in commands.items():
            run=subprocess.run(cmd,text=True,capture_output=True,timeout=35)
            (folder/(label+'.stdout.txt')).write_text(run.stdout);(folder/(label+'.stderr.txt')).write_text(run.stderr)
            result[label]={'exit_code':run.returncode,'accepted':run.returncode==0,'last_error':run.stderr.splitlines()[-1] if run.stderr else None}
        need(result['crosschecker']['accepted']==expect_cross,'unexpected crosschecker outcome '+name)
        need(result['receipt']['accepted']==expect_receipt,'unexpected receipt outcome '+name)
        try:
            review.verify(w,pinned=False)
        except ValueError as e:
            result['reviewer_oracle']={'rejected':True,'reason':str(e)}
        else:result['reviewer_oracle']={'rejected':False}
        print(json.dumps({'test':name,'crosschecker_accepts':expect_cross,'receipt_accepts':expect_receipt,'reviewer':result['reviewer_oracle']},separators=(',',':')),flush=True)
        return result
    tests=[]
    tests.append(check_mutant('missing_n4_upper_witness',lambda c:c['cases'][1].update(upper_witnesses=[]),True,True))
    # A false claim, not merely malformed evidence: n=4 is infeasible even at
    # 0.50000000001. Recompute valid angular tables and the LOWER proof for the
    # altered endpoints; remove its sole upper witness. Existing checkers must
    # not accept this, regardless of matching hashes / twin reports.
    L,U=F('0.5'),F('0.50000000001');wl,hl=gen.angular_tables(4,L);wu,hu=gen.angular_tables(4,U)
    badrow=copy.deepcopy(basew['certificate']['cases'][1]);badrow.update(L='0.5',U='0.50000000001',upper_witnesses=[],lower_bound=gen.fresh_lower_bound(4,wl,T))
    for a in badrow['angle_intervals_scaled']:
        i,j=a['a'],a['b'];a.update(L_lower=str(wl[i][j]),L_upper=str(hl[i][j]),U_lower=str(wu[i][j]),U_upper=str(hu[i][j]))
        review.verify_angle(F(i*j)/((U+i)*(U+j)),wu[i][j],hu[i][j])
    false_upper_proof=review.audit_lower(4,wu,T)
    need(false_upper_proof['canonical_orders_covered']==3 and int(false_upper_proof['minimum_explicit_angular_margin_scaled'])>0,'false-upper proof failed')
    def false_bracket(c):c['cases'][1]=copy.deepcopy(badrow)
    tests.append(check_mutant('FALSE_n4_bracket_empty_witness',false_bracket,True,True))
    def false_with_47(c):
        false_bracket(c);c['cases'][0]['upper_witnesses'].append(copy.deepcopy(c['cases'][0]['upper_witnesses'][0]))
    tests.append(check_mutant('FALSE_n4_bracket_47_total_witnesses',false_with_47,True,True))
    def bad_L_angle(c):
        row=c['cases'][0];a=row['angle_intervals_scaled'][0];a['L_lower']=a['L_upper'];a['L_upper']=str(int(a['L_upper'])+1)
        W=[[0]*4 for _ in range(4)]
        for e in row['angle_intervals_scaled']:W[e['a']][e['b']]=W[e['b']][e['a']]=int(e['L_lower'])
        row['lower_bound']=gen.fresh_lower_bound(3,W,T)
    tests.append(check_mutant('one_ulp_false_L_angle_rehashed',bad_L_angle,True,False))
    def bad_U_angle(c):c['cases'][1]['angle_intervals_scaled'][0].update(U_lower='0',U_upper='1')
    tests.append(check_mutant('false_U_angle_rehashed',bad_U_angle,True,False))
    def collapsed(c):c['cases'][1]['upper_witnesses'][0]['exact_cartesian_check']['stereographic_parameters'][1]={'numerator':'0','denominator':'1'}
    tests.append(check_mutant('collapsed_cartesian_direction',collapsed,False,False))
    tests.append(check_mutant('wrong_case_coverage',lambda c:c['cases'].pop(),False,False))
    tests.append(check_mutant('wrong_canonical_count',lambda c:c['cases'][1]['lower_bound'].update(canonical_orders_covered=0),True,False))
    def bad_dp_hash(c):c['cases'][-1]['lower_bound'].update(dp_table_sha256='0'*64,pruning_and_skeleton_stream_sha256='0'*64)
    tests.append(check_mutant('unchecked_DP_and_pruning_hashes',bad_dp_hash,True,True))
    # Source-to-input hash linkage is checked by the separate pinned audit main;
    # review.verify checks mathematical content and intentionally ignores it.
    tests.append(check_mutant('unchecked_input_cases_hash',lambda c:c.update(input_cases_sha256='0'*64),True,True))
    # Small brute-force checks of EVERY populated completion state, including
    # asymmetric weights, so an incorrectly directed closing edge is visible.
    rng=random.Random(20260917);dp_cases=dp_states=0
    for m in range(1,7):
        vals=tuple(range(1,m+1))
        for rep in range(6):
            W=[[0]*(m+1) for _ in range(m+1)]
            for i in range(m+1):
                for j in range(i+1,m+1):
                    W[i][j]=rng.randrange(1,100);W[j][i]=W[i][j] if rep<3 else rng.randrange(1,100)
            table,root=gen.completion_table(vals,0,W)
            for mask in range(1<<m):
                members=[vals[k] for k in range(m) if mask>>k&1]
                for j,v in enumerate(vals):
                    if mask>>j&1:need(table[mask][j] is None,'invalid DP state');continue
                    def pathcost(p):
                        seq=(v,)+p+(0,);return sum(W[a][b] for a,b in zip(seq,seq[1:]))
                    want=min(pathcost(p) for p in itertools.permutations(members))
                    need(table[mask][j]==want,'brute DP state disagreement');dp_states+=1
            brute=min(review.cycle_cost((0,)+p,W) for p in itertools.permutations(vals))
            need(root==brute,'brute DP root disagreement');dp_cases+=1
    # Structural hooks: force the original pruning branch onto n=4..9 in a
    # test-only in-memory module. Mock leaf witnesses ONLY to observe which
    # cycles it sends for further checking; this is not a feasibility test.
    forced=memory_module('forced_small_pruning',src/'ringmin_global_interval_replay.py',[('if n <= 9:','if n <= 3:')])
    coverage=[]
    for n in range(4,10):
        W=[[0]*(n+1) for _ in range(n+1)]
        for a,b in itertools.combinations(range(1,n+1),2):W[a][b]=W[b][a]=rng.randrange(1,100)
        skels=[(n,)+p for p in itertools.permutations(range(2,n)) if p<p[::-1]]
        costs=sorted(review.cycle_cost(s,W) for s in skels)
        thresholds=sorted(set([costs[0]-1,costs[0],costs[len(costs)//2],costs[-1]]))
        for threshold in thresholds:
            observed=[]
            def spy(order,weights,tau):observed.append(tuple(order));return 0,1
            forced.lower_witness=spy
            got=forced.fresh_lower_bound(n,W,threshold)
            # Oracle: enumerate full cyclic orders directly; delete 1, score
            # the induced skeleton, and retain exactly those <= threshold.
            want={(n,)+p for p in itertools.permutations(range(1,n)) if p<p[::-1] and review.cycle_cost(tuple(v for v in ((n,)+p) if v!=1),W)<=threshold}
            normal=[review.norm_order(s) for s in observed]
            need(set(normal)==want and len(normal)==len(want),'pruning/insertion coverage disagreement')
            coverage.append({'n':n,'threshold':threshold,'explicit_classes':len(want),'pruned_oriented':got['pruned_oriented_completions']})
    wrong_strict=memory_module('wrong_pruning_comparison',src/'ringmin_global_interval_replay.py',[
        ('if n <= 9:','if n <= 3:'),('if bound > tau_hi:','if bound >= tau_hi:')])
    n=6;W=[[int(a!=b) for b in range(n+1)] for a in range(n+1)]
    wrong_strict.lower_witness=lambda *a:(0,1)
    wrong_result=wrong_strict.fresh_lower_bound(n,W,n-1)
    need(wrong_result['canonical_orders_covered']==math.factorial(n-1)//2,'wrong comparison should still pass factorial count')
    need(wrong_result['explicit_full_orders_checked']==0,'expected equality overpruning')
    # Correct branch must leave all equality cycles explicit.
    forced.lower_witness=lambda *a:(0,1)
    right_result=forced.fresh_lower_bound(n,W,n-1)
    need(right_result['explicit_full_orders_checked']==60,'correct equality handling')
    omit_gap=memory_module('missing_wrap_insertion',src/'ringmin_global_interval_replay.py',[
        ('if n <= 9:','if n <= 3:'),('range(1, len(path)+1)','range(1, len(path))')])
    omit_gap.lower_witness=lambda *a:(0,1)
    missing_gap_rejected=False
    try:omit_gap.fresh_lower_bound(n,W,n-1)
    except gen.CheckFailure:missing_gap_rejected=True
    except Exception as e:
        # Each in-memory module defines its own CheckFailure class.
        need(type(e).__name__=='CheckFailure','unexpected gap exception');missing_gap_rejected=True
    need(missing_gap_rejected,'wrap-gap mutant survived')
    # New exact rational kernel oracles (not the packet's KERNEL_REGRESSION).
    def exact_atan(t,N=512):
        a=t;p=F(0)
        for k in range(N):
            p+=a if k%2==0 else -a
            a*=t*t*F(2*k+1,2*k+3)
        return (p,p+a) if N%2==0 else (p-a,p)
    ts=[F(0),F(1,1000),F(1,3),F(1,2),F(3,4),F(167,241)]+[F(rng.randrange(1,751),1000) for _ in range(24)]
    for t in ts:
        lo,hi,_=receipt.atan_enclosed(t);a,b=exact_atan(t)
        need(F(lo,receipt.P)<=a<=b<=F(hi,receipt.P),'alternate atan versus exact 512-term oracle')
    def exact_cos(x,N=160):
        a=F(1);p=F(0)
        for k in range(N):
            p+=a if k%2==0 else -a
            a*=x*x/F((2*k+1)*(2*k+2))
        return (p,p+a) if N%2==0 else (p-a,p)
    xs=[F(0),F(1,7),F(1),F(3,2),F(2),F(3),F(4)]+[F(rng.randrange(1,4001),1000) for _ in range(15)]
    for x in xs:
        for N in (112,113):
            lo,hi=review.cos_bounds(x,N);a,b=exact_cos(x)
            need(F(lo,review.B)<=a<=b<=F(hi,review.B),'reviewer cosine versus exact oracle')
    qs=[F(1,10**6),F(1,1000),F(1,4),F(1,2),F(89,100),F(899999,10**6)]+[F(rng.randrange(1,900),1000) for _ in range(14)]
    for q in qs:
        lo,hi=gen.angle_enclosure(q);review.verify_angle(q,lo,hi)
        al,ah,_=receipt.pair_angle(q)
        need(lo*(1<<128)<=al<=ah<=hi*(1<<128),'pair kernel agreement')
    bad_domains=0
    for q in [F(-1),F(0),F(9,10),F(1),F(2)]:
        for fn in (gen.angle_enclosure,receipt.pair_angle):
            try:fn(q)
            except Exception:bad_domains+=1
            else:raise AssertionError('invalid angle domain accepted')
    for t in (F(-1,10),F(750001,10**6)):
        try:receipt.atan_enclosed(t)
        except ValueError:bad_domains+=1
        else:raise AssertionError('invalid atan domain accepted')
    need(before=={p.name:review.sha(p.read_bytes()) for p in src.iterdir() if p.is_file()},'original evidence changed')
    report={'status':'COMPLETED_WITH_REPRODUCED_VERIFIER_SOUNDNESS_DEFECT',
      'original_source_unchanged':True,'source_sha256':before,'adversarial_certificate_tests':tests,
      'false_upper_counterexample':{'n':4,'false_L':str(L),'false_U':str(U),
          'independent_lower_proof_at_the_false_U':false_upper_proof,
          'meaning':'All three order classes are infeasible even at the claimed U; nevertheless both packet checkers accept the forged report.'},
      'DP_bruteforce_instances':dp_cases,'DP_nonroot_states_checked':dp_states,
      'DP_symmetric_instances':dp_cases//2,'DP_asymmetric_instances':dp_cases//2,
      'small_pruning_and_insertion_tests':coverage,
      'strict_comparison_mutant':{'detected':True,'n':6,'threshold':5,'correct_explicit':60,'incorrect_explicit':0,'factorial_metadata_still_passed':True},
      'missing_closing_insertion_gap_mutant_rejected':missing_gap_rejected,
      'alternate_atan_exact_512term_tests':len(ts),'reviewer_cosine_exact_160term_tests':len(xs)*2,
      'pair_kernel_cosine_and_alternate_tests':len(qs),'invalid_domains_rejected':bad_domains,
      'seconds':time.perf_counter()-start,
      'notes':['Tests use scratch reports and in-memory mutants only.','Mock leaf tests check traversal structure, not geometric infeasibility.','The original pinned certificate is not invalidated by a verifier accepting other false certificates.']}
    (out/'adversarial_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('source_sha256','adversarial_certificate_tests','small_pruning_and_insertion_tests','false_upper_counterexample','notes')},indent=2))
if __name__=='__main__':main()
