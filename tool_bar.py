from tkinter import Frame,Menu,Button,PhotoImage,LEFT,TOP,X,FLAT

class ToolBar:

    def __init__(self,window):
        appointment = PhotoImage(file='./icons/schedule.png',width=30,height=30)
        medcine = PhotoImage(file='./icons/clinic.png',width=30,height=30)
        billing = PhotoImage(file='./icons/invoice.png')
        report = PhotoImage(file='./icons/report.png')
        lock = PhotoImage(file='./icons/lock.png')
        exit = PhotoImage(file='./icons/exit.png')
        tool_frame = Frame(window, width=1920,height=50, bg='pink')
        appointment_btn = Button(tool_frame,text='Appointment',image=appointment,compound=TOP)
        appointment_btn.pack()
        medicine_btn = Button(tool_frame, text='Medicine', image=medcine, compound=TOP)
        medicine_btn.pack()

        tool_frame.pack()
