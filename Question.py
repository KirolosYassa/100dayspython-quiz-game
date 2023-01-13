class Question:

    def __init__(self, question_statement, ans):
        self.question_statement = question_statement
        self.answer = ans

    def check_answer(self, ans):
        if ans == self.answer:
            return True
        return False
