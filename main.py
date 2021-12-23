from tkinter import *
import menu_bar
import tool_bar

# Colors to use
color1 = '#FF9999'
color2 = '#FFEBCC'
color3 = '#FBFFE2'
color4 = '#FFAFAF'

class Application:

    def __init__(self):
        self.window = Tk()
        self.window.title = 'Hospital Management System'
        self.window.geometry('1500x820+0+0')
        self.window.resizable(width=False, height=False)

        mb = menu_bar.MenuBar(self.window)
        tb = tool_bar.ToolBar(self.window)

        self.window.mainloop()

Application()