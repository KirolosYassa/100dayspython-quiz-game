class Question:

    def __int__(self, question_statement, answer):
        self.question_statement = question_statement
        self.answer = answer

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        return False


q1 = Question("Plane flies? ( True/False )?", "t")
answer = input(q1.question_statement)
print(q1.check_answer(answer))

# class Quiz:
#     questions = Question([])
#     score = 0

    # def check_answer(self):
    #
    # def show_score(self):
    #     print(f"Your current score is {str(len(questions))}/{}")
