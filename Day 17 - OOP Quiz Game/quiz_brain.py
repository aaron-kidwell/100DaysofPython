
from question_model import Question
# initialize object with the starting question #, the list, and the starting score
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    #while true, creates loop until length of question list exceeded
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)
    #checks the user answer against the correct_answer key from data, adds to score if correct.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
            print(f"Your current score is: {self.score}/{self.question_number}.")
        else: 
            print("That's wrong.")
            print(f'The correct answer was: {correct_answer}.')
            print(f"Your current score is: {self.score}/{self.question_number}.")
        print('\n')