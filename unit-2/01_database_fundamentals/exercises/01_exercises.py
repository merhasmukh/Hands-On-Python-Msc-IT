"""
01_exercises.py — Database Fundamentals
=======================================
MSc (IT) — Unit 2: Web Application Development with Flask and Databases

Instructions:
- Complete each exercise by writing code in the space provided.
- Run this file to verify your database operations.
"""

import sqlite3
import os

print("=" * 60)
print("  Unit 2 — Database Fundamentals Exercises")
print("=" * 60)

db_file = "exercise.db"

# Cleanup from previous runs
if os.path.exists(db_file):
    os.remove(db_file)

# Connect to the new database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# ===========================================================================
# Exercise 1: Create a Table
# ===========================================================================
print("\n🏋️  Exercise 1: Create a Table")
print("-" * 40)
"""
Write SQL to create a table named 'books' with the following columns:
1. id (INTEGER, Primary Key, Auto-increment)
2. title (TEXT, Not Null)
3. author (TEXT, Not Null)
4. year_published (INTEGER)
"""

# Write your CREATE TABLE query below:
create_query = """

"""
# cursor.execute(create_query)
# print("Table 'books' created.")


# ===========================================================================
# Exercise 2: Insert Data (Create)
# ===========================================================================
print("\n🏋️  Exercise 2: Insert Data")
print("-" * 40)
"""
Insert 3 books into the 'books' table using parameterized queries (?).
Example data:
- "1984", "George Orwell", 1949
- "To Kill a Mockingbird", "Harper Lee", 1960
- "The Great Gatsby", "F. Scott Fitzgerald", 1925
"""

# Write your INSERT code below:
books_to_insert = [
    # Add tuples here
]

# cursor.executemany("...", books_to_insert)
# conn.commit()
# print("Books inserted.")


# ===========================================================================
# Exercise 3: Select Data (Read)
# ===========================================================================
print("\n🏋️  Exercise 3: Select Data")
print("-" * 40)
"""
Write a query to SELECT and print all books published before 1950.
"""

# Write your SELECT query below:


# ===========================================================================
# Exercise 4: Update Data (Update)
# ===========================================================================
print("\n🏋️  Exercise 4: Update Data")
print("-" * 40)
"""
Update the year_published of "1984" to 1950.
"""

# Write your UPDATE query below:

# conn.commit()


# ===========================================================================
# Exercise 5: Delete Data (Delete)
# ===========================================================================
print("\n🏋️  Exercise 5: Delete Data")
print("-" * 40)
"""
Delete the book written by "F. Scott Fitzgerald".
"""

# Write your DELETE query below:

# conn.commit()


print("\n" + "=" * 60)
print("  All exercises completed! Check the exercise.db file.")
print("=" * 60)

# Close connection
conn.close()
