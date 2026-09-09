import math
import numpy as np
import pandas as pd
from frames import frame, surviving_sigma_min

N, r = 64, 1
ES = [4, 8, 12, 16]
TRIALS = 1000
SEED = 42
m = N // (2**r)
bsize = 2**r
rng = np.random.default_rng(SEED)
F = frame(N,r)


def lower_bound(E):
    I = [i for i in E if i < N]
    J = [i-N for i in E if i >= N]
    if not I or not J:
        return 1/math.sqrt(2)
    ic=[0]*bsize; jc=[0]*bsize
    for i in I: ic[i % bsize] += 1
    for j in J: jc[j % bsize] += 1
    alpha=max(math.sqrt(ic[b]*jc[b]/m) for b in range(bsize))
    return math.sqrt(max(0.0,(1-alpha)/2))

rows=[]
for e in ES:
    exact=[]; bound=[]
    for _ in range(TRIALS):
        E=np.sort(rng.choice(2*N,size=e,replace=False))
        exact.append(surviving_sigma_min(F,E))
        bound.append(lower_bound(E))
    exact=np.asarray(exact); bound=np.asarray(bound)
    rows.append(dict(e=e,median_exact_sigma=np.median(exact),median_bound=np.median(bound),
                     p05_exact_sigma=np.quantile(exact,.05),p05_bound=np.quantile(bound,.05),
                     median_gap=np.median(exact-bound)))

pd.DataFrame(rows).to_csv('../results/bound_tightness_N64_r1.csv',index=False)
print(pd.DataFrame(rows).to_string(index=False))
