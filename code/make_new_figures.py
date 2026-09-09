import math
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIGDIR = ROOT / 'figures'
FIGDIR.mkdir(parents=True, exist_ok=True)

# Exact worst-case profile for m=16 (e.g. N=64,r=2), where s=4 is even.
m=16
e_star=8
es=np.arange(0,17)
g=[]
for e in es:
    if e==0:
        g.append(1.0)
    elif e==1:
        g.append(1/math.sqrt(2))
    elif e<e_star:
        p=e//2; q=e-p
        g.append(math.sqrt((1-math.sqrt(p*q/m))/2))
    else:
        g.append(0.0)
plt.figure(figsize=(6.4,4.2))
plt.plot(es,g,marker='o')
plt.xlabel('Number of erased coefficients e')
plt.ylabel(r'$\gamma_{N,r}(e)$')
plt.title('Exact worst-case stability profile for m=16')
plt.grid(True,alpha=.25)
plt.tight_layout()
plt.savefig(FIGDIR / 'sharp_profile_m16.pdf')
plt.close()

# Compare rank-one extremal geometry against aligned dyadic blocks for equal block sizes k=1,2,4,8,16 in m=16.
ks=np.array([1,2,4,8,16])
extremal=np.sqrt(ks*ks/m)
dyadic=np.sqrt(ks/m)
plt.figure(figsize=(6.4,4.2))
plt.plot(ks,extremal,marker='o',label='orthogonal-subspace rank-one blocks')
plt.plot(ks,dyadic,marker='s',label='aligned dyadic intervals')
plt.xlabel('Block size k=|I|=|J|')
plt.ylabel(r'$\|H_m[I,J]\|_2$')
plt.title('Partial Walsh norms for two structured geometries (m=16)')
plt.legend()
plt.grid(True,alpha=.25)
plt.tight_layout()
plt.savefig(FIGDIR / 'dyadic_vs_extremal_m16.pdf')
plt.close()
