import tkinter

class MenuBar:
    def __init__(self,window):
        # Create and display the main menu bar
        menuBar = tkinter.Menu(window)

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

        clinicOptionsMenu.add_command(label='Masters')
        clinicOptionsMenu.add_command(label='Account')
        clinicOptionsMenu.add_command(label='Reports')
        clinicOptionsMenu.add_command(label='Administration')
        clinicOptionsMenu.add_command(label='Appointments')
        clinicOptionsMenu.add_command(label='Employee Information')
        clinicOptionsMenu.add_command(label='Doctor Details')
        clinicOptionsMenu.add_command(label='Insurance Section')

        menuBar.add_cascade(menu=clinicOptionsMenu, label="Wale's Clinic Options")


        utilityMenu = tkinter.Menu(menuBar, tearoff=False)
        utilityMenu.add_command(label='Password Management')
        menuBar.add_cascade(menu=utilityMenu, label='Utility')




        aboutMenu = tkinter.Menu(menuBar, tearoff=False)

        aboutMenu.add_command(label='About')
        aboutMenu.add_command(label='Help')
        aboutMenu.add_command(label='Update')
        menuBar.add_cascade(menu=aboutMenu, label='About/Help')

        window.config(menu=menuBar)