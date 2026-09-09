import itertools, math, csv
from pathlib import Path
import numpy as np


def hadamard_normalized(m):
    H=np.array([[1.0]])
    while H.shape[0] < m:
        H=np.block([[H,H],[H,-H]])/np.sqrt(2.0)
    return H


def exact_max_partial_norm(m,e):
    H=hadamard_normalized(m)
    best=0.0
    best_pq=None
    for p in range(1,e):
        q=e-p
        if p>m or q>m:
            continue
        for I in itertools.combinations(range(m),p):
            for J in itertools.combinations(range(m),q):
                val=np.linalg.norm(H[np.ix_(I,J)],2)
                if val > best + 1e-13:
                    best=val
                    best_pq=(p,q)
    return best,best_pq


def theorem_condition(m,e):
    if e<2:
        return True
    s=int(round(math.log2(m)))
    p=e//2
    q=e-p
    return math.ceil(math.log2(p))+math.ceil(math.log2(q)) <= s

rows=[]
# Full exhaustive check is feasible for m<=8 over the ranges below.
for m,max_e in [(2,3),(4,4),(8,5)]:
    for e in range(2,max_e+1):
        exact,pq=exact_max_partial_norm(m,e)
        p=e//2; q=e-p
        pred=math.sqrt(p*q/m)
        cond=theorem_condition(m,e)
        rows.append([m,e,cond,exact,pred,abs(exact-pred),pq])
        if cond and abs(exact-pred)>1e-10:
            raise RuntimeError((m,e,exact,pred,pq))

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'results' / 'sharp_profile_exhaustive_small.csv'
with open(out,'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['m','e','theorem_condition','exact_max_partial_norm','predicted_rank_one_norm','abs_error','argmax_branch_sizes'])
    w.writerows(rows)
print('All theorem-range exhaustive checks passed.')
for r in rows:
    print(r)
