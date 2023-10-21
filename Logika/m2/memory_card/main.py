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
    lb_correct.setText(random_q.answer)
    
    radio_list[0].setText(random_q.answer)
    radio_list[1].setText(random_q.wrong_answer1)
    radio_list[2].setText(random_q.wrong_answer2)
    radio_list[3].setText(random_q.wrong_answer3)

new_question()


def check_result():
    if radio_list[0].isChecked():
        lb_result.setText('Правильно')
    else:
        lb_result.setText('Не правильно')
        
    RadioGroupBox.hide()
    AnsGroupBox.show()
    
def click_ok():
    if btn_ok.text()== 'Відповісти':
        check_result()
        
        RadioGroup.setExclusive(False)
        for btn in radio_list:
            btn.setChecked(False)
        RadioGroup.setExclusive(True)
        
        btn_ok.setText('Наступне запитання')
    else:
        new_question()
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_ok.setText('Відповісти')

def rest():
    main_win.hide()
    n = box_minuts.value()*60
    sleep(n)
    main_win.show()

def menu_show():
    main_win.hide()
    menu_win.show()

def main_show():
    menu_win.hide()
    main_win.show()

def clear():
    txt_answer.clear()
    txt_question.clear()
    txt_wrong1.clear()
    txt_wrong2.clear()
    txt_wrong3.clear()
    
def add_question():
    question = txt_question.text()
    answer = txt_answer.text()
    wrong1 = txt_wrong1.text()
    wrong2 = txt_wrong2.text()
    wrong3 = txt_wrong3.text()
    
    newq = Question(question , answer , wrong1 , wrong2 , wrong3)
    questions.append(newq)
    clear()

btn_add_question.clicked.connect(add_question)
btn_clear.clicked.connect(clear)
btn_menu.clicked.connect(menu_show)
btn_back.clicked.connect(main_show)
btn_ok.clicked.connect(click_ok)
btn_rest.clicked.connect(rest)

main_win.show()
app.exec()