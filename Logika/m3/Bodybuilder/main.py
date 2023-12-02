from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
from profiles import *
from change_profile import *

def show_change():
    global key
    key = lst_profile.currentItem().text()
    fld_name.setText(profiles[key]["personal"]['name'])
    fld_height.setText(str(profiles[key]["measurments"]['height']))
    
    win_info.show()


btn_setting.clicked.connect(show_change)
win_lst_profiles.show()
app.exec()