from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

def read_file():
    global profiles
    with open('m3/Bodybuilder/data_profiles.json', 'r', encoding='utf8') as file:
        profiles = json.load(file)
read_file()

def write_file():
    with open('m3/Bodybuilder/data_profiles.json', 'w', encoding='utf8') as file:
        json.dump(profiles, file , sort_keys=True, ensure_ascii=False, indent=4)    


app = QApplication([])

win_lst_profiles = QWidget()

win_lst_profiles.resize(800,500)

btn_add_profile = QPushButton("Створити профіль")
btn_delete_profile = QPushButton("Видалити профіль")
btn_setting = QPushButton("⚙️")
lst_profile = QListWidget()
lst_profile.addItems(profiles)
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

def show_info():
    global key
    key = lst_profile.currentItem().text()
    lb_name.setText("Ім'я: " +profiles[key]["personal"]["name"])
    lb_gender.setText("Стать: " +profiles[key]["personal"]["gender"])
    lb_age.setText("Вік: " +str(profiles[key]["measurments"]["age"]))
    lb_height.setText("Зріст: " +str(profiles[key]["measurments"]["height"]))
    lb_weight.setText("Вага: " +str(profiles[key]["measurments"]["weight"]))
    lb_BMI.setText("ІМТ: " +str(profiles[key]["measurments"]["bmi"]))
    field_goal.setText(  str(profiles[key]["goal"]))
    field_notes.setText(  str(profiles[key]["notes"]))
    
    
def edit_goal():
    profiles[key]["goal"] = field_goal.text()
    write_file()

def edit_notes():
    profiles[key]["notes"] = field_notes.toPlainText()
    write_file()   
    
def add_profile():
    profile_name , ok = QInputDialog.getText(win_lst_profiles , "Додавання профілю" , "Назва профілю")
    profile_name = profile_name.strip()
    if ok ==  True and profile_name != '':
        profiles[profile_name] = {
        "goal": "",
        "measurments": {"age": 0,"biceps": 0,"bmi": 0,"calf": 0,"chest": 0,"forearm": 0,"height": 0,"hips": 0,"neck": 0,"waist": 0,"weight": 0},
        "notes": "",
        "nutrition": {"creatine": 0,"protein": 0},
        "personal": {"gender": "","name": ""}
        }
        write_file()
        lst_profile.addItem(profile_name)

def del_profile():
    del profiles[key]
    write_file()
    lst_profile.clear()
    lst_profile.addItems(profiles)
      

    
    
lst_profile.itemClicked.connect(show_info)
field_goal.editingFinished.connect(edit_goal)
field_notes.textChanged.connect(edit_notes)
btn_add_profile.clicked.connect(add_profile)
btn_delete_profile.clicked.connect(del_profile)
win_lst_profiles.setLayout(main_layout)
