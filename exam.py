from assessment import Assessment

class Exam(Assessment):
    def display_info(self):
        print(f"Exam: {self.title} - Max score: {self.max_score}")