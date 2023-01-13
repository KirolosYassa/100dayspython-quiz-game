from Question import Question
from data import que

questions = []

for question in que:
    ques = Question(question[0], question[1])
    questions.append(ques)
