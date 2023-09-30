from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

main_win = QWidget()
main_win.resize(600, 500)

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_ok = QPushButton('Відповісти')

box_minuts = QSpinBox()
box_minuts.setValue(10)

lb_questien = QLabel('')


RadioGroupBox = QGroupBox('Варінти відповідей')
RadioGroup = QButtonGroup()

r_btn1 = QRadioButton('')
r_btn2 = QRadioButton('')
r_btn3 = QRadioButton('')
r_btn4 = QRadioButton('')

RadioGroup.addButton(r_btn1)
RadioGroup.addButton(r_btn2)
RadioGroup.addButton(r_btn3)
RadioGroup.addButton(r_btn4)

Layout_ans1 =QHBoxLayout() 
Layout_ans2 =QVBoxLayout() 
Layout_ans3 =QVBoxLayout() 

Layout_ans2.addWidget(r_btn1)
Layout_ans2.addWidget(r_btn2)

Layout_ans3.addWidget(r_btn3)
Layout_ans3.addWidget(r_btn4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

AnsGroupBox =QGroupBox('Результат тесту')

lb_correct = QLabel('')
lb_result = QLabel('')

Layout_res =QVBoxLayout()
Layout_res.addWidget(lb_result , alignment=(Qt.AlignLeft|Qt.AlignTop))
Layout_res.addWidget(lb_correct , alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(Layout_res)
AnsGroupBox.hide()

Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()
Layout_line4 = QHBoxLayout()

Layout_line1.addWidget(btn_menu)
Layout_line1.addStretch(1)
Layout_line1.addWidget(btn_rest)
Layout_line1.addWidget(box_minuts)
Layout_line1.addWidget(QLabel('хвилин'))

Layout_line2.addWidget(lb_questien , alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

Layout_line3.addWidget(RadioGroupBox)
Layout_line3.addWidget(AnsGroupBox)

Layout_line4.addStretch(1)
Layout_line4.addWidget(btn_ok)
Layout_line4.addStretch(1)

Layout_card= QVBoxLayout()
Layout_card.addLayout(Layout_line1)
Layout_card.addLayout(Layout_line2)
Layout_card.addLayout(Layout_line3)
Layout_card.addLayout(Layout_line4)

main_win.setLayout(Layout_card)