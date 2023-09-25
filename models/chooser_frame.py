import tkinter as tk

from models import constants
from models.my_frame import MyFrame
from models.utils import create_plots

class ChooserFrame(MyFrame): # inherits from MyFrame
    def __init__(self,title="Stock Chooser",geometry=""):
        super().__init__(title=title,geometry="")
        self.sym_var = tk.StringVar()


    def draw(self):
        tmptxt = "Enter Stock Symbol"
        tmptxt_formatted = tmptxt.ljust(constants.CHSR_COL_WIDTH)
        lbl = tk.Label(self.root, text=tmptxt_formatted, font = ("Arial",12))
        lbl.grid(column = 0, row = 0,padx=10,pady=10)
        # get input using entry class
        sym_entry = tk.Entry(self.root, textvariable=self.sym_var, width=constants.CHSR_COL_WIDTH)
        # use the grid function as usual to add it to the window
        sym_entry.grid(column=1, row=0,padx=10,pady=10)
        sym_entry.focus()
        sym_entry.bind('<Return>',self.enter_pressed)

        self.root.mainloop()

    def enter_pressed(self,event:'tk.Event'):
        del event #how pylint says to deal with an unused var
        tmp_symbol = self.sym_var.get()
        symbol = ""
        for char in tmp_symbol:
            symbol += char.upper()
        create_plots(symbol)
