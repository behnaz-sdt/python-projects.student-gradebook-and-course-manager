class Student:
    def __init__(self, student_id, name, email):
        self.__courses = []
        self.__student_id = student_id
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
            print("email updated successfully")
        else:
            print("invalid email address")

    def enroll_course(self, course_code):
        if course_code not in self.__courses:
            self.__courses.append(course_code)
            print(f"{course_code} added to student's courses")
        else:
            print("student is already enrolled in this course.")

    def display_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Email:", self.__email)
        print("Enrolled courses:", self.__courses)
