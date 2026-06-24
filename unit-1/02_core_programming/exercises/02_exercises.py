"""
02_exercises.py — Core Programming Exercises
============================================
MSc (IT) — Unit 1: Core Programming

Instructions:
- Complete each exercise by writing code in the space provided
- Do NOT look at solutions — try yourself first!
- Run this file with: python 02_exercises.py
- Each exercise has a description and expected output shown in comments
"""

print("=" * 60)
print("  Unit 1 — Core Programming Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: Variable Exploration
# ===========================================================================
print("\n🏋️  Exercise 1: Variable Exploration")
print("-" * 40)
"""
Create variables of each type:
- An integer for your roll number
- A float for your GPA (e.g., 8.75)
- A string for your full name
- A boolean indicating if you are a full-time student

Then print each variable along with its type using type().

Expected Output (example):
Roll Number : 101  (type: <class 'int'>)
GPA         : 8.75 (type: <class 'float'>)
Name        : Alice Kumar (type: <class 'str'>)
Full-time   : True (type: <class 'bool'>)
"""

# Write your code below:


# ===========================================================================
# Exercise 2: Type Casting
# ===========================================================================
print("\n🏋️  Exercise 2: Type Casting")
print("-" * 40)
"""
Given the following string values, convert them to the appropriate types
and perform the described operation.

Expected Output:
Sum of 15 and 27 as integers: 42
Product of 3.5 and 2.0 as floats: 7.0
Is '1' truthy? True
Concatenated as strings: '1527'
"""

num1_str = "15"
num2_str = "27"

# Write your code below:


# ===========================================================================
# Exercise 3: F-Strings Formatting
# ===========================================================================
print("\n🏋️  Exercise 3: F-Strings Formatting")
print("-" * 40)
"""
You have:
    item = "Python Textbook"
    price = 450.5
    quantity = 3

Print an invoice line like:
    Item     : Python Textbook
    Quantity : 3
    Price    : ₹450.50 each
    Total    : ₹1351.50
    Discount : 10%
    Final    : ₹1216.35

Hint: Use f-string formatting:
    f"{price:.2f}"   → 2 decimal places
    f"{name:<20}"    → left-align in 20 chars
"""

item = "Python Textbook"
price = 450.5
quantity = 3
discount = 0.10

# Write your code below:


# ===========================================================================
# Exercise 4: Operators
# ===========================================================================
print("\n🏋️  Exercise 4: Operators")
print("-" * 40)
"""
Given: a = 17, b = 5

Compute and print ALL of the following:
1. a + b, a - b, a * b
2. a / b  (float division)
3. a // b (floor division)
4. a % b  (modulo / remainder)
5. a ** b (exponentiation)
6. Is a greater than b?
7. Is a equal to b?
8. Is a divisible by 2? (use %)
9. a AND b (bitwise &)
10. a OR b  (bitwise |)
"""

a = 17
b = 5

# Write your code below:


# ===========================================================================
# Exercise 5: Decision Making — Grade Calculator
# ===========================================================================
print("\n🏋️  Exercise 5: Grade Calculator")
print("-" * 40)
"""
Ask the user for a score (0–100) and print the grade.
Use if-elif-else:
    90-100  → Grade: A+  (Outstanding)
    80-89   → Grade: A   (Excellent)
    70-79   → Grade: B+  (Very Good)
    60-69   → Grade: B   (Good)
    50-59   → Grade: C   (Average)
    Below 50 → Grade: F  (Fail)

Also print if the student passed or failed.

Bonus: Handle invalid input (score < 0 or score > 100).

Expected Output (for score 85):
Score : 85
Grade : A (Excellent)
Result: PASS
"""

# Write your code below:


# ===========================================================================
# Exercise 6: Multiplication Table
# ===========================================================================
print("\n🏋️  Exercise 6: Multiplication Table")
print("-" * 40)
"""
Ask the user for a number and print its multiplication table from 1 to 10.

Expected Output (for n = 7):
Multiplication Table for 7
--------------------------
7 x  1 =  7
7 x  2 = 14
...
7 x 10 = 70
"""

# Write your code below:


# ===========================================================================
# Exercise 7: FizzBuzz
# ===========================================================================
print("\n🏋️  Exercise 7: FizzBuzz")
print("-" * 40)
"""
Print numbers from 1 to 50.
- If divisible by both 3 and 5 → print "FizzBuzz"
- If divisible by 3 only        → print "Fizz"
- If divisible by 5 only        → print "Buzz"
- Otherwise                     → print the number

Expected Output (first few):
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
"""

# Write your code below:


# ===========================================================================
# Exercise 8: Sum of Digits
# ===========================================================================
print("\n🏋️  Exercise 8: Sum of Digits")
print("-" * 40)
"""
Write a program that reads a positive integer from the user
and computes the sum of its digits using a while loop.

Expected Output (for 12345):
Number : 12345
Digit sum: 15
"""

# Write your code below:


# ===========================================================================
# Exercise 9: enumerate() and zip()
# ===========================================================================
print("\n🏋️  Exercise 9: enumerate() and zip()")
print("-" * 40)
"""
You have two lists:
    students = ["Alice", "Bob", "Charlie", "Diana"]
    marks = [88, 75, 92, 65]

Part A: Use enumerate() to print:
    1. Alice  — 88
    2. Bob    — 75
    3. Charlie — 92
    4. Diana  — 65

Part B: Use zip() to find and print students who scored above 80.
"""

students = ["Alice", "Bob", "Charlie", "Diana"]
marks = [88, 75, 92, 65]

# Part A:

# Part B:


# ===========================================================================
# Exercise 10: Pattern with Nested Loops
# ===========================================================================
print("\n🏋️  Exercise 10: Pattern with Nested Loops")
print("-" * 40)
"""
Print the following pattern using nested loops:

*
* *
* * *
* * * *
* * * * *
* * * * * *
(triangle with 6 rows)

Bonus: Print the inverted triangle below it.
"""

# Write your code below:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
