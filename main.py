from tkinter import *
import menu_bar


class Application:

    def __init__(self):
        self.window = Tk()
        self.window.title = 'Hospital Management System'
        self.window.geometry('1500x820+0+0')
        self.window.resizable(width=False, height=False)

        mb = menu_bar.MenuBar(self.window)

        self.window.mainloop()

Application()