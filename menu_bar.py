from PyQt5.QtWidgets import QAction

class MenuBar():

    def __init__(self,parent):
        bar = parent.menuBar()

        # System Menu
        system = bar.addMenu("System")

        hide = QAction('Show/Hide Shortcut',parent)
        hide.setShortcut('Ctrl+F12')
        system.addAction(hide)

        lock = QAction('Lock',parent)
        lock.setShortcut('Ctrl+F7')
        system.addAction(lock)

        log_off = QAction('Log off',parent)
        log_off.setShortcut('Ctrl+F9')
        system.addAction(log_off)

        quit = QAction('Exit',parent)
        quit.setShortcut('Ctrl+F8')
        system.addAction(quit)

        # Walz_Options Menu
        walz_options = bar.addMenu("Walz Clinic Options")

        general = walz_options.addMenu('General')
        general_settings = QAction('General Setting',parent)
        general.addAction(general_settings)
        general_master = QAction('OP Settings Master',parent)
        general.addAction(general_master)
        general_voucher = QAction('General Voucher',parent)
        general.addAction(general_voucher)
        general_workshop = QAction('Work Shop Form',parent)
        general.addAction(general_workshop)
        general_scanning = QAction('Photo Scanning Utility',parent)
        general.addAction(general_scanning)


        patient_info = walz_options.addMenu('Patient Information')

        # Walz_Options - Out Patient
        o_patient_dept = walz_options.addMenu('Out-Patient Department')

        op_register = QAction('OP Register', parent)
        o_patient_dept.addAction(op_register)

        op_discharge = QAction('Discharge Register', parent)
        o_patient_dept.addAction(op_discharge)

        op_followup = QAction('Follow-up Visit Register', parent)
        o_patient_dept.addAction(op_followup)

        op_diagnosis = QAction('Patient Diagnosis Details', parent)
        o_patient_dept.addAction(op_diagnosis)

        op_recommendation = QAction('Doctors Comments And Recommendation', parent)
        o_patient_dept.addAction(op_recommendation)

        op_prescription = QAction('Patient Prescription Details', parent)
        o_patient_dept.addAction(op_prescription)

        op_transaction = QAction('Patient Transaction', parent)
        o_patient_dept.addAction(op_transaction)

        op_utility = QAction('Patient Transaction Utility', parent)
        o_patient_dept.addAction(op_utility)

        op_record = QAction('Medical Record Management', parent)
        o_patient_dept.addAction(op_record)


        # Walz_Options - In Patient
        i_patient_dept = walz_options.addMenu('In-Patient Department')
        ip_register = QAction('Inpatient Registration',parent)
        i_patient_dept.addAction(ip_register)

        # Walz_Options - Master
        masters = walz_options.addMenu('Masters')
        accounts = walz_options.addMenu('Accounts')
        reports = walz_options.addMenu('Reports')
        admin = walz_options.addMenu('Administration')
        appointments = walz_options.addMenu('Appointments')
        emp_info = walz_options.addMenu('Employee Information')
        doctor_details = walz_options.addMenu('Doctor Details')
        insurance_sec = walz_options.addMenu('Insurance Section')

        utility = bar.addMenu("Utility")
        about = bar.addMenu("About/Help")
        exit = bar.addMenu("Exit")