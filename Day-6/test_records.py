import csv

from records import calculate_average, is_valid_email, load_records, parse_marks


def test_empty_file(tmp_path):
    """Test an empty CSV file."""
    file_path = tmp_path / "empty.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "email", "marks"])

    records = load_records(str(file_path))

    assert records == []


def test_missing_marks(tmp_path):
    """Test a row with missing marks."""
    file_path = tmp_path / "students.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "email", "marks"])
        writer.writerow(["Nidhi", "nidhi@gmail.com", ""])

    records = load_records(str(file_path))

    assert parse_marks(records[0]["marks"]) is None


def test_malformed_email():
    """Test an invalid email address."""
    assert is_valid_email("wrong-email") is False


def test_valid_email():
    """Test a valid email address."""
    assert is_valid_email("nidhi@gmail.com") is True


def test_invalid_marks():
    """Test invalid marks."""
    assert parse_marks("abc") is None


def test_average():
    """Test average marks calculation."""
    records = [
        {"marks": 80},
        {"marks": 60},
    ]

    assert calculate_average(records) == 70.0


def test_empty_average():
    """Test average when there are no records."""
    assert calculate_average([]) == 0.0
