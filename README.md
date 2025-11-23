# Student Database Management System

It is a python project built with Python and SQLite. This system allows us manage student records.

## Problem Statement
Educational institutions often struggle with managing student data using manual methods (like paper records) or complex software. There is a need for a simple and accessible tool that can:

   1. Store student details permanently so data isn't lost when the computer turns off.
   
   2. Allow for quick retrieval of student lists.
      
   3. Allows easy updates like changing student grade or removal of student data.
This Python program interfaces with a local SQLite database file to perform these CRUD (Create, Read, Update, Delete) operations.

## Code Structure & Explanation
### A. Library Import

import sqlite3

It Imports the built-in `sqlite3` module.This allows Python to interact with SQLite databases without installing external drivers.

### B. Database Setup 
connect_db

Functionality: This function handles the initial setup.

    1.  It connects to `student_data.db`. If the file doesn't exist, Python creates it automatically.
    
    2.  It runs a `CREATE TABLE IF NOT EXISTS` SQL query.
    
    3.  It defines the schema: `id` (integer), `name` (Text), `age` (Integer), and `grade` (Text).

### C. Adding Records
add_student

Functionality: Handles the Create aspect of CRUD.

    1.  Asks the user to input Name, Age, and Grade.
    
    2.  Establishes a fresh connection to the database.
    
    3.  Executes an `INSERT` query .

### D. Viewing Records 
view_students

Functionality: Handles the Read aspect of CRUD.

    1.  Executes a 'SELECT FROM students ' query to fetch all data.
    
    2.  Checks if the database is empty.
    
    3.  If data exists, it uses f-string formatting (e.g., `:<20`) to print a table header and rows for easy reading.
    

### E. Deleting Records 
delete_student

Functionality: Handles the Delete aspect of CRUD.

    1.  First, calls `view_students()` so the user can see the list and find the correct ID.
    
    2.  Asks for the `ID` of the student to remove.

    3.  Executes a `DELETE` SQL command.
    
    4.  Checks `cursor.rowcount` to inform the user if the deletion was successful or if the ID didn't exist.

### F. Updating Records 
update_student

Functionality: Handles the Update aspect of CRUD.

    1.  Displays current students.
    
    2.  Asks for the target `ID` and the new `Grade`.
    
    3.  Executes an `UPDATE` SQL command to modify only the specific record .

### G. The Main Controller 
main

Functionality: The entry point of the program.

    1.  Calls connect_db() to ensure the database file exists.
    
    2.  Enters a while True loop (Infinite loop) to keep the program running.
    
    3.  Displays a menu of options (1-5).
    
    4.  Uses if/elif/else loops to perform specific functions.
    
    5.  Breaks the loop only when the user selects "Exit".


