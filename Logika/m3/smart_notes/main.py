from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )

app = QApplication([])
main_win = QWidget()
main_win.resize(600, 500)

field_text =QTextEdit()

lb_note =QLabel('Список заміток')
lst_note = QListWidget()

btn_note_create = QPushButton('Створити замітку')
btn_note_delete = QPushButton('Видалити замітку')
btn_note_save = QPushButton('Зберегти замітку')

lb_tag = QLabel('Список тегів')
lst_tag = QListWidget()

field_tag = QLineEdit()
field_tag.setPlaceholderText('Введіть тег...')
btn_tag_add = QPushButton('Додати до замітки')
btn_tag_unpin = QPushButton('Відкріпити від замітки')
btn_tag_search = QPushButton('Шукати замітки по тегу')

layout_notes = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1 , 4)
layout_notes.addLayout(col2 , 2)

col1.addWidget(field_text)
col2.addWidget(lb_note)
col2.addWidget(lst_note)
col2.addWidget(btn_note_create)
col2.addWidget(btn_note_delete)
col2.addWidget(btn_note_save)
col2.addWidget(lb_tag)
col2.addWidget(lst_tag)
col2.addWidget(field_tag)
col2.addWidget(btn_tag_add)
col2.addWidget(btn_tag_unpin)
col2.addWidget(btn_tag_search)



main_win.setLayout(layout_notes)
main_win.show()
app.exec_()