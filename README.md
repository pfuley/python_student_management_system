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
* View student statistics:

  * Total students
  * Average marks
  * Highest marks
  * Lowest marks
* Store student information as `Student` objects in memory
* Object-Oriented Programming using a `Student` class

## Planned Features

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

The application automatically loads student records from `students.csv` when it starts. Users can manage student records through a menu-driven interface and save their changes back to the CSV file. The Statistics feature analyzes the stored student data and displays summary information such as total students, average marks, and the students with the highest and lowest marks.

## Current Status

The application now supports complete CRUD functionality, CSV-based persistence, and basic statistical analysis of student records.

## Learning Goals

This project practices:

* Python fundamentals
* Object-Oriented Programming
* CRUD operations
* CSV file reading and writing
* File handling
* Lists and loops
* List comprehensions
* Lambda functions
* Aggregate calculations
* Modular programming
* Git workflow
