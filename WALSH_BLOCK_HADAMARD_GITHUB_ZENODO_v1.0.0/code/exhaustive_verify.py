import itertools
import numpy as np
import pandas as pd
from frames import frame, e_star_formula, surviving_sigma_min

CASES = [(4,0),(4,1),(4,2),(8,0),(8,1),(8,2),(8,3),(16,1),(16,2),(16,3),(16,4)]
TOL = 1e-10
rows = []
for n, r in CASES:
    e = e_star_formula(n, r)
    F = frame(n, r)
    fail = 0
    min_positive = np.inf
    for E in itertools.combinations(range(2*n), e):
        s = surviving_sigma_min(F, E)
        if s <= TOL:
            fail += 1
        else:
            min_positive = min(min_positive, s)
    rows.append(dict(N=n, r=r, theory_e_star=e,
                     failing_subsets_at_e_star=fail,
                     min_positive_sigma_at_e_star=min_positive))

pd.DataFrame(rows).to_csv('../results/exhaustive_thresholds.csv', index=False)
print(pd.DataFrame(rows).to_string(index=False))
