from student import Student
from course import Course
from gradebook import Gradebook
from quiz import Quiz
from exam import Exam
from project import Project

gradebook = Gradebook()


def menu():
    while True:

        print("\n===== Student Gradebook System =====")
        print("1. Add Students")
        print("2. View Students")
        print("3. Search Students")
        print("4. Delete Students")
        print("5. Add Course")
        print("6. Enroll Students")
        print("7. Add Quiz")
        print("8. Add Exam")
        print("9. Add Project")
        print("10. Record Grade")
        print("11. Show Student Report")
        print("12. Dashboard")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":

            student_id = input("Student ID: ").upper()
            name = input("Name: ")
            email = input("Email:")

            if student_id == "" or name == "" or email == "":
                print("All fields are required!")

            elif "@" not in email or "." not in email:
                print("Invalid email!")

            else:
                student = Student(student_id, name, email)
                gradebook.add_student(student)

        elif choice == "2":

            for student in gradebook.students.values():
                student.display_info()


        elif choice == "3":

            keyword = input("Student ID or Name: ")

            if keyword.strip() == "":
                print("Please enter search value!")

            else:
                gradebook.search_student(keyword)

        elif choice == "4":

            student_id = input("Student ID: ").upper()

            if student_id.strip() == "":
                print("Student ID is required!")

            else:
                gradebook.delete_student(student_id)

        elif choice == "5":

            code = input("Course Code: ").upper()
            name = input("Course Name: ")

            if code.strip() == "" or name.strip() == "":
                print("All fields are required!")

            else:

                course = Course(code, name)
                gradebook.add_course(course)

        elif choice == "6":

            student_id = input("Student ID: ")
            course_code = input("Course Code: ")

            if student_id.strip() == "" or course_code.strip() == "":
                print("All fields are required!")

            else:
                gradebook.enroll_student(student_id, course_code)
                print("Student enrolled successfully!")

        elif choice == "7":

            course_code = input("Course Code: ").upper()
            title = input("Quiz Title: ")
            score = input("Max Score: ")

            if course_code.strip() == "" or title.strip() == "":
                print("All fields are required!")

            elif not score.isdigit():
                print("Score must be a number.")

            else:

                quiz = Quiz(title, int(score))
                gradebook.add_assessment(course_code, quiz)

        elif choice == "8":

            course_code = input("Course Code: ").upper()
            title = input("Exam Title: ")
            score = input("Max Score: ")

            if course_code.strip() == "" or title.strip() == "":
                print("All fields are required!")

            elif not score.isdigit():
                print("Score must be a number.")

            else:

                exam = Exam(title, int(score))
                gradebook.add_assessment(course_code, exam)

        elif choice == "9":

            course_code = input("Course Code: ").upper()
            title = input("Project Title: ")
            score = input("Max Score: ")

            if course_code.strip() == "" or title.strip() == "":
                print("All fields are required!")

            elif not score.isdigit():
                print("Score must be a number.")

            else:

                project = Project(title, int(score))
                gradebook.add_assessment(course_code, project)

        elif choice == "10":

            student_id = input("Student ID: ").upper()
            course_code = input("Course Code: ")
            title = input("Assessment Title: ")
            score = input("Score: ")

            if student_id.strip() == "" or course_code.strip() == "" or title.strip() == "":
                print("All fields are required!")

            elif not score.isdigit():
                print("Score must be a number!")

            else:
                gradebook.record_grade(
                    student_id,
                    course_code,
                    title,
                    int(score)
                )

        elif choice == "11":

            student_id = input("Student ID: ").upper()

            gradebook.show_report(student_id)

        elif choice == "12":

            gradebook.dashboard()

        elif choice == "0":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


menu()
