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

        # 1
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 2
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 3
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 4
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)

        # 5
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 6
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)

        # 7
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 8
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 9
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 10
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 11
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        # 12
        item_0 = QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QTreeWidgetItem(item_0)
        item_1 = QTreeWidgetItem(item_0)

        layout.addWidget(self.left_menu_Tree, 1, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.left_menu_Tree.headerItem().setText(0, _translate("MainWindow", "MENU"))
        __sortingEnabled = self.left_menu_Tree.isSortingEnabled()
        self.left_menu_Tree.setSortingEnabled(False)
        # 1
        self.left_menu_Tree.topLevelItem(0).setText(0, _translate("MainWindow", "General"))
        self.left_menu_Tree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "General Settings"))
        self.left_menu_Tree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "OP Settings Master"))
        self.left_menu_Tree.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "General Voucher"))
        self.left_menu_Tree.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Work Shop Form"))
        self.left_menu_Tree.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "Photo Scanning Utility"))

        # 2
        self.left_menu_Tree.topLevelItem(1).setText(0, _translate("MainWindow", "Patient Information"))
        self.left_menu_Tree.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Patient Registration"))
        self.left_menu_Tree.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Patient Info Sheet"))
        self.left_menu_Tree.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Patient Deposit Register"))

        # 3
        self.left_menu_Tree.topLevelItem(2).setText(0, _translate("MainWindow", "Out-Patient Department"))
        self.left_menu_Tree.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "OP Resgister"))
        self.left_menu_Tree.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Discharge Register"))
        self.left_menu_Tree.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "Follow-up Visit Register"))
        self.left_menu_Tree.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "Patient Diagnosis Details"))
        self.left_menu_Tree.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "Doctors Comments and Recommendation"))
        self.left_menu_Tree.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "Patient Prescription Details"))
        self.left_menu_Tree.topLevelItem(2).child(6).setText(0, _translate("MainWindow", "Patient Transaction"))
        self.left_menu_Tree.topLevelItem(2).child(7).setText(0, _translate("MainWindow", "Patient Transaction Utility"))
        self.left_menu_Tree.topLevelItem(2).child(8).setText(0, _translate("MainWindow", "Medical Record Management"))

        # 4
        self.left_menu_Tree.topLevelItem(3).setText(0, _translate("MainWindow", "In-Patient Department"))
        self.left_menu_Tree.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "In-Patient Registration"))

        # 5
        self.left_menu_Tree.topLevelItem(4).setText(0, _translate("MainWindow", "Masters"))
        self.left_menu_Tree.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "Service Master"))
        self.left_menu_Tree.topLevelItem(4).child(1).setText(0, _translate("MainWindow", "Account Head Register"))
        self.left_menu_Tree.topLevelItem(4).child(2).setText(0, _translate("MainWindow", "Expense Master"))
        self.left_menu_Tree.topLevelItem(4).child(3).setText(0, _translate("MainWindow", "Diagnosis Master"))
        self.left_menu_Tree.topLevelItem(4).child(4).setText(0, _translate("MainWindow", "Investigation Master"))
        self.left_menu_Tree.topLevelItem(4).child(5).setText(0, _translate("MainWindow", "Doctor Specialization Master"))
        self.left_menu_Tree.topLevelItem(4).child(6).setText(0, _translate("MainWindow", "Resource Master"))

        # 6
        self.left_menu_Tree.topLevelItem(5).setText(0, _translate("MainWindow", "Accounts"))
        self.left_menu_Tree.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "Patients Billing"))

        # 7
        self.left_menu_Tree.topLevelItem(6).setText(0, _translate("MainWindow", "Reports"))
        self.left_menu_Tree.topLevelItem(6).child(0).setText(0, _translate("MainWindow", "Reports"))
        self.left_menu_Tree.topLevelItem(6).child(0).setText(0, _translate("MainWindow", "Accounts Reports"))

        # 8
        self.left_menu_Tree.topLevelItem(7).setText(0, _translate("MainWindow", "Administration"))
        self.left_menu_Tree.topLevelItem(7).child(0).setText(0, _translate("MainWindow", "Company Profile Setting"))
        self.left_menu_Tree.topLevelItem(7).child(1).setText(0, _translate("MainWindow", "Branch Profile Setting"))
        self.left_menu_Tree.topLevelItem(7).child(2).setText(0, _translate("MainWindow", "User Rights Assignment"))
        self.left_menu_Tree.topLevelItem(7).child(3).setText(0, _translate("MainWindow", "Prescription Template Master"))
        self.left_menu_Tree.topLevelItem(7).child(4).setText(0, _translate("MainWindow", "Expense Charge Settings"))

        # 9
        self.left_menu_Tree.topLevelItem(8).setText(0, _translate("MainWindow", "Appointments"))
        self.left_menu_Tree.topLevelItem(8).child(0).setText(0, _translate("MainWindow", "Appointments"))
        self.left_menu_Tree.topLevelItem(8).child(1).setText(0, _translate("MainWindow", "Appointment Visit Register"))

        # 10
        self.left_menu_Tree.topLevelItem(9).setText(0, _translate("MainWindow", "Employee Information"))
        self.left_menu_Tree.topLevelItem(9).child(0).setText(0, _translate("MainWindow", "Employee Registration"))
        self.left_menu_Tree.topLevelItem(9).child(1).setText(0, _translate("MainWindow", "Employee Account Master"))
        self.left_menu_Tree.topLevelItem(9).child(2).setText(0, _translate("MainWindow", "Bank Master"))
        self.left_menu_Tree.topLevelItem(9).child(3).setText(0, _translate("MainWindow", "Bank Account Register"))
        self.left_menu_Tree.topLevelItem(9).child(4).setText(0, _translate("MainWindow", "Bank Account Transaction"))
        self.left_menu_Tree.topLevelItem(9).child(5).setText(0, _translate("MainWindow", "Employee Designation Master"))
        self.left_menu_Tree.topLevelItem(9).child(6).setText(0, _translate("MainWindow", "Employee Shift Master"))
        self.left_menu_Tree.topLevelItem(9).child(7).setText(0, _translate("MainWindow", "Employee Account Transaction"))
        self.left_menu_Tree.topLevelItem(9).child(8).setText(0, _translate("MainWindow", "User Maintenance"))
        self.left_menu_Tree.topLevelItem(9).child(9).setText(0, _translate("MainWindow", "Employee Attendance Register"))

        # 11
        self.left_menu_Tree.topLevelItem(10).setText(0, _translate("MainWindow", "Doctor Details"))
        self.left_menu_Tree.topLevelItem(10).child(0).setText(0, _translate("MainWindow", "Doctor Master"))
        self.left_menu_Tree.topLevelItem(10).child(1).setText(0, _translate("MainWindow", "Doctor Duty Timings Register"))
        self.left_menu_Tree.topLevelItem(10).child(2).setText(0, _translate("MainWindow", "Doctor Leave Register"))
        self.left_menu_Tree.topLevelItem(10).child(3).setText(0, _translate("MainWindow", "Refer In Doctor Master"))

        # 12
        self.left_menu_Tree.topLevelItem(11).setText(0, _translate("MainWindow", "Insurance Section"))
        self.left_menu_Tree.topLevelItem(11).child(0).setText(0, _translate("MainWindow", "Insurance Claim"))
        self.left_menu_Tree.topLevelItem(11).child(1).setText(0, _translate("MainWindow", "Insurance Master"))




        self.left_menu_Tree.setSortingEnabled(__sortingEnabled)