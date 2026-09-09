import math
import numpy as np
import pandas as pd
from frames import frame, surviving_sigma_min

N = 64
RS = [0,1,2,3]
ES = [6,13,26,38,51]
TRIALS = 2000
BASE_SEED = 20260906
TOL = 1e-10


def wilson(k, n, z=1.96):
    p = k/n
    d = 1 + z*z/n
    c = (p + z*z/(2*n))/d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c-h, c+h

rows=[]
for r in RS:
    rng = np.random.default_rng(BASE_SEED + 100*r)
    F = frame(N,r)
    for e in ES:
        sig=[]
        for _ in range(TRIALS):
            E = rng.choice(2*N, size=e, replace=False)
            sig.append(surviving_sigma_min(F,E))
        sig=np.asarray(sig)
        k=int(np.sum(sig>TOL))
        lo,hi=wilson(k,TRIALS)
        rows.append(dict(N=N,r=r,e=e,frac=e/(2*N),success=k/TRIALS,
                         ci_lo=lo,ci_hi=hi,median_sigma=np.median(sig),
                         p05_sigma=np.quantile(sig,0.05)))

df=pd.DataFrame(rows)
df.to_csv('../results/random_profiles_N64_2000.csv',index=False)
print(df.to_string(index=False))
