# Python Student Management System

A command-line application built in Python to manage student records. This project is being developed incrementally using Git, with each commit introducing a new feature.

## Current Features

* Interactive command-line menu
* Add a new student
* View all students
* Search students by Student ID
* Search students by Student Name (case-insensitive)
* Update existing student details by Student ID
* Store student information in memory during program execution
* Object-Oriented Programming using a `Student` class

## Planned Features

* Delete students
* Save student data to a CSV file
* Load student data from a CSV file
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
* Command-Line Interface (CLI)
* Git & GitHub

## How to Run

1. Clone the repository.

2. Navigate to the project folder.

3. Run:

```bash
python main.py
```

## How It Works

Student records are stored as `Student` objects inside a Python list. Users can add, view, search, and update student information through a menu-driven interface. When updating a student, leaving a field blank keeps its current value, making partial updates simple and user-friendly.

## Current Status

The application now supports creating, viewing, searching, and updating student records during a single program session. Persistent storage, deletion, statistics, sorting, and input validation will be added in future commits.

## Learning Goals

This project practices:

* Python fundamentals
* Classes and objects
* Object mutation
* Functions
* Lists
* Loops
* Linear search
* Conditional statements
* Modular programming
* CRUD operations
* Git workflow
