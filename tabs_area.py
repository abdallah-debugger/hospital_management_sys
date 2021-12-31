from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QPoint,\
    QRect, QSize, QUrl, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont,\
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,\
    QRadialGradient
from PyQt5.QtWidgets import *


class TabsArea:

    def __init__(self,parent,layout):
        self.right_tabwidget = QTabWidget(parent)
        # self.right_tabwidget.setObjectName("right_tabwidget")
        self.right_tabwidget.setMinimumSize(QSize(654, 0))
        self.right_tabwidget.currentChanged.connect(self.tabChanged)
        self.tab_1 = QWidget()
        # self.tab.setObjectName("tab")
        self.right_tabwidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        # self.tab_2.setObjectName("tab_2")
        self.right_tabwidget.addTab(self.tab_2, "")
        layout.addWidget(self.right_tabwidget, 1, 1, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.right_tabwidget.setTabText(self.right_tabwidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.right_tabwidget.setTabText(self.right_tabwidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

    def tabChanged(self):
        print(f'Tab was changed to : {self.right_tabwidget.currentIndex()}')

    def changeTab(self):
        # setTabText(index of the tab, tab name)
        self.right_tabwidget.setTabText(0,'Alrighty')