from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

app = QApplication([])

win_lst_profiles = QWidget()

win_lst_profiles.resize(800,500)

btn_add_profile = QPushButton("Створити профіль")
btn_delete_profile = QPushButton("Видалити профіль")
btn_setting = QPushButton("⚙️")
lst_profile = QListWidget()
lb_name = QLabel("Ім'я:")
lb_gender = QLabel("Стать:")
lb_age = QLabel("Вік:")
lb_height = QLabel("Зріст:")
lb_weight = QLabel("Вага:")
lb_BMI = QLabel("ІМТ:")
lb_goal = QLabel("Ціль:")
lb_notes = QLabel("Нотатки:")
field_goal = QLineEdit()
field_notes = QTextEdit()


main_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

main_layout.addLayout(col1 , 1)
main_layout.addLayout(col2 , 4)

col1.addWidget(lst_profile)
col1.addWidget(btn_add_profile)
col1.addWidget(btn_delete_profile)

col2.addWidget(btn_setting)
col2.addWidget(lb_name)
col2.addWidget(lb_gender)
col2.addWidget(lb_age)
col2.addWidget(lb_height)
col2.addWidget(lb_weight)
col2.addWidget(lb_BMI)
col2.addWidget(lb_goal)
col2.addWidget(field_goal)
col2.addWidget(lb_notes)
col2.addWidget(field_notes)

win_lst_profiles.setLayout(main_layout)
