class User:
    user_count = 1000

    def __init__(self):
        User.user_count += 1
        self.id = User.user_count
        self.username = input("Whats your name? ")
        
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_question(self):
        return self.question_number < len(self.question_list)
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer_q = input(f"Q.{self.question_number}: {current_question.text}(True/ False)? \n")
        self.check_answer(answer_q, current_question.answer)
        
    def check_answer(self, answer_q, correct_answer):
        if answer_q.lower() == correct_answer.lower():
            self.score += 1
        else:
            pass
