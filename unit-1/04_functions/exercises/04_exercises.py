"""
04_exercises.py — Functions and Functional Tools Exercises
==========================================================
MSc (IT) — Unit 1: Functions

Instructions:
- Complete each exercise by writing code in the space provided
- Do NOT look at solutions — try yourself first!
- Run this file with: python 04_exercises.py
"""

print("=" * 60)
print("  Unit 1 — Functions and Functional Tools Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: Basic Functions
# ===========================================================================
print("\n🏋️  Exercise 1: Basic Functions")
print("-" * 40)
"""
Write a function `circle_info(radius)` that returns a tuple of
(circumference, area) rounded to 2 decimal places.

Then write a function `bmi(weight_kg, height_m)` that returns:
    - the BMI value (rounded to 1 decimal place)
    - a category: "Underweight", "Normal", "Overweight", or "Obese"

Use pi = 3.14159265

Expected Output:
Circle (radius=7): circumference=43.98, area=153.94

BMI for 70kg, 1.75m: 22.9 → Normal
BMI for 50kg, 1.75m: 16.3 → Underweight
"""

# Write circle_info() here:


# Write bmi() here:


# Test your functions:


# ===========================================================================
# Exercise 2: Default Parameters and Keyword Arguments
# ===========================================================================
print("\n🏋️  Exercise 2: Default Parameters")
print("-" * 40)
"""
Write a function `make_email(username, domain="university.edu", tld="in")` 
that constructs an email address.

Expected Output:
alice@university.edu.in
bob@gmail.com
charlie@company.org
"""

# Write your function here:


# Test:
# make_email("alice")                          → alice@university.edu.in
# make_email("bob", "gmail", "com")            → bob@gmail.com
# make_email("charlie", domain="company", tld="org")


# ===========================================================================
# Exercise 3: *args and **kwargs
# ===========================================================================
print("\n🏋️  Exercise 3: *args and **kwargs")
print("-" * 40)
"""
Part A: Write a function `total(*args)` that returns the sum of any
        number of numeric arguments.

Part B: Write a function `profile(**kwargs)` that prints each key-value
        pair in the format "key: value".

Expected Output:
total(1, 2, 3)         → 6
total(10, 20, 30, 40)  → 100

profile(name="Alice", age=22, city="Mumbai"):
  name : Alice
  age  : 22
  city : Mumbai
"""

# Write your functions here:


# ===========================================================================
# Exercise 4: Variable Scope (LEGB Rule)
# ===========================================================================
print("\n🏋️  Exercise 4: Variable Scope")
print("-" * 40)
"""
Predict the output of the following code BEFORE running it.
Write your prediction as a comment, then run to verify.

Questions:
1. What does outer() print?
2. What does change_global() do to COUNTER?
3. What does inner() print inside nested()?
"""

COUNTER = 100  # Global

def outer():
    x = "outer"
    def inner():
        x = "inner"  # What does this affect?
        print("inner x:", x)
    inner()
    print("outer x:", x)

def change_global():
    global COUNTER
    COUNTER += 1

def nested():
    val = "enclosing"
    def inside():
        nonlocal val
        val = "modified by inside"
    inside()
    print("val after inside():", val)


# Write your predictions as comments, then run:
# outer() → ?
# print(COUNTER) → ?
# change_global(); print(COUNTER) → ?
# nested() → ?

outer()
print("COUNTER before:", COUNTER)
change_global()
print("COUNTER after:", COUNTER)
nested()


# ===========================================================================
# Exercise 5: Recursion
# ===========================================================================
print("\n🏋️  Exercise 5: Recursion")
print("-" * 40)
"""
Write the following recursive functions:

1. power(base, exp): computes base^exp WITHOUT using ** operator
2. sum_list(lst): returns sum of all elements in a list recursively
3. count_down(n): prints n, n-1, ..., 1, "Blastoff!" recursively

Expected Output:
power(2, 10) = 1024
power(3, 4) = 81
sum_list([1, 2, 3, 4, 5]) = 15
3
2
1
Blastoff!
"""

# Write your functions here:


# ===========================================================================
# Exercise 6: Lambda, map(), filter()
# ===========================================================================
print("\n🏋️  Exercise 6: Lambda, map(), filter()")
print("-" * 40)
"""
Given:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    names   = ["alice", "bob", "charlie", "diana", "eve"]
    prices  = [100.50, 75.00, 200.99, 50.25, 150.00]

1. Use map() to create a list of squares
2. Use filter() to keep only even numbers
3. Use map() to title-case all names
4. Use filter() to keep prices above 100
5. Use sorted() with a lambda key to sort names by length
6. Write a lambda that takes two numbers and returns the larger one

Expected Output:
Squares    : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens      : [2, 4, 6, 8, 10]
Title names: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
Exp prices : [100.5, 200.99, 150.0]
By length  : ['bob', 'eve', 'alice', 'diana', 'charlie']
max(5,9)   : 9
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names   = ["alice", "bob", "charlie", "diana", "eve"]
prices  = [100.50, 75.00, 200.99, 50.25, 150.00]

# Write your code below:


# ===========================================================================
# Exercise 7: Decorator
# ===========================================================================
print("\n🏋️  Exercise 7: Decorator")
print("-" * 40)
"""
Write a decorator `@log_call` that:
- Prints the function name and arguments BEFORE calling it
- Prints the return value AFTER calling it

Apply it to a function `add(a, b)`.

Expected Output:
Calling: add with args=(3, 5), kwargs={}
Result: 8
---
Calling: add with args=(100, 200), kwargs={}
Result: 300

Bonus: Write a `@timer` decorator that measures and prints
       the execution time of a function.
"""

# Write your decorator and function here:


# ===========================================================================
# Exercise 8: Generator
# ===========================================================================
print("\n🏋️  Exercise 8: Generator")
print("-" * 40)
"""
Write a generator function `fibonacci_gen(n)` that yields the first
n Fibonacci numbers.

Write another generator `even_numbers(limit)` that yields even
numbers up to the limit (without creating a list first).

Expected Output:
First 10 Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Even up to 20: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Memory efficient? Use: import sys; sys.getsizeof()
Compare list vs generator size.
"""

# Write your generators here:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
