import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout
from PyQt5.QtGui import QIcon

class WindowExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle('Olawale\'s app')
        self.setWindowIcon(QIcon('./icons/medicine.png'))

        # self.setFixedHeight(400)
        # self.setFixedWidth(300)
        # self.setWindowOpacity(0.8)

        # self.setStyleSheet('background-color:pink')

        self.create_button()
        self.create_label()
        self.btn_count = 0

        vbox = QVBoxLayout()

        btn1 = QPushButton('Click One')
        btn2 = QPushButton('Click Two')
        btn3 = QPushButton('Click Three')
        btn4 = QPushButton('Click Four')
        btn5 = QPushButton('Click Five')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(btn5)

        self.setLayout(vbox)

        # self.show()
    def clicked_btn(self):

        self.label1.setText(f'I was clicked {self.btn_count} times')
        self.btn_count += 1

    def create_button(self):
        btn1 = QPushButton('Click Moi',self)
        # btn1.move(50,100)
        btn1.setText('Ooo')
        btn1.setGeometry(50,100,100,50)
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:green')
        btn1.clicked.connect(self.clicked_btn)

        btn2 = QPushButton(self)
        # btn2.setText('Exit')
        btn2.setIcon(QIcon('./icons/exit.png'))

    def create_label(self):
        self.label1 = QLabel(self)
        self.label1.setText('Nothing Happening')
        self.label1.setGeometry(100,50,200,50)
        self.label1.show()



app = QApplication(sys.argv)
window = WindowExample()
window.show()
app.exec_()