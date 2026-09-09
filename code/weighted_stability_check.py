import numpy as np
from frames import hadamard_normalized, block_hadamard

N = 16
r = 1
I = np.array([0, 3, 5])
J = np.array([1, 4])
H = hadamard_normalized(N)
R = block_hadamard(N, r)
C = H[I] @ R[J].T
c = np.linalg.svd(C, compute_uv=False)[0]

thetas = np.array([0.2, 0.35, 0.5, 0.65, 0.8])
rows = []
for th in thetas:
    F = np.vstack([np.sqrt(th)*H, np.sqrt(1-th)*R])
    erased = np.r_[I, N + J]
    keep = np.ones(2*N, dtype=bool)
    keep[erased] = False
    exact = np.linalg.svd(F[keep], compute_uv=False)[-1]
    formula_sq = (1 - np.sqrt((2*th-1)**2 + 4*th*(1-th)*c*c))/2
    formula = np.sqrt(max(formula_sq, 0.0))
    rows.append((th, exact, formula))

with open('../results/weighted_stability_check.txt', 'w', encoding='utf-8') as f:
    f.write('theta exact_sigma formula_sigma\n')
    for row in rows:
        f.write(f'{row[0]:.2f} {row[1]:.12f} {row[2]:.12f}\n')
print('theta exact_sigma formula_sigma')
for row in rows:
    print(f'{row[0]:.2f} {row[1]:.12f} {row[2]:.12f}')
