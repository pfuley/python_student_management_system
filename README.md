# Python Student Management System

A command-line application built in Python to manage student records. This project is being developed incrementally using Git, with each commit introducing a new feature.

## Current Features

* Interactive command-line menu
* Add a new student
* View all students
* Search students by Student ID
* Search students by Student Name
* Update existing student details by Student ID
* Delete a student by Student ID
* Save student records to a CSV file
* Automatically load student records from a CSV file on startup
* Store student information as `Student` objects in memory
* Object-Oriented Programming using a `Student` class

## Planned Features

* Student statistics
* Sort students
* Input validation and error handling

## Project Structure

```text
python_student_management_system/
│
├── main.py
├── menu.py
├── student.py
├── file_handler.py
├── utils.py
├── students.csv
├── README.md
├── .gitignore
└── requirements.txt
```

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* CSV File Handling
* Command-Line Interface (CLI)
* Git & GitHub

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run:

```bash
python main.py
```

## How It Works

When the application starts, it automatically loads student records from `students.csv` into memory as `Student` objects. Users can then add, view, search, update, or delete records during the session. Selecting **Save Data** writes the current records back to the CSV file, allowing changes to persist between program runs.

## Current Status

The application now supports persistent storage using CSV files. Student data can be loaded at startup and saved after changes, making the project function as a simple file-based student management system.

## Learning Goals

This project practices:

* Python fundamentals
* Object-Oriented Programming
* CRUD operations
* File handling
* CSV file reading and writing
* Module organization
* Lists and loops
* Persistent data storage
* Git workflow
