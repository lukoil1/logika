from random import choice, shuffle
from time import sleep
from menu_window import*
from main_window import*

class Question():
    def __init__(self , question , answer , wrong_answer1 , wrong_answer2 , wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        
q1 = Question('2+2' , '4', '1' , '5', 'anton')       
q2 = Question('2+4' , '6', '3' , '20', 'andrii')       
q3 = Question('2+8' , '10', '100' , '6', 'ihor')       
        
questions = [q1 , q2 , q3]        
radio_list = [r_btn1 , r_btn2, r_btn3 , r_btn4]    

def new_question():
    random_q = choice(questions)
    shuffle(radio_list)
    lb_questien.setText(random_q.question)   

new_question()


main_win.show()
app.exec()