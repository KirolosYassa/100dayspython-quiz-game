class Quiz:

    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_score = 0

    def show_score(self, answer, question):
        if answer:
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question.correct_answer}.")
        print(f"Your current score is: {self.score}/{self.total_score}\n\n")

    def show_quiz(self):
        for quiz in self.questions:
            ans = input(f"Q.{self.total_score+1}({quiz.category}): {quiz.question} ( True/False ): ")
            answer = quiz.check_answer(ans)
            self.total_score += 1
            if answer:
                self.score += 1
            self.show_score(answer, quiz)

        print(f"""
You've completed the quiz
Your final score was: {self.score}/{self.total_score}
                """)

