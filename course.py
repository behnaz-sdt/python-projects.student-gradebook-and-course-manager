class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)
            print(f"student {student_id} enrolled successfully.")
        else:
            print("Student is already enrolled in this course")

    def add_assessment(self, assessment):
        self.assessments.append(assessment)
        print("Assessment added successfully.")

    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title.lower() == title.lower():
                return assessment
        return None

    def display_info(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Enrolled Students:", len(self.students))

        print("Assessments:")
        if len(self.assessments) == 0:
            print("No assessments added yet.")
        else:
            for assessment in self.assessments:
                print(f"-{assessment.title}/Max score:{assessment.max_score}")







