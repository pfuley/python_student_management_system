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
* Save all student records to a CSV file
* Store student information as objects during program execution
* Object-Oriented Programming using a `Student` class

## Planned Features

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

Student records are stored as `Student` objects while the application is running. Users can perform all CRUD operations through the menu interface.

Selecting **Save Data** exports every student record into a CSV file named `students.csv`, allowing the data to be stored outside the application for future use.

## Current Status

The application now supports:

* Create student records
* View student records
* Search student records
* Update student records
* Delete student records
* Export student records to a CSV file

The next milestone is automatically loading previously saved data when the application starts.

## Learning Goals

This project practices:

* Python fundamentals
* Object-Oriented Programming
* Classes and objects
* CRUD operations
* File handling
* CSV file writing
* Lists
* Loops
* Modular programming
* Git workflow
