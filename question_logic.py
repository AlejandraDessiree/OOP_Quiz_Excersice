from data import question_data
from Users import Question, QuizBrain, User


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
player = User()
username = player.username
id_player = player.id
questions = QuizBrain(question_bank)

while questions.still_question():
    questions.next_question()

print(f"ID:{id_player} {username} this is the end of the test.")
print(f"Final Score: {questions.score}/{len(question_bank)}")