from PyQt5.QtWidgets import *
import sys


class SideMenu():
    def __init__(self, parent):
        super().__init__()

        # set the title of main window
        # self.setWindowTitle('Sidebar layout - www.luochang.ink')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        parent.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('1', parent)
        self.btn_2 = QPushButton('2', parent)
        self.btn_3 = QPushButton('3', parent)
        self.btn_4 = QPushButton('4', parent)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        parent.setCentralWidget(main_widget)

        # def ui1():
        #     main_layout = QVBoxLayout()
        #     main_layout.addWidget(QLabel('page 1'))
        #     main_layout.addStretch(5)
        #     main = QWidget()
        #     main.setLayout(main_layout)
        #     return main
        #
        # def ui2():
        #     main_layout = QVBoxLayout()
        #     main_layout.addWidget(QLabel('page 2'))
        #     main_layout.addStretch(5)
        #     main = QWidget()
        #     main.setLayout(main_layout)
        #     return main
        #
        # def ui3():
        #     main_layout = QVBoxLayout()
        #     main_layout.addWidget(QLabel('page 3'))
        #     main_layout.addStretch(5)
        #     main = QWidget()
        #     main.setLayout(main_layout)
        #     return main
        #
        # def ui4():
        #     main_layout = QVBoxLayout()
        #     main_layout.addWidget(QLabel('page 4'))
        #     main_layout.addStretch(5)
        #     main = QWidget()
        #     main.setLayout(main_layout)
        #     return main
        #
        # # add tabs
        # self.tab1 = ui1()
        # self.tab2 = ui2()
        # self.tab3 = ui3()
        # self.tab4 = ui4()
