"""
05_exercises.py — Modules, Packages, and Error Handling Exercises
=================================================================
MSc (IT) — Unit 1: Modules & Errors

Instructions:
- Complete each exercise by writing code in the space provided
- Run this file with: python 05_exercises.py
- Some exercises use mymodule.py (make sure it's in the same directory)
"""

print("=" * 60)
print("  Unit 1 — Modules & Error Handling Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: Importing and Using mymodule
# ===========================================================================
print("\n🏋️  Exercise 1: Using mymodule")
print("-" * 40)
"""
Import mymodule from the same folder and:
1. Call greet() with your name
2. Call factorial() for 0, 1, 5, 10
3. Convert 0°C, 37°C, 100°C to Fahrenheit
4. Count vowels in: "Python Programming is Powerful"
5. Create a Calculator, do all 4 operations, show history

Expected Output:
Hello, Alice! Welcome to Python.
factorial(5) = 120
37°C = 98.6°F
Vowels in 'Python Programming is Powerful': 9
"""

# Write your code below (import and use mymodule):


# ===========================================================================
# Exercise 2: Standard Library — os and sys
# ===========================================================================
print("\n🏋️  Exercise 2: Standard Library — os and sys")
print("-" * 40)
"""
Using the os and sys modules:
1. Print the current working directory
2. List all .py files in the current directory
3. Print the Python version
4. Print the platform (Windows/Linux/macOS)
5. Print the size of this script file in bytes

Expected Output:
CWD: /path/to/your/folder
Python files: ['05_exercises.py', 'mymodule.py']
Python: 3.11.x
Platform: darwin (or win32, linux)
This file size: XXXX bytes
"""

import os
import sys

# Write your code below:


# ===========================================================================
# Exercise 3: Standard Library — random and math
# ===========================================================================
print("\n🏋️  Exercise 3: random and math")
print("-" * 40)
"""
Using the random and math modules:
1. Generate 5 random integers between 1 and 100
2. Pick a random name from a list of 5 names
3. Shuffle a list [1..10] and print it
4. Compute: sqrt(144), ceil(4.3), floor(4.9), log(100, 10)
5. Find the hypotenuse of a right triangle with sides 3 and 4

Expected Output (varies due to random):
5 random numbers: [34, 72, 15, 88, 41]
Random name: Charlie
Shuffled: [7, 3, 10, 1, 5, 8, 2, 9, 4, 6]
sqrt(144) = 12.0
ceil(4.3) = 5
floor(4.9) = 4
log10(100) = 2.0
Hypotenuse: 5.0
"""

import random
import math

# Write your code below:


# ===========================================================================
# Exercise 4: Standard Library — datetime
# ===========================================================================
print("\n🏋️  Exercise 4: datetime")
print("-" * 40)
"""
Using the datetime module:
1. Print today's date in format: "24 June, 2024 (Tuesday)"
2. Print the current time (hours, minutes, seconds)
3. Calculate how many days until 1st January 2025
4. Calculate your age if you were born on a date you choose
5. Add 30 days to today's date and print it

Expected Output:
Today      : 24 June, 2024 (Tuesday)
Time now   : 15:30:45
Days to NY2025: 191
Your age   : 22 years old
30 days later: 24 July, 2024
"""

from datetime import datetime, date, timedelta

# Write your code below:


# ===========================================================================
# Exercise 5: Exception Handling — try/except/finally
# ===========================================================================
print("\n🏋️  Exercise 5: Exception Handling")
print("-" * 40)
"""
Write a function `safe_divide(a, b)` that:
- Returns a / b
- Handles ZeroDivisionError gracefully
- Handles TypeError if non-numbers are passed
- Always prints "Operation complete." in finally

Write a function `safe_list_access(lst, index)` that:
- Returns lst[index]
- Handles IndexError gracefully

Expected Output:
safe_divide(10, 2)    → 5.0
safe_divide(10, 0)    → Error: Cannot divide by zero!
safe_divide(10, "a")  → Error: Invalid types!

safe_list_access([1,2,3], 1)  → 2
safe_list_access([1,2,3], 10) → Error: Index out of range!
"""

# Write your functions here:


# ===========================================================================
# Exercise 6: Raising Custom Exceptions
# ===========================================================================
print("\n🏋️  Exercise 6: Custom Exceptions")
print("-" * 40)
"""
Create custom exception classes:
    class NegativeAgeError(ValueError): ...
    class InvalidScoreError(ValueError): ...

Write functions:
    validate_age(age)   → raise NegativeAgeError if age < 0
                          raise TypeError if not int
    validate_score(score) → raise InvalidScoreError if score < 0 or > 100

Expected Output:
validate_age(22)    → Valid age: 22
validate_age(-5)    → NegativeAgeError: Age cannot be negative. Got: -5
validate_age("abc") → TypeError: Age must be an integer. Got: str

validate_score(85)  → Valid score: 85
validate_score(110) → InvalidScoreError: Score must be 0-100. Got: 110
"""

# Write your custom exceptions and functions here:


# ===========================================================================
# Exercise 7: Type Hints
# ===========================================================================
print("\n🏋️  Exercise 7: Type Hints")
print("-" * 40)
"""
Rewrite the following functions with FULL type hints:
(Use Python 3.10+ union syntax: int | None instead of Optional[int])

1. find_max(numbers: list[int]) -> int
   Returns the maximum in the list.

2. merge_dicts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]
   Returns a new dict merging a and b. If key conflicts, b wins.

3. parse_csv_line(line: str, sep: str = ",") -> list[str]
   Splits a CSV line by sep and strips whitespace from each field.

4. search(items: list[str], target: str) -> int | None
   Returns the index of target in items, or None if not found.

Run each function with test data and print results.
"""

# Write your type-annotated functions here:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
