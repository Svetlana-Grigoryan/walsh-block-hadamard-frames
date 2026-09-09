# Reproducibility protocol

## 1. Environment

The provided Conda specification uses Python 3.11. The archived verification run was also completed successfully with Python 3.13.5.

Minimum package requirements:
- NumPy >= 1.26
- SciPy >= 1.11
- pandas >= 2.1
- Matplotlib >= 3.8

Install with either `requirements.txt` or `environment.yml`. Exact package versions from the verified environment are recorded in `requirements-lock.txt`.

## 2. Run all verification scripts

From the repository root:

```bash
python code/run_all.py
```

The driver executes:
1. `exhaustive_verify.py`
2. `verify_sharp_profiles.py`
3. `random_profiles.py`
4. `bound_tightness.py`
5. `decoder_check.py`
6. `verify_critical_counts.py`
7. `weighted_stability_check.py`

A nonzero exit code indicates a failed verification.

## 3. Expected machine-readable outputs

The scripts write/update files in `results/`, including:
- `exhaustive_thresholds.csv`
- `sharp_profile_exhaustive_small.csv`
- `random_profiles_N64_2000.csv`
- `bound_tightness_N64_r1.csv`
- `critical_count_checks.csv`
- `weighted_stability_check.txt`
- decoder, exhaustive, and random console summaries

The repository contains the verified outputs corresponding to the archived release.

## 4. Figure generation

Run:

```bash
python code/make_new_figures.py
```

This regenerates:
- `figures/sharp_profile_m16.pdf`
- `figures/dyadic_vs_extremal_m16.pdf`

The other PDFs in `figures/` are retained as verified reproducibility snapshots supporting the computational record.

## 5. Numerical conventions

- Rank tolerance: `1e-10`.
- Monte-Carlo experiments use fixed seeds defined inside the corresponding scripts.
- Rank-deficient cases are represented by smallest singular values at numerical zero within the stated tolerance.
- Wilson 95% intervals apply only to sampled Monte-Carlo success probabilities.

## 6. Scope

The analytical proofs in the associated article are the scientific basis of the exact theorems. This public archive checks implementations, confirms selected small-dimensional cases exhaustively, reproduces numerical tables and figures, and illustrates typical random-erasure behavior.

The unpublished manuscript source and manuscript PDF are intentionally excluded from this release.

## 7. Integrity

On Linux/macOS, verify the archive with:

```bash
sha256sum -c SHA256SUMS.txt
```

On Windows PowerShell, compute hashes using `Get-FileHash -Algorithm SHA256` and compare them with `SHA256SUMS.txt`.
