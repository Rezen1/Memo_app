''' Window for editing questions '''
from PyQt5.QtWidgets import (
        QLineEdit, QFormLayout )


txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Question:', txt_Question)
txt_Question.setStyleSheet("color: white;");
layout_form.addRow('Correct answer:', txt_Answer)
txt_Answer.setStyleSheet("color: white;");
layout_form.addRow('Incorrect option #1:', txt_Wrong1)
txt_Wrong1.setStyleSheet("color: white;");
layout_form.addRow('Incorrect option #2:', txt_Wrong2)
txt_Wrong2.setStyleSheet("color: white;");
layout_form.addRow('Incorrect option #3:', txt_Wrong3)
txt_Wrong3.setStyleSheet("color: white;");

