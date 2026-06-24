"""
07_exercises.py — OOP Exercises
================================
MSc (IT) — Unit 1: Object-Oriented Programming

Instructions:
- Complete each exercise by writing code in the space provided
- Do NOT look at solutions — try yourself first!
- Run this file with: python 07_exercises.py
"""

print("=" * 60)
print("  Unit 1 — OOP Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: Your First Class — Student
# ===========================================================================
print("\n🏋️  Exercise 1: Student Class")
print("-" * 40)
"""
Create a class `Student` with:
    Attributes: name, roll_no, department, gpa (all set via __init__)
    Methods:
        - display()    : prints all details neatly
        - is_distinction(): returns True if gpa >= 8.0
        - update_gpa(new_gpa): updates gpa if 0 <= new_gpa <= 10
        - __str__(): returns "Student[name] | Roll: roll_no | GPA: gpa"
        - __repr__(): returns "Student('name', roll_no, 'dept', gpa)"

Expected Output:
Name       : Alice
Roll No    : 101
Department : MSc IT
GPA        : 8.75

Is distinction? True
Updated GPA: 9.0
str:  Student[Alice] | Roll: 101 | GPA: 9.0
repr: Student('Alice', 101, 'MSc IT', 9.0)
"""

# Write your Student class here:


# Test:
# s = Student("Alice", 101, "MSc IT", 8.75)


# ===========================================================================
# Exercise 2: Class Attributes and Methods
# ===========================================================================
print("\n🏋️  Exercise 2: Class Attributes and @classmethod")
print("-" * 40)
"""
Add to the Student class (or create a new version):
    - Class attribute: student_count = 0 (increments every time a Student is created)
    - @classmethod `get_count()`: returns the current count
    - @staticmethod `is_valid_gpa(gpa)`: returns True if 0.0 <= gpa <= 10.0

Expected Output:
Count: 0
Created Alice, Bob, Charlie
Count: 3
is_valid_gpa(8.5): True
is_valid_gpa(11.0): False
"""

# Write your enhanced Student class here:


# ===========================================================================
# Exercise 3: Encapsulation with Properties
# ===========================================================================
print("\n🏋️  Exercise 3: Encapsulation")
print("-" * 40)
"""
Create a class `BankAccount` with:
    - Private attribute __balance (set via __init__)
    - @property balance: returns __balance (read-only access)
    - deposit(amount): adds to balance if amount > 0
    - withdraw(amount): deducts if amount > 0 and sufficient balance,
                        otherwise raise ValueError
    - __str__(): "Account[owner]: ₹balance"

Expected Output:
Account[Alice]: ₹5000
After deposit 2000: ₹7000
After withdraw 3000: ₹4000
Error: Insufficient balance (tried to withdraw 9000)
Balance: ₹4000  (direct access via property)
"""

# Write your BankAccount class here:


# ===========================================================================
# Exercise 4: Inheritance — SavingsAccount
# ===========================================================================
print("\n🏋️  Exercise 4: Inheritance")
print("-" * 40)
"""
Create `SavingsAccount` that inherits from `BankAccount` with:
    - Extra attribute: interest_rate (default 4.5%)
    - Method add_interest(): adds interest to balance (balance * rate / 100)
    - Override __str__() to show rate too

Create `LoanAccount` that inherits from `BankAccount` with:
    - Extra attribute: loan_amount
    - Method pay_emi(emi): deducts emi from balance,
                           reduces loan_amount, raises error if balance insufficient

Demonstrate with test cases.

Expected Output:
SavingsAccount[Alice]: ₹10000 @ 4.5% interest
After interest: ₹10450.0
LoanAccount[Bob]: ₹5000 (Loan: ₹50000)
After EMI 2000: Balance=₹3000, Loan remaining=₹48000
"""

# Write your SavingsAccount and LoanAccount classes here:


# ===========================================================================
# Exercise 5: Polymorphism
# ===========================================================================
print("\n🏋️  Exercise 5: Polymorphism")
print("-" * 40)
"""
Create an Animal hierarchy:
    class Animal:
        - name (str)
        - sound() method → returns "..."
        - __str__() → "Animal: name"

    class Dog(Animal):   sound() → "Woof!"
    class Cat(Animal):   sound() → "Meow!"
    class Duck(Animal):  sound() → "Quack!"
    class Cow(Animal):   sound() → "Moo!"

Write a function `make_noise(animals)` that takes a list of Animal objects
and calls sound() on each. (This is polymorphism!)

Expected Output:
Dog (Rex) says: Woof!
Cat (Whiskers) says: Meow!
Duck (Donald) says: Quack!
Cow (Bessie) says: Moo!
"""

# Write your Animal hierarchy here:


# ===========================================================================
# Exercise 6: Dunder Methods — Vector
# ===========================================================================
print("\n🏋️  Exercise 6: Dunder Methods — Vector Class")
print("-" * 40)
"""
Create a `Vector` class representing a 2D vector (x, y).

Implement:
    - __init__(x, y)
    - __str__(): "Vector(x, y)"
    - __repr__(): "Vector(x=x, y=y)"
    - __add__(other): vector addition
    - __sub__(other): vector subtraction
    - __mul__(scalar): scalar multiplication (v * 3)
    - __len__(): returns 2 (dimension)
    - __eq__(other): True if same x and y
    - magnitude(): returns sqrt(x² + y²)

Expected Output:
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v1 + v2 = Vector(4, 6)
v1 - v2 = Vector(2, 2)
v1 * 3  = Vector(9, 12)
len(v1) = 2
v1 == v2 = False
|v1|    = 5.0
"""

# Write your Vector class here:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
