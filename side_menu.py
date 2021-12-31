from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QSize, QCoreApplication
from PyQt5.QtWidgets import *
import sys


class SideMenu():
    def __init__(self, parent,layout):
        self.left_menu_Tree = QTreeWidget(parent)
        self.left_menu_Tree.setColumnCount(1)
        self.left_menu_Tree.setMinimumSize(QtCore.QSize(200, 0))
        self.left_menu_Tree.setMaximumSize(QtCore.QSize(300, 16777215))
        self.left_menu_Tree.setStyleSheet("QTreeWidget{\n"
                                          "    border: None;\n"
                                          "}")
        self.left_menu_Tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.left_menu_Tree.setObjectName("left_menu_Tree")

        # header = QLabel(text='MENU')
        self.left_menu_Tree.setHeaderLabel("MENU")

        # For the sake of use in the future

        # When creating the parent "General", we passed the TreeWidget into it as the parent
        general = QTreeWidgetItem(self.left_menu_Tree,['General'])
        self.left_menu_Tree.addTopLevelItem(general)  # This is used to create an item that has sub children

        # There are two ways in which we can add a child to the above parent

        # We can create a TreeWidgetItem and manually add the the item to the parent 'x' using the addChild method.
        # Note that the string is passed into a list, this gave us a lot of headache at first.
        general_1 = QTreeWidgetItem(['General Settings'])
        general.addChild(general_1)

        # An alternative is to pass the parent and the string in the TreeWidgetItem instantiation. Then we would not need
        # to add the addChild method.
        general_2 = QTreeWidgetItem(general,["OP Settings Master"])
        general_3 = QTreeWidgetItem(general,["General Voucher"])
        general_4 = QTreeWidgetItem(general,["Work Shop Form"])
        general_5 = QTreeWidgetItem(general,["Photo Scanning Utility"])


        # 2
        patient_info = QTreeWidgetItem(self.left_menu_Tree,["Patient Information"])
        patient_info_1 = QTreeWidgetItem(patient_info,["Patient Registration"])
        patient_info_2 = QTreeWidgetItem(patient_info,["Patient Info Sheet"])
        patient_info_3 = QTreeWidgetItem(patient_info,["Patient Deposit Register"])

        # 3
        op_dept = QTreeWidgetItem(self.left_menu_Tree,["Out-Patient Department"])
        op_dept_1 = QTreeWidgetItem(op_dept,["OP Resgister"])
        op_dept_2 = QTreeWidgetItem(op_dept,["Discharge Register"])
        op_dept_3 = QTreeWidgetItem(op_dept,["Follow-up Visit Register"])
        op_dept_4 = QTreeWidgetItem(op_dept,["Patient Diagnosis Details"])
        op_dept_5 = QTreeWidgetItem(op_dept,["Doctors Comments and Recommendation"])
        op_dept_6 = QTreeWidgetItem(op_dept,["Patient Prescription Details"])
        op_dept_7 = QTreeWidgetItem(op_dept,["Patient Transaction"])
        op_dept_8 = QTreeWidgetItem(op_dept,["Patient Transaction Utility"])
        op_dept_9 = QTreeWidgetItem(op_dept,["Medical Record Management"])

        # 4
        ip_dept = QTreeWidgetItem(self.left_menu_Tree,["In-Patient Department"])
        ip_dept_1 = QTreeWidgetItem(ip_dept,["In-Patient Registration"])

        # 5
        masters = QTreeWidgetItem(self.left_menu_Tree,["Masters"])
        masters_1 = QTreeWidgetItem(masters,["Service Master"])
        masters_2 = QTreeWidgetItem(masters,["Account Head Register"])
        masters_3 = QTreeWidgetItem(masters,["Expense Master"])
        masters_4 = QTreeWidgetItem(masters,["Diagnosis Master"])
        masters_5 = QTreeWidgetItem(masters,["Investigation Master"])
        masters_6 = QTreeWidgetItem(masters,["Doctor Specialization Master"])
        masters_7 = QTreeWidgetItem(masters,["Resource Master"])

        # 6
        accounts = QTreeWidgetItem(self.left_menu_Tree,["Accounts"])
        accounts_1 = QTreeWidgetItem(accounts,["Patients Billing"])

        # 7
        reports = QTreeWidgetItem(self.left_menu_Tree,["Reports"])
        reports_1 = QTreeWidgetItem(reports,["Reports"])
        reports_2 = QTreeWidgetItem(reports,["Accounts Reports"])

        # 8
        admin = QTreeWidgetItem(self.left_menu_Tree,["Administration"])
        admin_1 = QTreeWidgetItem(admin,["Company Profile Setting"])
        admin_2 = QTreeWidgetItem(admin,["Branch Profile Setting"])
        admin_3 = QTreeWidgetItem(admin,["User Rights Assignment"])
        admin_4 = QTreeWidgetItem(admin,["Prescription Template Master"])
        admin_5 = QTreeWidgetItem(admin,["Expense Charge Settings"])

        # 9
        appointments = QTreeWidgetItem(self.left_menu_Tree,["Appointments"])
        appointments_1 = QTreeWidgetItem(appointments,["Appointments"])
        appointments_2 = QTreeWidgetItem(appointments,["Appointment Visit Register"])

        # 10
        emp_info = QTreeWidgetItem(self.left_menu_Tree,["Employee Information"])
        emp_info_1 = QTreeWidgetItem(emp_info,["Employee Registration"])
        emp_info_2 = QTreeWidgetItem(emp_info,["Employee Account Master"])
        emp_info_3 = QTreeWidgetItem(emp_info,["Bank Master"])
        emp_info_4 = QTreeWidgetItem(emp_info,["Bank Account Register"])
        emp_info_5 = QTreeWidgetItem(emp_info,["Bank Account Transaction"])
        emp_info_6 = QTreeWidgetItem(emp_info,["Employee Designation Master"])
        emp_info_7 = QTreeWidgetItem(emp_info,["Employee Shift Master"])
        emp_info_8 = QTreeWidgetItem(emp_info,["Employee Account Transaction"])
        emp_info_9 = QTreeWidgetItem(emp_info,["User Maintenance"])
        emp_info_10 = QTreeWidgetItem(emp_info,["Employee Attendance Register"])

        # 11
        doctor_dets = QTreeWidgetItem(self.left_menu_Tree,["Doctor Details"])
        doctor_dets_1 = QTreeWidgetItem(doctor_dets,["Doctor Master"])
        doctor_dets_2 = QTreeWidgetItem(doctor_dets,["Doctor Duty Timings Register"])
        doctor_dets_3 = QTreeWidgetItem(doctor_dets,["Doctor Leave Register"])
        doctor_dets_4 = QTreeWidgetItem(doctor_dets,["Refer In Doctor Master"])

        # 12
        insurance_sect = QTreeWidgetItem(self.left_menu_Tree,["Insurance Section"])
        insurance_sect_1 = QTreeWidgetItem(insurance_sect,["Insurance Claim"])
        insurance_sect_2 = QTreeWidgetItem(insurance_sect,["Insurance Master"])

        layout.addWidget(self.left_menu_Tree, 1, 0, 1, 1)


        # __sortingEnabled = self.left_menu_Tree.isSortingEnabled()
        # self.left_menu_Tree.setSortingEnabled(False)
        #
        # self.left_menu_Tree.setSortingEnabled(__sortingEnabled)