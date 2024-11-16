
from PyQt5.QtWidgets import (
        QWidget,
        QListView,   QHBoxLayout, QVBoxLayout,
        QPushButton  )
from memo_edit_layout import layout_form
from memo_app import app

app.setStyleSheet("""
    QWidget {
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
        stop:0 #1b4332, stop:1 #081c15);
        color:white 
    }
    QPushButton {
        color: white;
    }
""")




list_questions = QListView()
wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Нове запитання')
btn_delete = QPushButton('Видалити запитання')
btn_start = QPushButton('Почати')

main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_add)



main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)
