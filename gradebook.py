class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        student_id = student.get_id()

        if student_id not in self.students:
            self.students[student_id] = student
            self.grades[student_id] = {}

            print("Student added successfully.")

        else:
            print("Student already exists.")

    def add_course(self, course):
        course_code = course.course_code

        if course_code not in self.courses:
            self.courses[course_code] = course

            print("Course added successfully.")

        else:
            print("Course already exists.")

    def enroll_student(self, student_id, course_code):

        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]

            student.enroll_course(course_code)
            course.add_student(student_id)

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}
        else:
            print("Student or course not found.")

    def add_assessment(self, course_code, assessment):

        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)

        else:
            print("Course not found.")

    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id in self.students and course_code in self.courses:
            assessment = self.courses[course_code].find_assessment(assessment_title)

            if assessment:

                if score < 0 or score > assessment.max_score:
                    print("Invalid grade.")
                    return

                if student_id not in self.grades:
                    self.grades[student_id] = []

                    if course_code not in self.grades[student_id]: self.grades[student_id][course_code] = {}

                self.grades[student_id][course_code][assessment_title] = int(score)

                print("Grade recorded successfully.")

            else:
                print("Assessment not found.")

        else:
            print("Student or course not found")

    def calculate_average(self, student_id, course_code):

        if student_id in self.grades and course_code in self.grades[student_id]:

            scores = self.grades[student_id][course_code].values()

            if len(scores) == 0:
                return 0

            average = sum(scores) / len(scores)
            return average
        else:
            return 0

    def get_result(self, average):

        if average >= self.passing_grade:
            return "Passed"

        else:
            return "Failed"

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return
        student = self.students[student_id]

        print("Student Report")
        print("Name:", student.get_name())
        print("Student ID:", student.get_id())

        if student_id in self.grades:

            for course_code, assessment in self.grades[student_id].items():

                print("\nCourse:", course_code)

                for title, score in assessment.items():
                    print(f"{title}: {score}")

                average = self.calculate_average(student_id, course_code)

                print("Average:", average, "%")

                letter = self.get_letter_grade(average)
                print("Letter Grade:", letter)

                comment = self.get_teacher_comment(average)
                print("Teacher Comment:", comment)
                print("Result:", self.get_result(average))

    def search_student(self, keyword):
        found = False

        for student_id, student in self.students.items():
            if keyword.lower() == student_id.lower() or keyword.lower() == student.get_name().lower():
                student.display_info()
                found = True

            if not found:
                print("Student not found.")

    def delete_student(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        for course in self.courses.values():

            if student_id in course.students:
                course.students.remove(student_id)

        if student_id in self.grades:
            del self.grades[student_id]

        del self.students[student_id]

        print("Student deleted successfully.")

    def get_letter_grade(self, average):

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def dashboard(self):

        print("Total students:", len(self.students))
        print("Total courses:", len(self.courses))

        total_assessments = 0

        for course in self.courses.values():
            total_assessments += len(course.assessments)

        print("Total assessments:", total_assessments)

    def get_teacher_comment(self, average):

        if average >= 90:
            return "Excellent work!"
        elif average >= 80:
            return "Very good performance."
        elif average >= 70:
            return "Good job, keep improving."
        elif average >= 60:
            return "Satisfactory result."
        else:
            return "Needs more effort."
