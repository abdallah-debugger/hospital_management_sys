from PyQt5.QtWidgets import *


class StatusBar:

    def __init__(self,parent):
        self.statusbar = QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        user = 'Walz Admin'
        user_label = QLabel(f'User: {user}')
        self.statusbar.addPermanentWidget(user_label,stretch=1)

        user_mode = 'Administrator'
        mode_label = QLabel(f'Mode: {user_mode}')
        self.statusbar.addPermanentWidget(mode_label,stretch=1)

        date = '28-12-2021'
        date_label = QLabel(f'System Date: {date}')
        self.statusbar.addPermanentWidget(date_label,stretch=1)

        time = '13:45:55'
        time_label = QLabel(f'System Time: {time}')
        self.statusbar.addPermanentWidget(time_label,stretch=1)

        # self.statusbar.setStyleSheet('QStatusBar{padding:15px;}')