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
* Store student information in memory during program execution
* Object-Oriented Programming using a `Student` class

## Planned Features

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
* Object-Oriented Programming
* Command-Line Interface
* Git & GitHub

## How to Run

```bash
python main.py
```

## How It Works

Student records are stored as `Student` objects inside a Python list. Users can add, view, search, update, and delete student records through a menu-driven interface.

At this stage, all data exists only while the program is running. If the program closes, the student records are lost. CSV file saving and loading will be added in future commits.

## Current Status

The application now supports the core CRUD operations:

* Create student records
* Read/view student records
* Update student records
* Delete student records

## Learning Goals

This project practices:

* Python fundamentals
* Classes and objects
* Functions
* Lists
* Loops
* Linear search
* Object mutation
* Removing items from a list
* CRUD operations
* Modular programming
* Git workflow
