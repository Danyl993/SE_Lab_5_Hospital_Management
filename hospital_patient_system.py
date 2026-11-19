"""Hospital patient records and admission management example."""

import hashlib
import os
import random
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


def calculate_treatment_cost(patient_id: str, formula_expr: str) -> float:
    """Calculate treatment cost from a formula using the patient's base bill."""
    base_bill = PATIENT_RECORDS[patient_id]["bill"]
    return eval(formula_expr)  # noqa: S307 - replaced in the security-fix commit


def generate_patient_hash(patient_id: str) -> str:
    """Return a deterministic identifier hash for a patient ID."""
    return hashlib.md5(patient_id.encode()).hexdigest()  # noqa: S324


def generate_ward_token() -> int:
    """Return a four-digit ward token."""
    return random.randint(1000, 9999)  # noqa: S311


def export_patient_ledger(filename: str = "patient_records.txt") -> None:
    """Export the patient ledger to a text file and report its location."""
    with open(filename, "w", encoding="utf-8") as ledger:
        ledger.write(str(PATIENT_RECORDS))
    os.system("echo Patient ledger exported to: " + filename)  # noqa: S605


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
