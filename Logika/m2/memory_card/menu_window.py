from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
menu_win = QWidget()
txt_question = QLineEdit()
txt_answer = QLineEdit()
txt_wrong1 = QLineEdit()
txt_wrong2 = QLineEdit()
txt_wrong3 = QLineEdit()

layout_form = QFormLayout()
layout_form.addRow('Введіть запитання', txt_question)
layout_form.addRow('Введіть правильну відповідь', txt_answer)
layout_form.addRow('Введіть не правильну відповідь1', txt_wrong1)
layout_form.addRow('Введіть не правильну відповідь2', txt_wrong2)
layout_form.addRow('Введіть не правильну відповідь3', txt_wrong3)

btn_add_question = QPushButton('Додати запитання')
btn_back = QPushButton('Повернутись')
btn_clear = QPushButton('Очистити')

h_btn = QHBoxLayout()
h_btn.addWidget(btn_add_question)
h_btn.addWidget(btn_back)
h_btn.addWidget(btn_clear)

v_line = QVBoxLayout()
v_line.addLayout(layout_form)
v_line.addLayout(h_btn)
menu_win.setLayout(v_line)

