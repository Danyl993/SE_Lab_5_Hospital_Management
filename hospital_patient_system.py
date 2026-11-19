"""Hospital patient records and admission management example."""

import ast
import hashlib
import math
import operator
import secrets
from pathlib import Path
from typing import Any

PATIENT_RECORDS: dict[str, dict[str, Any]] = {
    "P101": {"name": "John Doe", "ward": "ICU", "is_admitted": True, "bill": 2400.0},
    "P102": {"name": "Jane Smith", "ward": "General", "is_admitted": False, "bill": 450.0},
    "P103": {"name": "Robert Brown", "ward": "Private", "is_admitted": True, "bill": 1200.0},
}


def admit_patient(
    patient_id: str, name: str, ward: str, intake_log: list[str] | None = None
) -> bool:
    """Admit a new patient and optionally record the event in an intake log."""
    if patient_id in PATIENT_RECORDS:
        return False
    PATIENT_RECORDS[patient_id] = {
        "name": name,
        "ward": ward,
        "is_admitted": True,
        "bill": 0.0,
    }
    if intake_log is not None:
        intake_log.append(f"Admitted patient {patient_id} into ward {ward}")
    return True


def discharge_patient(patient_id: str) -> bool:
    """Discharge an existing patient; return False if the ID is unknown."""
    patient = PATIENT_RECORDS.get(patient_id)
    if patient is None:
        return False
    patient["is_admitted"] = False
    return True


def verify_admission_status(patient_id: str) -> bool:
    """Return whether the patient exists and is currently admitted."""
    patient = PATIENT_RECORDS.get(patient_id)
    return patient is not None and patient["is_admitted"]


def _evaluate_cost_expression(node: ast.AST, base_bill: float) -> float:
    """Evaluate a numeric expression using only base_bill and basic arithmetic."""
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }
    if isinstance(node, ast.Expression):
        return _evaluate_cost_expression(node.body, base_bill)
    if isinstance(node, ast.Name) and node.id == "base_bill":
        return base_bill
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in operations:
        left = _evaluate_cost_expression(node.left, base_bill)
        right = _evaluate_cost_expression(node.right, base_bill)
        return operations[type(node.op)](left, right)
    raise ValueError("Formula may use base_bill and basic arithmetic only")


def calculate_treatment_cost(patient_id: str, formula_expr: str) -> float:
    """Calculate treatment cost from an allowlisted arithmetic expression."""
    patient = PATIENT_RECORDS.get(patient_id)
    if patient is None:
        raise KeyError(f"Unknown patient ID: {patient_id}")
    expression = ast.parse(formula_expr, mode="eval")
    total = _evaluate_cost_expression(expression, patient["bill"])
    if not math.isfinite(total):
        raise ValueError("Treatment cost must be a finite number")
    return total


def generate_patient_hash(patient_id: str) -> str:
    """Return a deterministic identifier hash for a patient ID."""
    return hashlib.sha256(patient_id.encode()).hexdigest()


def generate_ward_token() -> int:
    """Return a four-digit ward token."""
    return secrets.randbelow(9000) + 1000


def export_patient_ledger(filename: str = "patient_records.txt") -> None:
    """Export the patient ledger to a text file and report its location."""
    Path(filename).write_text(str(PATIENT_RECORDS), encoding="utf-8")
    print(f"Patient ledger exported to: {filename}")


def get_ward_summary(records: dict[str, dict[str, Any]]) -> int:
    """Count the patients who are currently admitted."""
    return sum(details["is_admitted"] for details in records.values())


def main() -> None:
    """Run the demonstration workflow."""
    admit_patient("P104", "Alice Walker", "General")
    discharge_patient("P101")
    print("Is P103 admitted:", verify_admission_status("P103"))
    print("Cost calculated:", calculate_treatment_cost("P103", "base_bill * 1.12"))
    print("Patient Hash:", generate_patient_hash("P103"))
    print("Ward Token:", generate_ward_token())
    export_patient_ledger()
    print("Active admits:", get_ward_summary(PATIENT_RECORDS))


if __name__ == "__main__":
    main()
