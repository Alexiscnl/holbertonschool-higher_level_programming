#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number (default is 98).

    Returns:
        a + b

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b
