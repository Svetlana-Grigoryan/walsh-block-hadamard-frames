import numpy as np
from frames import frame, structured_decoder

N, r = 64, 1
rng = np.random.default_rng(20260906)
F = frame(N,r)
x = rng.standard_normal(N)
E = np.sort(rng.choice(2*N, size=12, replace=False))
keep = np.ones(2*N,dtype=bool); keep[E]=False
y = F[keep] @ x
xh = structured_decoder(N,r,E,y)
print('relative reconstruction error =', np.linalg.norm(xh-x)/np.linalg.norm(x))
