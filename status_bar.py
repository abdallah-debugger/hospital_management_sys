class StatusBar:

    def __init__(self):
        self.empty_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.empty_statusbar.setObjectName("empty_statusbar")
        MainWindow.setStatusBar(self.empty_statusbar)