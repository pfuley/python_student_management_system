# Python Student Management System

A command-line application built in Python to manage student records. This project is being developed incrementally using Git, with each commit introducing a new feature.

## Current Features

* Interactive command-line menu
* Add a new student
* Store student information in memory during program execution
* View all students currently stored in memory
* Search students by Student ID
* Search students by Student Name (case-insensitive)
* Object-Oriented Programming using a `Student` class
* Student display method inside the `Student` class

## Planned Features

* Update student details
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

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd python_student_management_system
```

3. Run the application:

```bash
python main.py
```

## How It Works

Student records are stored in memory as `Student` objects inside a Python list. Users can add new students, view all students, and search for a student using either their ID or name. Name searches are case-insensitive, making the application easier to use.

## Current Status

The application currently supports creating, viewing, and searching student records during a single program session. Data persistence, editing, deletion, and statistics will be implemented in future commits.

## Learning Goals

This project is designed to practice:

* Python fundamentals
* Classes and objects
* Methods
* Functions
* Lists
* Loops
* Linear search
* Conditional statements
* Modular programming
* Git workflow
* Building applications incrementally

