"""Provide utilities for calculating student performance statistics."""

from typing import TypedDict


class Student(TypedDict):
    """Represent a student record."""

    name: str
    marks: int


def calculate_average(students: list[Student]) -> float:
    """Return the average marks of all students.

    Args:
        students: A list of student records containing marks.

    Returns:
        The average marks as a float, or 0.0 if the list is empty.
    """
    if not students:
        return 0.0

    total = sum(student["marks"] for student in students)
    return total / len(students)


def calculate_pass_rate(
    students: list[Student],
    passing: int = 40,
) -> float:
    """Return the percentage of students who passed.

    Args:
        students: A list of student records containing marks.
        passing: The minimum mark required to pass.

    Returns:
        The pass rate as a percentage, or 0.0 if the list is empty.
    """
    if not students:
        return 0.0

    passed = sum(student["marks"] >= passing for student in students)

    return passed / len(students) * 100


def highest_mark(students: list[Student]) -> int | None:
    """Return the highest mark among the students.

    Args:
        students: A list of student records containing marks.

    Returns:
        The highest mark, or None if the list is empty.
    """
    if not students:
        return None

    return max(student["marks"] for student in students)


def lowest_mark(students: list[Student]) -> int | None:
    """Return the lowest mark among the students.

    Args:
        students: A list of student records containing marks.

    Returns:
        The lowest mark, or None if the list is empty.
    """
    if not students:
        return None

    return min(student["marks"] for student in students)


def class_average(
    students: list[Student],
    passing: int = 40,
) -> tuple[float, float]:
    """Return the class average and pass rate.

    Args:
        students: A list of student records containing marks.
        passing: The minimum mark required to pass.

    Returns:
        A tuple containing the average marks and pass rate.
        Both values are 0.0 if the list is empty.
    """
    return (
        calculate_average(students),
        calculate_pass_rate(students, passing),
    )
