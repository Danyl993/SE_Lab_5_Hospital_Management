# Static analysis findings

Baseline findings below are ordered by severity. Line numbers refer to the original `hospital_patient_system.py` from the assigned repository.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command built from filename | High, Bandit B605 | 56 | `os.system` runs a shell command concatenated with a caller-controlled filename, creating a command-injection risk. | Remove the shell call and report the path with Python `print`. |
| Weak patient hash | High, Bandit B324 | 45 | MD5 is not collision resistant and is unsuitable as a security hash. | Use SHA-256 for the deterministic identifier digest. |
| Dynamic formula evaluation | Medium, Bandit B307; Pylint W0123 | 38-41 | `eval` can execute arbitrary Python from the formula string. | Parse and evaluate only a small allowlisted arithmetic expression over `base_bill`. |
| Mutable default intake log | Bug, Pylint W0102 | 13 | The default list is shared between calls, so one admission can affect later calls. | Use `None` as the default and create/use a log only when one is supplied. |
| Bare exception hides failed discharges | Bug, Pylint W0702; Bandit B110 | 21-25 | A bare `except` silently suppresses unknown IDs and unrelated programming errors. | Look up the patient explicitly and return `False` when the ID is absent. |
| Weak random ward token | Low, Bandit B311 | 49 | The standard pseudo-random generator is predictable if the value is used as an access token. | Generate the token using `secrets`, designed for security-sensitive random values. |
| Flake8 formatting and unused code | Style, Flake8 | 4, 7-9, 16, 24, 29-30, 39, 72, 80 | Unused import/locals, long lines, bare exception, `== None`, and missing final newline were reported. | Remove unused code, apply Python style, and end the file with a newline. |

Baseline reports: [`reports/before/pylint_report.txt`](reports/before/pylint_report.txt), [`reports/before/bandit_report.txt`](reports/before/bandit_report.txt), and [`reports/before/flake8_report.txt`](reports/before/flake8_report.txt).
