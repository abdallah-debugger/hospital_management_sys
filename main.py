import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow
from PyQt5.QtGui import QIcon
import menu_bar

class HospitalMgmt():

    def __init__(self):
        app = QApplication(sys.argv)

        # Window formating
        window = QMainWindow()
        window.setWindowTitle('Walz Hospital Mangement System')
        window.setWindowIcon(QIcon('./icons/clinic.png'))

        # window.setGeometry(200,200,300,200)


        menu_bar.MenuBar(window)

        window.show()
        app.exec_()

HospitalMgmt()