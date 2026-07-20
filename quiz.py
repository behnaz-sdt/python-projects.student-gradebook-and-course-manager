from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz:{self.title}- Max score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Great quiz result."
        else:
            return "Needs more practice."


