from mimetypes import init


class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = int(max_score)

    def calculate_percentage(self,score):
        return(score/self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 50:
            return "passed"
        else:
            return "failed"

    def display_info(self):
        print(f"{self.title}-Max score: {self.max_score}")
