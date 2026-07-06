# Python Student Management System

A command-line application built in Python to manage student records. This project is being developed incrementally using Git, with each commit introducing a new feature.

## Current Features

* Interactive command-line menu
* Add a new student
* Store student information in memory during program execution
* View all students currently stored in memory
* Object-Oriented Programming using a `Student` class
* Student display method inside the `Student` class

## Planned Features

* Search students by ID or name
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

The program starts with an interactive menu. Users can add student records by entering details such as student ID, name, age, course, and marks.

Students are stored in a Python list while the program is running. The `Student` class contains a `display_student()` method, which is used to print student details in a readable format.

## Current Status

At this stage, students can be added and viewed while the program is running. The data is not yet saved permanently. CSV file support and additional management features will be added in future commits.

## Learning Goals

This project is designed to practice:

* Python fundamentals
* Classes and objects
* Methods
* Functions
* Lists
* Loops
* Modular programming
* Git workflow
* Building applications incrementally
