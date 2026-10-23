"""Bounded arithmetic replay; universal statements remain analytic. Rejects -O."""
from pathlib import Path
import argparse
import subprocess
import sys

HERE=Path(__file__).resolve().parent
CHECKS=("upper_lambda.py","upper_alpha_minimum.py","upper_boundary.py",
        "upper_mixed_width.py","upper_fourth_block.py")
def main():
    if not __debug__:
        raise SystemExit("FAIL: assertions must remain enabled; do not use -O")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--with-lp",action="store_true",help="Also run existing SciPy candidate-discovery/exact checker")
    args=parser.parse_args()
    lower=HERE/"lower_supplement"
    if not lower.is_dir():
        lower=HERE.parent/"asymptotic_sequel/proposition7_supplement"
    for script in [lower/"verify.py", lower/"check_integrity_controls.py",
                   HERE/"checks/check_line_recovery.py",
                   *(HERE/"checks"/name for name in CHECKS)]:
        print("RUN",script.name,flush=True)
        extra = ["--exact-only"] if script.name in ("upper_lambda.py","upper_alpha_minimum.py") else []
        subprocess.run([sys.executable,"-I","-S",str(script),*extra],cwd=script.parent,check=True)
    if args.with_lp:
        script=HERE/"checks/check_word_lp.py"
        print("RUN",script.name,"(SciPy discovery; exact Fraction verification)",flush=True)
        subprocess.run([sys.executable,"-I",str(script)],cwd=script.parent,check=True)
    print("PASS bounded arithmetic replay; universal quantifiers require the written proofs")
if __name__=="__main__":
    main()
