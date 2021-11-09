#Day 17/100 Python OOP Quiz Game using API from Open Trivia DB

#import created classes and methods from other files
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

#create an empty list where the question class will append to
question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']    
    #creating object to append to question bank
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
#while loop to run until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")

