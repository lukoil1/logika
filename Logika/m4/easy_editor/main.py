from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from PIL import Image, ImageFilter

import os

app = QApplication([])
main_win = QWidget()
main_win.resize(900,600)
btn_folder  = QPushButton("Папка")
btn_left  = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_mirror  = QPushButton("Дзеркало")
btn_sharp  = QPushButton("Різкість")
btn_BW  = QPushButton("Ч/Б")

lst_images = QListWidget()

lb_pic = QLabel("Картинка") 

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h_main = QHBoxLayout()

v1.addWidget(btn_folder)
v1.addWidget(lst_images)

v2.addWidget(lb_pic)
v2.addLayout(h1)

h1.addWidget(btn_left)
h1.addWidget(btn_right)
h1.addWidget(btn_mirror)
h1.addWidget(btn_sharp)
h1.addWidget(btn_BW)

h_main.addLayout(v1,1)
h_main.addLayout(v2,4)

def filter(files):
    pass
    
def showFilenamesList():
    workdir = QFileDialog.getExistingDirectory()
    #print(workdir)
    files_and_folders = os.listdir(workdir)
    



btn_folder.clicked.connect(showFilenamesList)

main_win.setLayout(h_main)
main_win.show()
app.exec()