from Question import Question
from data import que

questions = []

for question in que:
    ques = Question(question["category"],
                    question["type"],
                    question["difficulty"],
                    question["question"],
                    question["correct_answer"],
                    question["incorrect_answers"][0],
                    )
    questions.append(ques)
