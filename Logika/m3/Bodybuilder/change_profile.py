from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

win_info = QWidget()
btn_save = QPushButton("Зберегти")
fld_name = QLineEdit()
fld_height = QLineEdit()
fld_weight = QLineEdit()
fld_age = QLineEdit()

fld_gender = QLineEdit()
fld_cretine = QLineEdit()
fld_protein = QLineEdit()
fld_biceps = QLineEdit()
fld_BMI = QLineEdit()
fld_calf = QLineEdit()
fld_chest = QLineEdit()
fld_hips = QLineEdit()
fld_neck = QLineEdit()
fld_forearm = QLineEdit()
fld_waist= QLineEdit()


form = QFormLayout()
form.addRow("Ім'я:", fld_name)
form.addRow("Зріст:", fld_height)
form.addRow("Вага:", fld_weight)
form.addRow("Вік", fld_age )
form.addRow("Стать", fld_gender )
form.addRow("Креатин", fld_cretine)
form.addRow("Протеїн", fld_protein )
form.addRow("Біцепс", fld_biceps )
form.addRow("ІМТ", fld_BMI )
form.addRow("Ікра", fld_calf )
form.addRow("Груди", fld_chest )
form.addRow("Стегна", fld_hips )
form.addRow("Шия", fld_neck )
form.addRow("Передпліччя", fld_forearm )
form.addRow("Талія", fld_waist )
form.addWidget(btn_save)
win_info.setLayout(form)