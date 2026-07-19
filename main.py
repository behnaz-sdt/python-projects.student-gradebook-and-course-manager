from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from gradebook import Gradebook
from project import Project

#Gradebook
gradebook = Gradebook()

#--------------
# Add Student
#--------------

print("\n===== Add Student =====")

student1 = Student("S001", "Ahmad", "ahmad@gmail.com")
student2 = Student("S002", "Sara", "sara@gmail.com")

gradebook.add_student(student1)
gradebook.add_student(student2)


#--------------
# Add Course
#--------------

print("\n===== Add Courses =====")

course1 = Course("PY101", "Python Programming")

gradebook.add_course(course1)

#---------------
# Enroll Student
#---------------

print("\n===== Enroll Students =====")

gradebook.enroll_student("S001", "PY101")
gradebook.enroll_student("S002", "PY101")

#---------------
# Add Assessments
#---------------

print("\n===== Add Assessments =====")

quiz1 = Quiz("Quiz1", 10)
exam1 = Exam("Midterm Exam", 100)
project1 = Project("Final project", 100)

gradebook.add_assessment("PY101", quiz1)
gradebook.add_assessment("PY101", exam1)
gradebook.add_assessment("PY101", project1)

#---------------
# Record Grades
#---------------

print("\n===== Record Grades =====")

gradebook.record_grade("S001", "PY101", "Quiz1", 85)
gradebook.record_grade("S001", "PY101", "Midterm Exam", 75)
gradebook.record_grade("S001", "PY101", "Final project", 90)

#---------------
# Show Report
#---------------

print("\n===== Student Report =====")
gradebook.show_report("S001")

#---------------
# Search Student
#---------------

print("\n===== Search Student =====")
gradebook.search_student("S001")

#---------------
# Delete Student
#---------------

print("\n===== Delete Student =====")
gradebook.delete_student("S002")

#---------------
# Dashboard
#---------------

print("\n===== Dashboard =====")

gradebook.dashboard()














