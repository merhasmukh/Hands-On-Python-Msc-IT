"""
09_exercises.py — Problem Solving Exercises
============================================
MSc (IT) — Unit 1: Problem Solving

Instructions:
- Complete each exercise by writing code in the space provided
- Focus on LOGIC — think before you code!
- Run this file with: python 09_exercises.py
"""

print("=" * 60)
print("  Unit 1 — Problem Solving Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: Pattern Programs
# ===========================================================================
print("\n🏋️  Exercise 1: Pattern Programs")
print("-" * 40)
"""
Print the following patterns (n=5 each):

Pattern A (Right Triangle):         Pattern B (Inverted):
*                                   * * * * *
* *                                 * * * *
* * *                               * * *
* * * *                             * *
* * * * *                           *

Pattern C (Pyramid):                Pattern D (Number Triangle):
    *                               1
   * *                              1 2
  * * *                             1 2 3
 * * * *                            1 2 3 4
* * * * *                           1 2 3 4 5
"""

n = 5
print("Pattern A:")
# Write Pattern A:

print("\nPattern B:")
# Write Pattern B:

print("\nPattern C:")
# Write Pattern C:

print("\nPattern D:")
# Write Pattern D:


# ===========================================================================
# Exercise 2: Linear Search
# ===========================================================================
print("\n🏋️  Exercise 2: Linear Search")
print("-" * 40)
"""
Implement `linear_search(arr, target)` that:
- Returns the INDEX of target if found
- Returns -1 if not found
- Also counts comparisons made

Expected Output:
Searching for 42 in [15, 3, 42, 8, 27, 56, 1]:
Found at index 2 (made 3 comparisons)

Searching for 99 in [15, 3, 42, 8, 27, 56, 1]:
Not found (made 7 comparisons)
"""

# Write your linear_search function here:

arr = [15, 3, 42, 8, 27, 56, 1]
# Test it:


# ===========================================================================
# Exercise 3: Binary Search
# ===========================================================================
print("\n🏋️  Exercise 3: Binary Search")
print("-" * 40)
"""
Implement `binary_search(arr, target)` (arr must be SORTED):
- Returns the index of target
- Returns -1 if not found
- Prints the search steps (left, mid, right at each step)

Also implement it recursively as `binary_search_recursive(arr, target, low, high)`.

Expected Output:
Sorted array: [1, 3, 8, 15, 27, 42, 56]
Searching for 27:
  Step 1: left=0, mid=3, right=6 → mid=15, go right
  Step 2: left=4, mid=5, right=6 → mid=42, go left
  Step 3: left=4, mid=4, right=4 → mid=27, FOUND!
Found at index 4
"""

sorted_arr = [1, 3, 8, 15, 27, 42, 56]

# Write your binary_search function here:

# Write your binary_search_recursive function here:


# ===========================================================================
# Exercise 4: Bubble Sort
# ===========================================================================
print("\n🏋️  Exercise 4: Bubble Sort")
print("-" * 40)
"""
Implement `bubble_sort(arr)` that sorts in-place.
Print the array after each PASS (outer loop iteration).

Expected Output (for [64, 34, 25, 12, 22, 11, 90]):
Original : [64, 34, 25, 12, 22, 11, 90]
After pass 1: [34, 25, 12, 22, 11, 64, 90]
After pass 2: [25, 12, 22, 11, 34, 64, 90]
...
Sorted  : [11, 12, 22, 25, 34, 64, 90]

Also count total comparisons and swaps made.
"""

# Write your bubble_sort function here:

arr = [64, 34, 25, 12, 22, 11, 90]
# Test it:


# ===========================================================================
# Exercise 5: Classic Problems
# ===========================================================================
print("\n🏋️  Exercise 5: Classic Problems")
print("-" * 40)
"""
Solve each of the following:

A) Palindrome Check:
   is_palindrome("racecar") → True
   is_palindrome("hello")   → False
   is_palindrome("Madam")   → True (case-insensitive)
   
B) Anagram Check:
   is_anagram("listen", "silent") → True
   is_anagram("hello", "world")   → False
   
C) Prime Check + List first N primes:
   is_prime(7)   → True
   is_prime(10)  → False
   first_n_primes(10) → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
   
D) Count vowels and consonants:
   "Python Programming" → Vowels: 5, Consonants: 12

E) Second Largest in a list (without sorting):
   second_largest([5, 3, 9, 1, 7, 9, 4]) → 7
"""

# A) Palindrome:

# B) Anagram:

# C) Prime:

# D) Vowels/Consonants:

# E) Second Largest:

# Test all functions:


# ===========================================================================
# Exercise 6: Sorting Challenge
# ===========================================================================
print("\n🏋️  Exercise 6: Sorting Challenge")
print("-" * 40)
"""
Implement Selection Sort and Insertion Sort.

Then use Python's built-in sort for:
1. Sort a list of student dicts by GPA (descending)
2. Sort a list of words by length, then alphabetically for ties

students = [
    {"name": "Alice", "gpa": 8.75},
    {"name": "Bob",   "gpa": 7.50},
    {"name": "Charlie","gpa": 9.00},
    {"name": "Diana", "gpa": 8.75},
]

words = ["python", "java", "c", "go", "ruby", "rust", "perl"]

Expected Output:
By GPA (desc): Charlie(9.0), Alice(8.75), Diana(8.75), Bob(7.5)
By length then alpha: c, go, java, perl, ruby, rust, python
"""

students = [
    {"name": "Alice",   "gpa": 8.75},
    {"name": "Bob",     "gpa": 7.50},
    {"name": "Charlie", "gpa": 9.00},
    {"name": "Diana",   "gpa": 8.75},
]
words = ["python", "java", "c", "go", "ruby", "rust", "perl"]

# Write selection_sort:

# Write insertion_sort:

# Sort students and words using built-in:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
