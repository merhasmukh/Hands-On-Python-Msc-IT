"""
mymodule.py
-----------
A simple custom Python module used in the
'Modules, Packages, and Error Handling' notebook.

MSc IT – Hands-On Python
"""

# ── Module-level constant ──────────────────────────────────────────────────
MODULE_VERSION = "1.0.0"
AUTHOR = "MSc IT Python Course"


# ── Utility functions ──────────────────────────────────────────────────────

def greet(name: str) -> str:
    """Return a personalised greeting string."""
    return f"Hello, {name}! Welcome to Python modules."


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def factorial(n: int) -> int:
    """Return n! recursively.  Raises ValueError for negative input."""
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_palindrome(text: str) -> bool:
    """Return True if *text* reads the same forwards and backwards."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


# ── Simple class ───────────────────────────────────────────────────────────

class Circle:
    """Represent a circle and expose area / perimeter helpers."""

    import math as _math          # private import inside class scope

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return self._math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Return the circumference of the circle."""
        return 2 * self._math.pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


# ── Guard: only runs when this file is executed directly ───────────────────
if __name__ == "__main__":
    print("Running mymodule.py directly (not imported).")
    print(greet("Developer"))
    print(f"5! = {factorial(5)}")
    c = Circle(7)
    print(f"Circle area: {c.area():.2f}")
