from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
mainwindow = QWidget()
mainwindow.resize(150, 100)

label = QLabel('UI popup window')
label.setAlignment(Qt.AlignCenter)
okbutton = QPushButton('Ok')

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(okbutton)

okbutton.clicked.connect(exit)

mainwindow.setLayout(layout)
mainwindow.show()


app.exec_()