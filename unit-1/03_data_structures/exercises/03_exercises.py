"""
03_exercises.py — Data Structures Exercises
===========================================
MSc (IT) — Unit 1: Built-in Data Structures

Instructions:
- Complete each exercise by writing code in the space provided
- Do NOT look at solutions — try yourself first!
- Run this file with: python 03_exercises.py
"""

print("=" * 60)
print("  Unit 1 — Data Structures Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: String Manipulation
# ===========================================================================
print("\n🏋️  Exercise 1: String Manipulation")
print("-" * 40)
"""
Given: sentence = "  Python is Amazing and Fun!  "

1. Remove leading/trailing spaces
2. Convert to UPPERCASE
3. Count how many times 'a' or 'A' appears
4. Replace 'Amazing' with 'Powerful'
5. Split into individual words
6. Check if it starts with 'Python' (after stripping)
7. Print the last 5 characters (slicing)

Expected Output:
Stripped   : 'Python is Amazing and Fun!'
Uppercase  : 'PYTHON IS AMAZING AND FUN!'
Count of A : 3
Replaced   : 'Python is Powerful and Fun!'
Words      : ['Python', 'is', 'Amazing', 'and', 'Fun!']
Starts with 'Python': True
Last 5 chars: 'Fun!'
"""

sentence = "  Python is Amazing and Fun!  "

# Write your code below:


# ===========================================================================
# Exercise 2: List Operations
# ===========================================================================
print("\n🏋️  Exercise 2: List Operations")
print("-" * 40)
"""
Create a list of 8 integers (any values you like).

Perform and print results for:
1. The first and last elements (indexing)
2. Sum, minimum, and maximum of the list
3. Sort the list in ascending order
4. Reverse the sorted list
5. Append the value 100 and insert 0 at position 0
6. Remove duplicates (convert to set, then back to sorted list)

Expected Output (example with [5,3,8,1,5,9,2,3]):
First: 5, Last: 3
Sum: 36, Min: 1, Max: 9
Sorted: [1, 2, 3, 3, 5, 5, 8, 9]
Reversed: [9, 8, 5, 5, 3, 3, 2, 1]
After append/insert: [0, 9, 8, 5, 5, 3, 3, 2, 1, 100]
Unique sorted: [1, 2, 3, 5, 8, 9, 100]
"""

numbers = [5, 3, 8, 1, 5, 9, 2, 3]

# Write your code below:


# ===========================================================================
# Exercise 3: Tuple Unpacking
# ===========================================================================
print("\n🏋️  Exercise 3: Tuple Unpacking")
print("-" * 40)
"""
Given: student = ("Alice", 22, "Mumbai", 88.5, True)

1. Unpack into variables: name, age, city, score, is_active
2. Print each variable with its meaning
3. Try to change a tuple element — observe the error (comment it out after)
4. Convert the tuple to a list, change the score to 90, convert back to tuple
5. Use slicing to get only (name, age, city)

Expected Output:
Name  : Alice
Age   : 22
City  : Mumbai
Score : 88.5
Active: True
Modified score tuple: ('Alice', 22, 'Mumbai', 90, True)
"""

student = ("Alice", 22, "Mumbai", 88.5, True)

# Write your code below:


# ===========================================================================
# Exercise 4: Set Operations
# ===========================================================================
print("\n🏋️  Exercise 4: Set Operations")
print("-" * 40)
"""
You have two sections of students:
    section_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
    section_b = {"Charlie", "Eve", "Frank", "Grace", "Bob"}

Find and print:
1. All unique students across both sections (union)
2. Students in BOTH sections (intersection)
3. Students ONLY in section_a (difference)
4. Students in either but NOT both (symmetric difference)
5. Is "Alice" in section_b? (membership test)
6. Total unique student count

Expected Output:
Union        : {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'}
Intersection : {'Bob', 'Charlie', 'Eve'}
Only in A    : {'Alice', 'Diana'}
Symmetric Diff: {'Alice', 'Diana', 'Frank', 'Grace'}
Alice in B?  : False
Total unique : 7
"""

section_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
section_b = {"Charlie", "Eve", "Frank", "Grace", "Bob"}

# Write your code below:


# ===========================================================================
# Exercise 5: Dictionary — Student Record
# ===========================================================================
print("\n🏋️  Exercise 5: Dictionary — Student Record")
print("-" * 40)
"""
Create a student record dictionary with:
    name, roll_no, department, semester, subjects (list), gpa

1. Print each key-value pair using .items()
2. Add a new key: 'email'
3. Update the GPA to 9.0
4. Delete the 'roll_no' key
5. Check if 'department' key exists
6. Use .get() with a default for a missing key 'phone'

Expected Output (example):
name       : Alice Kumar
roll_no    : 101
department : MSc IT
...
After update GPA: 9.0
'roll_no' deleted
'department' exists: True
Phone (default): Not Provided
"""

student = {
    "name": "Alice Kumar",
    "roll_no": 101,
    "department": "MSc IT",
    "semester": 1,
    "subjects": ["Python", "DBMS", "Networks"],
    "gpa": 8.75
}

# Write your code below:


# ===========================================================================
# Exercise 6: List Comprehension
# ===========================================================================
print("\n🏋️  Exercise 6: List Comprehension")
print("-" * 40)
"""
Using list comprehensions, create:

1. A list of squares of numbers 1 to 10
2. A list of even numbers from 1 to 30
3. A list of words from the sentence that have more than 4 characters
4. A list of (number, square) tuples for 1 to 5
5. Flatten this list of lists: [[1,2,3],[4,5],[6,7,8,9]]

sentence = "The quick brown fox jumps over the lazy dog"

Expected Output:
Squares    : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens      : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
Long words : ['quick', 'brown', 'jumps', 'over', 'lazy']
Tuples     : [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
Flattened  : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

sentence = "The quick brown fox jumps over the lazy dog"
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Write your code below:


# ===========================================================================
# Exercise 7: Dictionary Comprehension
# ===========================================================================
print("\n🏋️  Exercise 7: Dictionary Comprehension")
print("-" * 40)
"""
Given:
    names  = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [88, 75, 92, 65]

1. Create a dict mapping name → score using zip + dict comprehension
2. Create a dict mapping name → grade (A if >=80, B if >=70, C if >=60, F otherwise)
3. Create a dict of name → score, but only for students who passed (score >= 60)
4. Create a dict of name → name_length

Expected Output:
Scores    : {'Alice': 88, 'Bob': 75, 'Charlie': 92, 'Diana': 65}
Grades    : {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A', 'Diana': 'C'}
Passed    : {'Alice': 88, 'Bob': 75, 'Charlie': 92, 'Diana': 65}
Name lens : {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'Diana': 5}
"""

names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [88, 75, 92, 65]

# Write your code below:


# ===========================================================================
# Exercise 8: Word Frequency Counter
# ===========================================================================
print("\n🏋️  Exercise 8: Word Frequency Counter")
print("-" * 40)
"""
Given a paragraph of text, count the frequency of each word.
(Ignore case, ignore punctuation like . , ! ?)

text = "the cat sat on the mat the cat is fat"

Expected Output:
Word Frequency:
  the    : 3
  cat    : 2
  sat    : 1
  on     : 1
  mat    : 1
  is     : 1
  fat    : 1

Most common word: 'the' (3 times)
"""

text = "the cat sat on the mat the cat is fat"

# Write your code below:


# ===========================================================================
# Exercise 9: Nested Data Structure
# ===========================================================================
print("\n🏋️  Exercise 9: Nested Data Structure")
print("-" * 40)
"""
You have a list of student dictionaries:

students = [
    {"name": "Alice",   "scores": [85, 90, 78]},
    {"name": "Bob",     "scores": [70, 65, 80]},
    {"name": "Charlie", "scores": [92, 95, 88]},
]

1. Print each student's name and their average score
2. Find the student with the highest average
3. Add a new student: {"name": "Diana", "scores": [75, 80, 70]}
4. Sort students by average score (descending)

Expected Output:
Alice   — Average: 84.33
Bob     — Average: 71.67
Charlie — Average: 91.67
Top Student: Charlie (91.67)
"""

students = [
    {"name": "Alice",   "scores": [85, 90, 78]},
    {"name": "Bob",     "scores": [70, 65, 80]},
    {"name": "Charlie", "scores": [92, 95, 88]},
]

# Write your code below:


# ===========================================================================
# Exercise 10: String Slicing Puzzle
# ===========================================================================
print("\n🏋️  Exercise 10: String Slicing Puzzle")
print("-" * 40)
"""
Using ONLY slicing on the string below, extract the words:
    text = "PythonProgrammingIsFun"

Extract:
    - "Python"        → text[?:?]
    - "Programming"   → text[?:?]
    - "Is"            → text[?:?]
    - "Fun"           → text[?:?]
    - Reverse the entire string
    - Every second character

Expected Output:
'Python'
'Programming'
'Is'
'Fun'
'nuFsIgnimmargorPnohtyP'
'yhnPormigi u'
"""

text = "PythonProgrammingIsFun"

# Write your code below:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
