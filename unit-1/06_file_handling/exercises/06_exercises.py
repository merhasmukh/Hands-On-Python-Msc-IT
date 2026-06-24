"""
06_exercises.py — File Handling Exercises
==========================================
MSc (IT) — Unit 1: File Handling

Instructions:
- Complete each exercise by writing code in the space provided
- Run this file with: python 06_exercises.py
- Use the provided sample.txt, sample.csv, and sample.json files.
"""

print("=" * 60)
print("  Unit 1 — File Handling Exercises")
print("=" * 60)

# ===========================================================================
# Exercise 1: Read a Text File
# ===========================================================================
print("\n🏋️  Exercise 1: Read a Text File")
print("-" * 40)
"""
1. Open 'sample.txt' using a context manager (with statement).
2. Read the entire file and print its contents.
3. Print the total number of lines in the file.
"""

# Write your code below:


# ===========================================================================
# Exercise 2: Write to a Text File
# ===========================================================================
print("\n🏋️  Exercise 2: Write to a Text File")
print("-" * 40)
"""
1. Create a new file named 'my_output.txt' in write mode ('w').
2. Write 3 lines of text into it (e.g., your name, course, and hobby).
3. Open it again in append mode ('a') and add one more line.
4. Finally, read and print the contents of 'my_output.txt' to verify.
"""

# Write your code below:


# ===========================================================================
# Exercise 3: Process a CSV File
# ===========================================================================
print("\n🏋️  Exercise 3: Process a CSV File")
print("-" * 40)
"""
Using the 'sample.csv' file:
1. Open and read it using csv.DictReader.
2. Calculate and print the average 'Score' of all students.
3. Print the names of students who live in 'Mumbai'.
"""
import csv

# Write your code below:


# ===========================================================================
# Exercise 4: Read and Write JSON Data
# ===========================================================================
print("\n🏋️  Exercise 4: Read and Write JSON Data")
print("-" * 40)
"""
Using the 'sample.json' file:
1. Read the JSON data into a Python dictionary.
2. Print the 'university' name and the total number of students.
3. Add a new student to the 'students' list.
4. Save the modified data to a new file 'updated_sample.json' with an indent of 2.
"""
import json

# Write your code below:


print("\n" + "=" * 60)
print("  All exercises completed! Submit your file.")
print("=" * 60)
