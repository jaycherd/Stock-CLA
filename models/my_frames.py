import tkinter as tk
from . import constants


class MyFrame:
    def __init__(self,title="cool title",geometry="500x500"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)


class ChooserFrame(MyFrame): # inherits from MyFrame
    def __init__(self,title="Stock Chooser",geometry="500x500"):
        super().__init__(title=title,geometry=geometry)
    
    def draw(self):
        tmptxt = "Enter Stock Symbol"
        tmptxt_formatted = tmptxt.ljust(constants.CHSR_COL_WIDTH)
        lbl = tk.Label(self.root, text=tmptxt_formatted, font = ("Arial",12))
        lbl.grid(column = 0, row = 0)
        # get input using entry class
        sym_var = tk.StringVar()
        sym_entry = tk.Entry(self.root, textvariable=sym_var, width=constants.CHSR_COL_WIDTH)
        # use the grid function as usual to add it to the window
        sym_entry.grid(column=1, row=0)
        sym_entry.focus()
        sym_entry.bind('<Return>',self.enter_pressed)
        self.root.mainloop()

    def enter_pressed(self,event:'tk.Event'):
        print(type(event))