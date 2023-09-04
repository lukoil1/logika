from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QVBoxLayout, QRadioButton, QMessageBox , QHBoxLayout
from random import randint
app = QApplication([])
mainwin = QWidget()
mainwin.resize(300,200)

text = QLabel('Скільки є видів грифів')
btn1 = QRadioButton('1')
btn2 = QRadioButton('5')
btn3 = QRadioButton('3')
btn4 = QRadioButton('7')

vline = QVBoxLayout()
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(text,alignment=Qt.AlignCenter)
hline2.addWidget(btn1,alignment=Qt.AlignCenter)
hline2.addWidget(btn2,alignment=Qt.AlignCenter)
hline3.addWidget(btn3,alignment=Qt.AlignCenter)
hline3.addWidget(btn4,alignment=Qt.AlignCenter)

vline.addLayout(hline1)
vline.addLayout(hline2)
vline.addLayout(hline3)

def win():
    winner = QMessageBox()
    winner.setText('Та ти прям знаток !')
    winner.exec_()
    
    
def losse():
    winner = QMessageBox()
    winner.setText('Lox')
    winner.exec_()


btn1.clicked.connect(losse)
btn2.clicked.connect(losse)
btn3.clicked.connect(losse)
btn4.clicked.connect(win)


mainwin.setLayout(vline)

mainwin.show()
app.exec_()