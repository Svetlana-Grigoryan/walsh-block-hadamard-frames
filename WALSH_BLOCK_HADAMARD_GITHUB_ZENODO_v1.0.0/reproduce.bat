@echo off
python code\run_all.py
if errorlevel 1 exit /b 1
echo All verification scripts completed successfully.
