from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QVBoxLayout
from random import randint
app = QApplication([])
mainwin = QWidget()
mainwin.resize(300,200)


text = QLabel('Натисни щоб дізнатись переможця')
btn = QPushButton('Згенерувати')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(winner,alignment=Qt.AlignCenter)
line.addWidget(btn,alignment=Qt.AlignCenter)
def show_winner():
    a = randint(1,100)
    winner.setText(str(a))
btn.clicked.connect(show_winner)

mainwin.setLayout(line)

mainwin.show()
app.exec_()
