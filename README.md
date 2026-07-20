# Student Gradebook & Course Manager
A python-based Object-Oriented Programming(OOP) application designed to manage students, courses, grades, assessments and grades.

## Author
Developed by Behnaz Saadat
Python Developer

## Project Title
Student Gradebook and Course Manager

## Project Description
Student Gradebook & Course Manager is a Python-based project developed using Object-Oriented Programming (OOP) principles.

The purpose of this project is to provide a simple system for managing students, courses, assessments and grades. 
The program allows user to create students and courses, enroll student into courses, add different types of assessments, record grades, and calculate student averages.
This project is organized using multiple classes, with each class responsible for specific part of the system.

The project demonstrates the use of Object-Oriented Programming concepts such as encapsulation, inheritance, and method overriding.

## How to Run the Project
 - Make sure that Python 3 is installed on your computer.
 - Open the project folder in PYCharm or another Python IDE.
 - Run the main.py file.

The main.py file is the main entry point of the application.

## Classes Created

### Student 
stores student information including student ID, name, email and enrollment courses.

### Course
Manages course information such as course code, course name and enrolled students.

### Assessment
The parent class for all assessments. Stores assessment details and provides methodes for display information, calculating percentages and giving feedback.

### Quiz
Child class of Assessment that inherits from Assessment and represents quiz assessments with customized behavior.

### Exam 
Child class of Assessment that provides exam specific display.

### Project
Child class of Assessment that provides project-specific display and feedback.

### Gradebook
The Gradebook class manages students, courses, assessments and grades. It handles enrollment, recording grades, calculating averages, reports and results.

### Main
The main file of the application. It runs the program, create objects from different classes, and demonstrates how students, courses, assessments and grades work together.

## Object-Oriented Programming Concepts Used

### Encapsulation
Encapsulation is used in the student class by making important attributes private and controlling access to them.

### Inheritance
Inheritance is used in Quiz, Exam and Project classes. All three of these classes inherit attributes and methods from the Assessment parent class.

### Method Overriding
Method overriding is used in Quiz, Exam and Project classes by changing inherited methods such as 'display_info()' and 'grade_message' to provide specific behaviors.

## Custom Features
 - Letter Grade System: Converts student averages into letter grades such as A, B, C, D and F.
 - Teacher Comments: Add personalized comments to student reports based on their performance.
 - Dashboard: Displays useful statistics such as the number of students, courses and Assessments.





