from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

win_info = QWidget()
btn_save = QPushButton("Зберегти")
fld_name = QLineEdit()
fld_height = QLineEdit()
fld_weight = QLineEdit()
form = QFormLayout()
form.addRow("Ім'я:", fld_name)
form.addRow("Зріст:", fld_height)
form.addRow("Вага:", fld_weight)
form.addWidget(btn_save)
win_info.setLayout(form)