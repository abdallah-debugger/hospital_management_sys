from tkinter import Frame,Menu,Button,PhotoImage,LEFT,TOP,X,FLAT

class ToolBar:

    def __init__(self,window):
        appointment = PhotoImage(file='./icons/schedule.png')
        medcine = PhotoImage(file='./icons/clinic.png')
        billing = PhotoImage(file='./icons/invoice.png')
        report = PhotoImage(file='./icons/report.png')
        lock = PhotoImage(file='./icons/lock.png')
        exit = PhotoImage(file='./icons/exit.png')
        tool_frame = Frame(window, width=1920,height=50, bg='pink')

        tool_frame.pack()
