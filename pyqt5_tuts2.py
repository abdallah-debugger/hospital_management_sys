from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton, QGroupBox, QRadioButton, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,300)
        self.setWindowTitle('PyQt5 HBoxLayout')
        self.setWindowIcon(QIcon('./icons/medicine.png'))

        # hbox = QHBoxLayout()
        #
        # btn1 = QPushButton('Click One')
        # btn2 = QPushButton('Click Two')
        # btn3 = QPushButton('Click Three')
        # btn4 = QPushButton('Click Four')
        #
        # hbox.addWidget(btn1)
        # hbox.addWidget(btn2)
        # hbox.addWidget(btn3)
        # hbox.addWidget(btn4)


        self.create_radiobutton()
        # self.setLayout(hbox)
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)


    def create_radiobutton(self):
        self.groupbox = QGroupBox('WHat is your favorite sport?')
        self.groupbox.setFont(QFont('Sanserif',15))

        hbox = QHBoxLayout()
        self.rad1 = QRadioButton('Football')
        self.rad1.setChecked(True)
        self.rad1.setIcon(QIcon('./icons/schedule.png'))
        self.rad1.setIconSize(QSize(50,50))
        self.rad1.toggled.connect(self.radio_clicked)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton('Basket Ball')
        self.rad2.setIcon(QIcon('./icons/medicine.png'))
        self.rad2.setIconSize(QSize(50, 50))
        self.rad2.toggled.connect(self.radio_clicked)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton('Tennis')
        self.rad3.setIcon(QIcon('./icons/exit.png'))
        self.rad3.setIconSize(QSize(50, 50))
        self.rad3.toggled.connect(self.radio_clicked)
        hbox.addWidget(self.rad3)

        self.groupbox.setLayout(hbox)

        self.labela = QLabel(self)
        self.labela.setText('Nothing')
        self.labela.setGeometry(100,200,350,30)
        self.labela.setFont(QFont('Arial',15))
        self.labela.show()

    def radio_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.labela.setText('You selected: '+radio_button.text())

app = QApplication(sys.argv)
window = AnotherWindow()
window.show()

app.exec_()
