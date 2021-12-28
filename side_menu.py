from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QSize, QCoreApplication
from PyQt5.QtWidgets import *
import sys


class SideMenu():
    def __init__(self, parent,layout):
        self.left_menu_Tree = QTreeWidget(parent)
        self.left_menu_Tree.setMinimumSize(QtCore.QSize(200, 0))
        self.left_menu_Tree.setMaximumSize(QtCore.QSize(300, 16777215))
        self.left_menu_Tree.setStyleSheet("QTreeWidget{\n"
                                          "    border: None;\n"
                                          "}")
        self.left_menu_Tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.left_menu_Tree.setObjectName("left_menu_Tree")
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        layout.addWidget(self.left_menu_Tree, 1, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.left_menu_Tree.headerItem().setText(0, _translate("MainWindow", "School"))
        __sortingEnabled = self.left_menu_Tree.isSortingEnabled()
        self.left_menu_Tree.setSortingEnabled(False)
        self.left_menu_Tree.topLevelItem(0).setText(0, _translate("MainWindow", "School Items"))
        self.left_menu_Tree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Ruler"))
        self.left_menu_Tree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Pencil"))
        self.left_menu_Tree.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Biro"))
        self.left_menu_Tree.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Eraser"))
        self.left_menu_Tree.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "Divider"))
        self.left_menu_Tree.topLevelItem(0).child(5).setText(0, _translate("MainWindow", "Mathset"))
        self.left_menu_Tree.topLevelItem(1).setText(0, _translate("MainWindow", "School Members"))
        self.left_menu_Tree.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Cleaners"))
        self.left_menu_Tree.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Teacher"))
        self.left_menu_Tree.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Security"))
        self.left_menu_Tree.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "Head master"))
        self.left_menu_Tree.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "Baddo"))
        self.left_menu_Tree.topLevelItem(2).setText(0, _translate("MainWindow", "School Facilites"))
        self.left_menu_Tree.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Swings"))
        self.left_menu_Tree.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Toilets"))
        self.left_menu_Tree.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "Labs"))
        self.left_menu_Tree.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "Storage"))
        self.left_menu_Tree.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "Computer Lab"))
        self.left_menu_Tree.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "Home Econmic Lab"))
        self.left_menu_Tree.setSortingEnabled(__sortingEnabled)