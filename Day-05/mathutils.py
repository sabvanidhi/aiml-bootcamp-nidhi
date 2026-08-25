"""Provide basic mathematical utility functions."""


def average(nums: list[int]) -> float:
    """Return the average of a list of numbers.

    Args:
        nums: A list of numbers. May be empty.



    Returns:
        The average as a float, or 0.0 if the list is empty.
    """

    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> int | None:
    """Return the biggest number in a list.

    Args:
        nums: A list of numbers. May be empty.

    Returns:
        The biggest number, or None if the list is empty.
    """
    if not nums:
        return None
    return max(nums)


def is_prime(n: int) -> bool:
    """Return whether a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, otherwise False.
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
