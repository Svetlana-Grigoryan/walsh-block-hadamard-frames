import numpy as np
from scipy.linalg import hadamard


def hadamard_normalized(n: int) -> np.ndarray:
    return hadamard(n).astype(float) / np.sqrt(n)


def block_hadamard(n: int, r: int) -> np.ndarray:
    if r < 0 or r > int(np.log2(n)):
        raise ValueError('r must satisfy 0 <= r <= log2(n)')
    if r == 0:
        return np.eye(n)
    b = 2 ** r
    return np.kron(np.eye(n // b), hadamard_normalized(b))


def frame(n: int, r: int) -> np.ndarray:
    H = hadamard_normalized(n)
    R = block_hadamard(n, r)
    return np.vstack([H, R]) / np.sqrt(2.0)


def e_star_formula(n: int, r: int) -> int:
    m = n // (2 ** r)
    s = int(np.log2(m))
    return min(2 ** j + 2 ** (s - j) for j in range(s + 1))


def surviving_sigma_min(F: np.ndarray, erased) -> float:
    keep = np.ones(F.shape[0], dtype=bool)
    keep[np.asarray(erased, dtype=int)] = False
    return float(np.linalg.svd(F[keep], compute_uv=False)[-1])


def erasure_cross_gram(n: int, r: int, I, J) -> np.ndarray:
    H = hadamard_normalized(n)
    R = block_hadamard(n, r)
    I = np.asarray(I, dtype=int)
    J = np.asarray(J, dtype=int)
    return H[I, :] @ R[J, :].T


def structured_decoder(n: int, r: int, erased, observed_survivors) -> np.ndarray:
    """Known-erasure decoder using an erasure-sized Woodbury solve.

    observed_survivors must be ordered as the surviving rows of F.
    """
    F = frame(n, r)
    erased = np.asarray(sorted(erased), dtype=int)
    keep = np.ones(2 * n, dtype=bool)
    keep[erased] = False
    Fs = F[keep]
    D = F[erased]
    z = Fs.T @ np.asarray(observed_survivors, dtype=float)
    if erased.size == 0:
        return z
    G = np.eye(erased.size) - D @ D.T
    w = np.linalg.solve(G, D @ z)
    return z + D.T @ w
