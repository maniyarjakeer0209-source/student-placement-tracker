# student-placement-tracker
A Python OOP project for managing student placement profiles.
# Student Placement Tracker

A Python OOP project for managing student placement profiles.

## Project Overview

The Student Placement Tracker is a menu-driven Python application created using Object-Oriented Programming concepts.

The application allows users to:

- Add student profiles
- Display all students
- Update mock scores
- Change the platform name
- View the total number of students
- Exit the application

## OOP Concepts Used

- Classes and Objects
- Constructors
- Instance Variables
- Class Variables
- Instance Methods
- Encapsulation
- Private Attributes
- Properties and Setters
- Static Methods
- Class Methods
- Alternative Constructors

## Student Details

Each student profile contains:

- Student ID
- Name
- Branch
- Mock Score
- Placement Status

## Score Validation

Scores are accepted only between 0 and 100.

Placement status is calculated as:

- 80–100 → Placement Ready
- 60–79 → Needs More Practice
- 0–59 → Not Ready

  ## Test Cases

| Test Case | Expected Result |
|---|---|
| Add a student with valid details | Student added successfully |
| Add a student with duplicate ID | Student ID already exists |
| Display students | Student profiles are displayed |
| Update score with a valid value | Score is updated successfully |
| Update score with value below 0 or above 100 | Score is not updated |
| Search for a non-existing student | Student not found |
| Change platform | Platform is updated for all students |
| Show total students | Total student count is displayed |
| Enter an invalid menu option | Invalid choice message is displayed |
| Select Exit | Program terminates |

## How to Run

Make sure Python is installed and run:

```bash
python main.py
