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
    fld_weight.setText(str(profiles[key]["measurments"]["weight"]))
    fld_age.setText(str(profiles[key]["measurments"]["age"]))
    fld_gender.setText(str(profiles[key]["personal"]["gender"]))
    fld_cretine.setText(str(profiles[key]["nutrition"]["creatine"]))
    fld_protein.setText(str(profiles[key]["nutrition"]["protein"]))
    fld_biceps.setText(str(profiles[key]["measurments"]["biceps"]))
    fld_BMI.setText(str(profiles[key]["measurments"]["bmi"]))
    fld_calf.setText(str(profiles[key]["measurments"]["calf"]))
    fld_chest.setText(str(profiles[key]["measurments"]["chest"]))
    fld_hips.setText(str(profiles[key]["measurments"]["hips"]))
    fld_neck.setText(str(profiles[key]["measurments"]["neck"]))
    fld_forearm.setText(str(profiles[key]["measurments"]["forearm"]))
    fld_waist.setText(str(profiles[key]["measurments"]["waist"]))
    win_info.show()


btn_setting.clicked.connect(show_change)
win_lst_profiles.show()
app.exec()