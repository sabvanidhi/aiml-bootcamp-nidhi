import csv


def load_records(path: str) -> list:
    """Load records from CSV file."""
    with open(path, "r") as file:
        records = list(csv.DictReader(file))

    return records


def is_valid_email(email: str) -> bool:
    """Check if email is valid."""
    if "@" in email and "." in email:
        return True

    return False


def parse_marks(marks: str):
    """Convert marks into a number."""
    if marks == "":
        return None

    return float(marks)


def calculate_average(records: list) -> float:
    """Calculate average marks."""
    total = 0
    count = 0

    for record in records:
        marks = record.get("marks")

        if marks is not None:
            total = total + marks
            count = count + 1

    if count == 0:
        return 0.0

    return total / count
