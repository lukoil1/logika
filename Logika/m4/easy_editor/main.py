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
    exts = ['png', 'jpeg', 'jpg', 'bmp', 'gif' ]
    img_file = []

    for file in files:
        for ext in exts:
            if file.endswith(ext):
                img_file.append(file)
    return img_file


    
def showFilenamesList():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    #print(workdir)
    files_and_folders = os.listdir(workdir)
    files = filter(files_and_folders)
    lst_images.clear()
    lst_images.addItems(files)

class ImageProccesor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = "Modified/"
    def Loadimage(self , filename):
        self.filename = filename
        full_path = os.path.join(workdir , filename)
        self.original = Image.open(full_path)
        
    def showimage(self , full_path):
        lb_pic.hide()
        pixmapimage = QPixmap(full_path)
        w = lb_pic.width()
        h = lb_pic.height()
        pixmapimage = pixmapimage.scaled(w , h , Qt.KeepAspectRatio)
        lb_pic.setPixmap(pixmapimage)
        
        
        lb_pic.show()
        
def showchosenitem():
    filename = lst_images.currentItem().text()
    workImage.Loadimage(filename)
    full_path = os.path.join(workdir , filename)
    workImage.showimage(full_path)
    
    
            
workImage = ImageProccesor()
        
        
btn_folder.clicked.connect(showFilenamesList)
lst_images.itemClicked.connect(showchosenitem)
main_win.setLayout(h_main)
main_win.show()
app.exec()