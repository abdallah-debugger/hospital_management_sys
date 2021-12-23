import tkinter

class MenuBar:
    def __init__(self,window):
        # Create and display the main menu bar
        menuBar = tkinter.Menu(window,background='blue',fg='red')
        # menuBar.config()


        # System Menu
        systemMenu = tkinter.Menu(menuBar, tearoff=False)
        systemMenu.add_command(label="Show / Hide Shortcut Menu")
        systemMenu.add_command(label="Lock")
        systemMenu.add_command(label="Log Off")
        systemMenu.add_command(label="Exit")
        menuBar.add_cascade(menu=systemMenu, label="System")

        # Wale's Clinic Options Menu
        clinicOptionsMenu = tkinter.Menu(menuBar, tearoff=False)
        # General submenu
        generalSub = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        generalSub.add_command(label='General Settings')
        generalSub.add_command(label='OP Settings Master')
        generalSub.add_command(label='General Voucher')
        generalSub.add_command(label='Work Shop Form')
        generalSub.add_command(label='Photo Scanning Utility')
        clinicOptionsMenu.add_cascade(menu=generalSub, label='General')

        # Patients Information submenu
        patientsInfo = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        patientsInfo.add_command(label='Patient Registration')
        patientsInfo.add_command(label='Patient Info Sheet')
        patientsInfo.add_command(label='Patients Deposit Register')
        clinicOptionsMenu.add_cascade(menu=patientsInfo, label='Patients Information')

        # Outpatient Department Submenu
        outPatient = tkinter.Menu(clinicOptionsMenu,tearoff=False)
        outPatient.add_command(label='OP Register')
        outPatient.add_command(label='Discharge Register')
        outPatient.add_command(label='Followup Visit Register')
        outPatient.add_command(label='Patient Diagnosis Register')
        outPatient.add_command(label='Patient Diagnosis Details')
        outPatient.add_command(label='Doctors Comments and Recommendations')
        outPatient.add_command(label='Patient Prescription Details')
        outPatient.add_command(label='Patient Transaction')
        outPatient.add_command(label='Patient Transaction Utility')
        outPatient.add_command(label='Medical Record Management')
        clinicOptionsMenu.add_cascade(menu=outPatient,label='Outpatient Department')

        # Inpatient Department Submenu
        inPatient = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        inPatient.add_command(label='Inpatient Registration')
        clinicOptionsMenu.add_cascade(menu=inPatient, label='Inpatient Department')

        # Masters Submenu
        masters = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        masters.add_command(label='Service Master')
        masters.add_command(label='Account Head Register')
        masters.add_command(label='Expense Master')
        masters.add_command(label='Diagnosis Master')
        masters.add_command(label='Investigation Master')
        masters.add_command(label='Doctor Specialization Master')
        masters.add_command(label='Resource Master')
        clinicOptionsMenu.add_cascade(menu=masters, label='Masters')

        # Account Submenu
        account = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        account.add_command(label='Patient Billings')
        clinicOptionsMenu.add_cascade(menu=account, label='Account')

        # Reports Submenu
        reports = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        reports.add_command(label='Reports')
        reports.add_command(label='Account Reports')
        clinicOptionsMenu.add_cascade(menu=reports, label='Reports')

        # Administration Submenu
        administration = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        administration.add_command(label='Company Profile Settings')
        administration.add_command(label='Branch Profile Settings')
        administration.add_command(label='User Rights Assignment')
        administration.add_command(label='Prescription Template Master')
        administration.add_command(label='Expense Charge Settings')
        clinicOptionsMenu.add_cascade(menu=administration, label='Administration')

        # Appointments Submenu
        appointments = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        appointments.add_command(label='Appointments')
        appointments.add_command(label='Appointments Visit Register')
        clinicOptionsMenu.add_cascade(menu=appointments, label='Appointments')

        # Employee Information
        empInfo = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        empInfo.add_command(label='Employee Registration')
        empInfo.add_command(label='Employee Account Master')
        empInfo.add_command(label='Bank Master')
        empInfo.add_command(label='Bank Account Register')
        empInfo.add_command(label='Bank Account Transaction')
        empInfo.add_command(label='Employee Designation Master')
        empInfo.add_command(label='Employee Shift Master')
        empInfo.add_command(label='Employee Account Transaction')
        empInfo.add_command(label='User Maintenance')
        empInfo.add_command(label='Employee Attendance Register')
        clinicOptionsMenu.add_cascade(menu=empInfo, label='Employee Information')

        # Doctor Details Submenu
        doctorDetails = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        doctorDetails.add_command(label='Doctor Master')
        doctorDetails.add_command(label='Doctor Duty Timings Register')
        doctorDetails.add_command(label='Doctor Leave Register')
        doctorDetails.add_command(label='Refer In Doctor Master')
        clinicOptionsMenu.add_cascade(menu=doctorDetails, label='Doctor Details')

        # Insurance Section Submenu
        insuranceSection = tkinter.Menu(clinicOptionsMenu, tearoff=False)
        insuranceSection.add_command(label='Insurance Claim')
        insuranceSection.add_command(label='Insurance Master')
        clinicOptionsMenu.add_cascade(menu=insuranceSection, label='Insurance Section')
        menuBar.add_cascade(menu=clinicOptionsMenu, label="Wale's Clinic Options")

        # Utitlty Menu
        utilityMenu = tkinter.Menu(menuBar, tearoff=False)
        utilityMenu.add_command(label='Password Management')
        menuBar.add_cascade(menu=utilityMenu, label='Utility')

        # About Menu
        aboutMenu = tkinter.Menu(menuBar, tearoff=False)
        aboutMenu.add_command(label='About')
        aboutMenu.add_command(label='Help')
        aboutMenu.add_command(label='Update')
        menuBar.add_cascade(menu=aboutMenu, label='About/Help')

        # Exit Menu
        menuBar.add_command(label='Exit',command=window.quit)


        window.config(menu=menuBar)