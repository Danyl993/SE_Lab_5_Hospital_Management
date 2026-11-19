# Reflection

The handout asks for four reflection answers but does not include the question text on any of its three pages. The repository README also refers to four questions without listing them. The answers below address the lab's stated learning outcomes and static-analysis work; replace the prompts if your instructor provides the original questions separately.

## 1. What is static code analysis, and how is it different from running a program?

Static analysis inspects source code without executing it. Pylint checks code quality and likely mistakes, Flake8 checks style and common Python errors, and Bandit scans for risky coding patterns. Running the application still matters because static tools cannot prove that the program behaves as intended for every input.

## 2. Which issues did the tools help identify, and which required manual review?

The tools reported the shared mutable default list, a bare exception, `eval`, MD5, predictable random values, shell execution, unused code, and formatting problems. Manual review also caught that the original program printed a hard-coded nurse access key and silently ignored failed discharges. Tool output was useful evidence, but I still had to judge the impact and choose a safe replacement.

## 3. How did the fixes improve security and maintainability?

The formula evaluator now accepts only numeric literals, `base_bill`, and basic arithmetic operators, so formula text cannot run arbitrary Python. The ledger export no longer invokes a shell, patient IDs use SHA-256, and ward tokens use `secrets`. Explicit missing-patient handling and non-shared defaults make behavior easier to reason about. The final Pylint score is 10.00/10, Bandit reports no findings, and Flake8 reports no formatting issues.

## 4. What are the limitations of static analysis, and how would you use it in future work?

Static analysis can miss runtime and business-logic defects, and it can report issues that need context. The original wrong behavior was not fully described by the tool findings, so I ran the program and reviewed its output as well. I would run these tools repeatedly during development and pair them with functional tests, code review, and realistic data checks.
