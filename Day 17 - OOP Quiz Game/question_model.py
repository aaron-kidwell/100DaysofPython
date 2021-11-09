#open trivia DB questions and answers pass through this and assign it to 'new_question' variable
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
