# Lab 5: Static Code Analysis - Hospital Patient System

This submission analyzes and improves `hospital_patient_system.py` with Pylint, Bandit, and Flake8.

## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

## Run the application

```powershell
python hospital_patient_system.py
```

The example exports `patient_records.txt` in the current directory. It is generated at runtime and is excluded from Git.

## Recreate the reports

```powershell
pylint hospital_patient_system.py > pylint_report.txt
bandit -r hospital_patient_system.py > bandit_report.txt
flake8 hospital_patient_system.py > flake8_report.txt
```

The final reports are included at the repository root. Baseline reports are in `reports/before/`; a copy of the final reports is in `reports/after/`.

## Submission files

- `hospital_patient_system.py` - cleaned application.
- `issues.md` - findings and fixes, with original source line references.
- `reflection.md` - four reflection answers. The handout refers to questions but does not print their text, so the prompts are stated in terms of the listed learning outcomes.
- `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` - final analyzer output.
- `reports/before/` and `reports/after/` - baseline and final report copies.

Three local commits record the quality fixes, Bandit security fixes, and final formatting/submission work. No remote changes were made.
