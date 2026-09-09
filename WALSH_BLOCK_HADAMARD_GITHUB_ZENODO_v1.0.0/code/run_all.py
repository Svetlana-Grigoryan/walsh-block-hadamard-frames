import subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
scripts = [
    'exhaustive_verify.py',
    'verify_sharp_profiles.py',
    'random_profiles.py',
    'bound_tightness.py',
    'decoder_check.py',
    'verify_critical_counts.py',
    'weighted_stability_check.py',
]
for s in scripts:
    print(f'=== {s} ===')
    subprocess.run([sys.executable, s], cwd=HERE, check=True)
print('All verification scripts completed successfully.')
