#!/usr/bin/env python3
"""Read-only verifier written for the 2026-09-17 STRICT review.

No imports from the packet or Ringmin. Stdlib only. Angles are independently
checked using cos(theta)=1-2q and outward cosine-series enclosures at 224 bits.
The lower computation uses forward Held-Karp paths (reverse of completion
paths); geometry uses explicit Cartesian coordinates and cross-product polar
ordering. This is an audit implementation, not proof-assistant verification.
"""
from __future__ import annotations
import argparse, ast, hashlib, itertools, json, math, platform, sys, time
from fractions import Fraction as F
from functools import cmp_to_key
from pathlib import Path

B = 1 << 224
S = 1 << 128
ENDPOINTS = [
 (3,'0.26086956521','0.26086956522',1),
 (4,'0.84445358956','0.84445358957',1),
 (5,'1.69549408120','1.69549408121',1),
 (6,'2.79491951889','2.79491951890',1),
 (7,'4.15318955374','4.15318955375',1),
 (8,'5.76779428458','5.76779428459',1),
 (9,'7.72672655261','7.72672655262',1),
 (10,'9.97990738586','9.97990738587',4),
 (11,'12.48872048718','12.48872048719',6),
 (12,'15.25887043044','15.25887043045',9),
 (13,'18.31756304721','18.31756304722',10),
 (14,'21.66539518221','21.66539518222',11)]

def need(ok, msg):
    if not ok: raise ValueError(msg)

def sha(x): return hashlib.sha256(x).hexdigest()
def canonical(x): return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False).encode('ascii')
def unique(pairs):
    out={}
    for k,v in pairs:
        need(k not in out, 'duplicate JSON key: '+k)
        out[k]=v
    return out

def read(path):
    def bad(x): raise ValueError('nonfinite JSON: '+x)
    return json.loads(Path(path).read_bytes(), object_pairs_hook=unique, parse_constant=bad)

def ceildiv(a,b):
    need(b>0, 'nonpositive denominator')
    return -((-a)//b)

def sint(x):
    need(isinstance(x,str) and str(int(x))==x,'noncanonical scaled integer')
    return int(x)

def cos_bounds(x: F, terms: int=112):
    """Bounds B*cos(x) using alternating series, exact outward integer arithmetic.

    The first omitted absolute term bounds the remainder: the tail terms are
    decreasing after the chosen cutoff. No claim that early terms decrease is
    made (for x>sqrt(2) they need not). All operations prior to cutoff retain
    independent lower/upper bounds on each positive absolute term.
    """
    need(isinstance(x,F) and 0<=x<=4 and terms>=4, 'cos domain/cutoff')
    xx=x*x; a,d=xx.numerator,xx.denominator
    low=high=B; lo=hi=0
    for k in range(terms):
        if k%2: lo-=high; hi-=low
        else: lo+=low; hi+=high
        den=d*(2*k+1)*(2*k+2)
        low=low*a//den; high=ceildiv(high*a,den)
    need(xx < (2*terms+1)*(2*terms+2), 'cos tail must decrease')
    if terms%2: lo-=high
    else: hi+=high
    need(lo<=hi,'cos endpoint ordering')
    return lo,hi

def verify_tau(lo,hi):
    need(6*S<lo<hi<7*S, 'tau location')
    # On (0,pi), cos is strictly decreasing. pi>3 is a standard elementary
    # bound. The zero enclosed in (1.5,1.75) is pi/2; therefore tau=2*pi.
    need(cos_bounds(F(lo,4*S))[0]>0, 'tau lower fails independent cosine test')
    need(cos_bounds(F(hi,4*S))[1]<0, 'tau upper fails independent cosine test')

def verify_angle(q,lo,hi):
    need(0<q<F(9,10), 'angle q domain')
    need(0<lo<=hi<3*S and hi-lo<=2, 'angle interval schema/domain')
    target=1-2*q
    # Both endpoints are in (0,3), where cos is decreasing since pi>3.
    need(F(cos_bounds(F(lo,S))[0],B)>target, 'false angular LOWER endpoint')
    need(F(cos_bounds(F(hi,S))[1],B)<target, 'false angular UPPER endpoint')

def norm_order(seq):
    seq=tuple(seq); k=seq.index(max(seq)); a=seq[k:]+seq[:k]
    return min(a,a[:1]+a[:0:-1])

def cycle_cost(seq,W): return sum(W[a][b] for a,b in zip(seq,seq[1:]+seq[:1]))

def forward_dp(vertices,anchor,W):
    """D[(mask,j)] is the minimum path anchor -> vertices(mask), ending in j."""
    m=len(vertices); D={}
    for mask in range(1,1<<m):
        members=[j for j in range(m) if mask>>j&1]
        for j in members:
            prev=mask^(1<<j)
            D[mask,j] = (W[anchor][vertices[j]] if not prev else
                         min(D[prev,k]+W[vertices[k]][vertices[j]] for k in members if k!=j))
    full=(1<<m)-1
    return D,min(D[full,j]+W[vertices[j]][anchor] for j in range(m))

def audit_lower(n,W,T):
    expected=math.factorial(n-1)//2
    counts=[0,0,0]; margins=[]; witness_hash=hashlib.sha256(); normal=set(); raw_noncanonical=0
    def inspect(seq):
        nonlocal raw_noncanonical
        seq=tuple(seq); found=False
        for k in range(3):
            subset=tuple(v for v in seq if v>k)
            if len(subset)>=3:
                gap=cycle_cost(subset,W)-T
                if gap>0:
                    counts[k]+=1; margins.append(gap)
                    witness_hash.update(bytes(seq)+bytes([k]));found=True;break
        need(found,'UNPROVEN lower order '+repr(seq))
        can=norm_order(seq)
        need(can not in normal,'duplicate explicit cyclic-order class')
        normal.add(can);raw_noncanonical+=int(seq!=can)
    if n<=9:
        for p in itertools.permutations(range(1,n)):
            if p<p[::-1]: inspect((n,)+p)
        need(len(normal)==expected,'small exhaustive coverage')
        return dict(canonical_orders_covered=expected,explicit_full_orders_checked=len(normal),
                    witness_counts_full_remove1_remove12=counts,
                    minimum_explicit_angular_margin_scaled=str(min(margins)),
                    explicit_order_witness_sha256=witness_hash.hexdigest(),
                    raw_noncanonical_explicit_tuples=raw_noncanonical)
    vals=tuple(range(2,n));m=len(vals);full=(1<<m)-1
    need(all(W[a][b]==W[b][a] for a in range(1,n+1) for b in range(1,n+1)), 'reverse DP requires symmetric weights')
    D,root=forward_dp(vals,n,W)
    # Reversal: a completion v -> M -> anchor has cost D[M union {v},v].
    dp_stream=[[mask,j,str(D[mask|(1<<j),j])] for mask in range(1<<m) for j in range(m) if not mask>>j&1]
    stack=[((n,),full,0,None)]
    nodes=prunes=pruned=kept=reversed_leaves=0; prune_margins=[]; pruning_hash=hashlib.sha256()
    while stack:
        seq,mask,cost,j=stack.pop();nodes+=1
        bound=root if j is None else cost+D[mask|(1<<j),j]
        if bound>T:
            prunes+=1; pruned+=math.factorial(mask.bit_count());prune_margins.append(bound-T)
            pruning_hash.update(b'P'+bytes(seq)+b':'+str(mask).encode()+b';')
        elif not mask:
            need(bound==cost+W[seq[-1]][n], 'closing edge mismatch')
            if seq!=norm_order(seq): reversed_leaves+=1;continue
            kept+=1;pruning_hash.update(b'E'+bytes(seq)+b';')
            for gap in range(len(seq)):
                p=gap+1; inspect(seq[:p]+(1,)+seq[p:])
        else:
            for k in range(m-1,-1,-1):
                if mask>>k&1:
                    v=vals[k];stack.append((seq+(v,),mask^(1<<k),cost+W[seq[-1]][v],k))
    need(reversed_leaves==kept and pruned+2*kept==math.factorial(n-2),'oriented skeleton coverage')
    need(pruned%2==0 and len(normal)==(n-1)*kept,'reflection / insertion count')
    need(pruned*(n-1)//2+len(normal)==expected,'full coverage')
    return dict(canonical_orders_covered=expected, explicit_full_orders_checked=len(normal),
                witness_counts_full_remove1_remove12=counts,
                minimum_explicit_angular_margin_scaled=str(min(margins)) if margins else None,
                explicit_order_witness_sha256=witness_hash.hexdigest(),
                dp_states=len(D)+1,dp_root_cost_minus_tau_hi_scaled=str(root-T),
                dp_table_sha256=sha(canonical(dp_stream)),nodes=nodes,pruned_subtrees=prunes,
                pruned_oriented_completions=pruned,canonical_skeletons_expanded=kept,
                reversed_leaves_omitted=reversed_leaves,
                full_canonical_orders_covered_by_pruning=pruned*(n-1)//2,
                minimum_prune_angular_margin_scaled=str(min(prune_margins)) if prune_margins else None,
                pruning_and_skeleton_stream_sha256=pruning_hash.hexdigest(),
                raw_noncanonical_explicit_tuples=raw_noncanonical)

def compare_polar(a,b):
    def half(p): return 0 if (p[1]>0 or p[1]==0 and p[0]>0) else 1
    ha,hb=half(a),half(b)
    if ha!=hb:return -1 if ha<hb else 1
    cross=a[0]*b[1]-a[1]*b[0]
    return -1 if cross>0 else 1 if cross<0 else 0

def audit_geometry(row,HU,tau_lo,pad):
    n=row['n'];R=F(row['U']);ws=row['upper_witnesses']
    need(isinstance(ws,list) and len(ws)>0,'MISSING existential upper witness n='+str(n))
    pairs=tangent=angular=0;minima=[];seen=set()
    for w in ws:
        order=w['order'];need(len(order)==n and all(type(v)is int for v in order) and set(order)==set(range(1,n+1)), 'witness radius set')
        co=norm_order(order);need(co not in seen,'duplicate witness order');seen.add(co)
        x=[sint(v) for v in w['positions_scaled_integers']]
        need(len(x)==n and x[0]==0 and all(a<b for a,b in zip(x,x[1:])) and x[-1]<tau_lo,'angular ordering')
        ag=[]
        for i,j in itertools.combinations(range(n),2):
            d=x[j]-x[i];h=HU[order[i]][order[j]]
            ag.extend([d-h,tau_lo-d-h]);angular+=2
        need(min(ag)>=pad and sint(w['minimum_verified_all_pairs_slack_scaled'])==min(ag),'angular slack')
        need(w['pair_constraints_checked']==n*(n-1),'angular pair count')
        data=w['exact_cartesian_check'];pars=data['stereographic_parameters']
        need(len(pars)==n,'stereographic parameter count')
        centers=[];directions=[]
        for r,p in zip(order,pars):
            num,den=sint(p['numerator']),sint(p['denominator']);need(den>0,'parameter denominator')
            t=F(num,den);dx=(1-t*t)/(1+t*t);dy=2*t/(1+t*t)
            cx=(R+r)*dx;cy=(R+r)*dy
            need(cx*cx+cy*cy==(R+r)**2,'central tangency')
            tangent+=1;centers.append((cx,cy));directions.append((dx,dy))
        need(directions[0]==(1,0),'Cartesian anchor')
        need(sorted(directions,key=cmp_to_key(compare_polar))==directions and len(set(directions))==n,'Cartesian polar order')
        gaps=[]
        for i,j in itertools.combinations(range(n),2):
            dx=centers[i][0]-centers[j][0];dy=centers[i][1]-centers[j][1]
            gap=dx*dx+dy*dy-(order[i]+order[j])**2
            need(gap>0,'Cartesian overlap');gaps.append(gap);pairs+=1
        mn=data['minimum_squared_distance_gap'];want=F(sint(mn['numerator']),sint(mn['denominator']))
        need(min(gaps)==want,'stored Cartesian minimum')
        need(data['central_tangencies_checked']==n and data['outer_pairs_checked']==n*(n-1)//2,'Cartesian count metadata')
        minima.append(str(want))
    return dict(witnesses=len(ws),central_tangencies=tangent,outer_pairs=pairs,angular_inequalities=angular,
                minimum_squared_gap_per_witness=minima)

def verify(report, pinned=True):
    c=report['certificate'];need(sha(canonical(c))==report['certificate_sha256'],'certificate digest')
    need(sint(c['scale_denominator'])==S,'scale denominator')
    tau_lo,tau_hi=sint(c['tau_lower_scaled']),sint(c['tau_upper_scaled']);verify_tau(tau_lo,tau_hi)
    pad=sint(c['placement_padding_scaled']);need(pad==ceildiv(S,10**16),'positive constructive padding')
    need([r['n'] for r in c['cases']]==list(range(3,15)) and all(type(r['n'])is int for r in c['cases']),'case coverage')
    rows=[];total_angles=0
    for row,ep in zip(c['cases'],ENDPOINTS):
        n=row['n'];L,U=F(row['L']),F(row['U'])
        need(0<L<U and U-L==F(1,10**11),'bracket width')
        if pinned: need((n,L,U)==(ep[0],F(ep[1]),F(ep[2])),'endpoints do not match reviewed packet')
        recs=row['angle_intervals_scaled'];want_pairs=set(itertools.combinations(range(1,n+1),2))
        need(len(recs)==len(want_pairs) and {(r['a'],r['b']) for r in recs}==want_pairs,'pair table completeness')
        WL=[[0]*(n+1) for _ in range(n+1)]; HU=[[0]*(n+1) for _ in range(n+1)]
        deriv=[]
        for r in recs:
            a,b=r['a'],r['b'];need(type(a)is int and type(b)is int,'pair labels')
            for key,Q in [('L',L),('U',U)]:
                q=F(a*b)/((Q+a)*(Q+b));lo,hi=sint(r[key+'_lower']),sint(r[key+'_upper'])
                verify_angle(q,lo,hi);total_angles+=1
                if key=='L':
                    WL[a][b]=WL[b][a]=lo
                    z=q/(1-q)
                    deriv.append(max(F(1),z)*(1/(L+a)+1/(L+b)))
                else: HU[a][b]=HU[b][a]=hi
        # Check existence before expensive full lower computation.
        geo=audit_geometry(row,HU,tau_lo,pad)
        if pinned:need(geo['witnesses']==ep[3],'pinned witness count')
        lower=audit_lower(n,WL,tau_hi)
        for key,value in lower.items():
            if key!='raw_noncanonical_explicit_tuples':need(row['lower_bound'].get(key)==value,'lower metadata '+str(n)+' '+key)
        m=min(int(lower[k]) for k in ('minimum_explicit_angular_margin_scaled','minimum_prune_angular_margin_scaled') if lower.get(k) is not None)
        need(m>0,'strict lower margin')
        # For Q>=L, |phi_ab'(Q)| <= max(1,q/(1-q))*(1/(L+a)+1/(L+b)).
        # Every selected cycle uses at most n edges. This gives a constructive
        # positive buffer beyond L, without assuming attainment of the infimum.
        eps=F(m,2*S)/(n*max(deriv));need(0<eps<U-L,'strictness buffer inconsistent with U')
        rows.append(dict(n=n,L=str(L),U=str(U),lower=lower,geometry=geo,
                         strict_lower_radius_buffer=str(eps),minimum_angular_margin_scaled=str(m)))
    return dict(status='PASS_REVIEWER_INDEPENDENT_CHECK',certificate_sha256=report['certificate_sha256'],
                angles_verified_by_cosine=total_angles,tau_verified_by_cosine_zero=True,
                witnesses=sum(r['geometry']['witnesses'] for r in rows),
                central_tangencies=sum(r['geometry']['central_tangencies'] for r in rows),
                outer_pairs=sum(r['geometry']['outer_pairs'] for r in rows),
                angular_inequalities=sum(r['geometry']['angular_inequalities'] for r in rows),
                explicit_order_classes=sum(r['lower']['explicit_full_orders_checked'] for r in rows),
                all_order_classes_covered=sum(r['lower']['canonical_orders_covered'] for r in rows),cases=rows)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();t0=time.perf_counter();p=args.source
    before={f.name:sha(f.read_bytes()) for f in p.iterdir() if f.is_file()}
    manifest=read(p/'packet_manifest.json')
    need(set(before)=={f['name'] for f in manifest['files']}|{'packet_manifest.json'},'unexpected archive member set')
    for r in manifest['files']:
        need(before[r['name']]==r['sha256'] and (p/r['name']).stat().st_size==r['bytes'],'source fingerprint '+r['name'])
    windows=read(p/'global_interval_replay_20260917T101809Z_3399172f.json');linux=read(p/'ringmin_global_interval_candidate.json')
    need(canonical(windows['certificate'])==canonical(linux['certificate']),'Windows/Linux payload difference')
    source=p/'ringmin_global_interval_replay.py';tree=ast.parse(source.read_text())
    assignments=[a for a in tree.body if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CASES' for t in a.targets)]
    cases=json.loads(ast.literal_eval(assignments[0].value.args[0]))
    need(windows['certificate']['input_cases_sha256']==sha(canonical(cases)), 'source input cases digest')
    need(windows['script_sha256']==linux['script_sha256']==before[source.name], 'script digest')
    for case,row in zip(cases,windows['certificate']['cases']):
        need((case['n'],F(case['L']),F(case['U']),case['orders'])==(row['n'],F(row['L']),F(row['U']),[w['order'] for w in row['upper_witnesses']]), 'source to certificate case correspondence')
    result=verify(windows)
    need(before=={f.name:sha(f.read_bytes()) for f in p.iterdir() if f.is_file()},'source files changed')
    result.update(source_sha256=before,source_unchanged=True,python=sys.version,platform=platform.platform(),seconds=time.perf_counter()-t0,
                  method='cosine 224-bit; forward Held-Karp; explicit rational Cartesian and cross-product ordering',
                  limitations=['Not a proof-assistant proof or human peer review.','Does not validate historical Top-K pruning or unseen checkpoint bytes.'])
    with args.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','source_sha256','limitations')},indent=2))
if __name__=='__main__':main()
