from log_utils import (
    calculate_average,
    calculate_pass_rate,
    class_average,
    highest_mark,
    lowest_mark,
)

students = [
    {"name": "asha", "marks": 88},
    {"name": "ravi", "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev", "marks": 40},
]


def test_calculate_average():
    assert calculate_average(students) == 74.75


def test_calculate_average_empty():
    assert calculate_average([]) == 0.0


def test_calculate_pass_rate():
    assert calculate_pass_rate(students) == 100.0


def test_calculate_pass_rate_empty():
    assert calculate_pass_rate([]) == 0.0


def test_highest_mark():
    assert highest_mark(students) == 92


def test_highest_mark_empty():
    assert highest_mark([]) is None


def test_lowest_mark():
    assert lowest_mark(students) == 40


def test_lowest_mark_empty():
    assert lowest_mark([]) is None


def test_class_average():
    assert class_average(students) == (74.75, 100.0)


def test_class_average_empty():
    assert class_average([]) == (0.0, 0.0)
