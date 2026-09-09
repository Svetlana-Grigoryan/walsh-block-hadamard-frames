import math
import pandas as pd


def gaussian_binomial_2(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    num = 1
    den = 1
    for j in range(k):
        num *= 2 ** (n - j) - 1
        den *= 2 ** (k - j) - 1
    return num // den


def predicted_count(N: int, r: int) -> int:
    m = N // (2 ** r)
    s = int(round(math.log2(m)))
    if 2 ** s != m or s % 2:
        raise ValueError('This count formula is for m=2^(2t).')
    t = s // 2
    return N * gaussian_binomial_2(2*t, t)

cases = [(8, 1, 24), (16, 2, 48), (16, 0, 560)]
rows = []
for N, r, expected in cases:
    pred = predicted_count(N, r)
    rows.append({'N': N, 'r': r, 'predicted_count': pred,
                 'comparison_value': expected, 'match': pred == expected})

out = pd.DataFrame(rows)
out.to_csv('../results/critical_count_checks.csv', index=False)
print(out.to_string(index=False))
