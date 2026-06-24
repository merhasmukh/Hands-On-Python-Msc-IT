"""
hello_world.py — Your Very First Python Program
================================================
MSc (IT) — Unit 1: Getting Started with Python

Run this file:
    python hello_world.py
"""

# ---------------------------------------------------------------------------
# 1. The classic first program
# ---------------------------------------------------------------------------
print("Hello, World!")

# ---------------------------------------------------------------------------
# 2. Printing with variables
# ---------------------------------------------------------------------------
student_name = "Alice"
course = "MSc Information Technology"
year = 2024

print(f"Welcome, {student_name}!")
print(f"You are enrolled in: {course}, Year {year}")

# ---------------------------------------------------------------------------
# 3. Basic arithmetic in Python
# ---------------------------------------------------------------------------
print("\n--- Basic Arithmetic ---")
print("5 + 3 =", 5 + 3)      # Addition
print("10 - 4 =", 10 - 4)    # Subtraction
print("6 * 7 =", 6 * 7)      # Multiplication
print("15 / 4 =", 15 / 4)    # Division (float result)
print("15 // 4 =", 15 // 4)  # Floor division (integer result)
print("15 % 4 =", 15 % 4)    # Modulo (remainder)
print("2 ** 10 =", 2 ** 10)  # Exponentiation (power)

# ---------------------------------------------------------------------------
# 4. Getting user input
# ---------------------------------------------------------------------------
print("\n--- Interactive Input ---")
name = input("What is your name? ")
print(f"Nice to meet you, {name}! Welcome to Python 🐍")

# ---------------------------------------------------------------------------
# 5. Python version info
# ---------------------------------------------------------------------------
import sys

print(f"\nPython version: {sys.version}")
print(f"Python executable: {sys.executable}")
