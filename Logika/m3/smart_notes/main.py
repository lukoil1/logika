from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
import json

def write_file():
    with open('m3/smart_notes/notes_data.json', 'w', encoding='utf8') as file:
        json.dump(notes, file , sort_keys=True, ensure_ascii=False, indent=4)
    

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

with open('m3/smart_notes/notes_data.json', 'r', encoding='utf8') as file:
    notes = json.load(file)
    
def show_notes():
    key = lst_note.currentItem().text()     
    field_text.setText(notes[key]['текст'])
    
    
    lst_tag.clear()
    lst_tag.addItems(notes[key]['теги'])
    
    
def add_note():
    note_name , ok = QInputDialog.getText(main_win , "Додавання замітки" , "Назва замітки")
    lst_note.addItem(note_name)
    
    notes[note_name] = {"текст": "","теги":[]}

def save_note():
    key = lst_note.currentItem().text()
    text = field_text.toPlainText()
    notes[key]['текст'] = text
    write_file()


def del_note():
    key = lst_note.currentItem().text()
    del notes[key]
    write_file()
    lst_tag.clear()
    lst_note.clear()
    lst_note.addItems(notes)
    field_text.clear()
        
def add_tag():
    key = lst_note.currentItem().text()
    tag = field_tag.text()
    notes[key]["теги"].append(tag)
    write_file()
    lst_tag.addItem(tag)
        
def del_tag():
    key = lst_note.currentItem().text()
    tag = lst_tag.currentItem().text()
    notes[key]["теги"].remove(tag)
    write_file()
    lst_tag.clear()
    lst_tag.addItems(notes[key]["теги"])        
 
def search_tag():
    pass 
    
    
lst_note.addItems(notes)
lst_note.itemClicked.connect(show_notes)
btn_note_create.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)
btn_note_delete.clicked.connect(del_note)
btn_tag_add.clicked.connect(add_tag)
btn_tag_unpin.clicked.connect(del_tag)
btn_tag_search.clicked.connect(search_tag)


main_win.setLayout(layout_notes)
main_win.show()
app.exec_()