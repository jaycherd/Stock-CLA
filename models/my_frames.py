import tkinter as tk
import models.constants as constants #a file
from models.utils import create_longterm_plots,create_medterm_plots #fxns


class MyFrame:
    def __init__(self,title="cool title",geometry="500x500"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)


class ChooserFrame(MyFrame): # inherits from MyFrame
    def __init__(self,title="Stock Chooser",geometry="500x500"):
        super().__init__(title=title,geometry=geometry)
        self.sym_var = tk.StringVar()
        self.short_term_flag = False
        self.med_term_flag = False
        self.long_term_flag = False
        self.short_btn = None
        self.med_btn = None
        self.long_btn = None
    
    def draw(self):
        tmptxt = "Enter Stock Symbol"
        tmptxt_formatted = tmptxt.ljust(constants.CHSR_COL_WIDTH)
        lbl = tk.Label(self.root, text=tmptxt_formatted, font = ("Arial",12))
        lbl.grid(column = 0, row = 0)
        # get input using entry class
        sym_entry = tk.Entry(self.root, textvariable=self.sym_var, width=constants.CHSR_COL_WIDTH)
        # use the grid function as usual to add it to the window
        sym_entry.grid(column=1, row=0)
        sym_entry.focus()
        sym_entry.bind('<Return>',self.enter_pressed)

        # short_str = "Short Term"
        # short_str.ljust(constants.BUTTON_STR_WIDTH)
        # self.short_btn = tk.Button(self.root,text=short_str,bg="grey",fg="blue",command=self.short_clicked,width=constants.CHSR_COL_WIDTH)
        med_str = "Medium Term"
        med_str.ljust(constants.BUTTON_STR_WIDTH)
        self.med_btn = tk.Button(self.root,text=med_str,bg="grey",fg="blue",command=self.med_clicked,width=constants.CHSR_COL_WIDTH)
        long_str = "Long Term"
        long_str.ljust(constants.BUTTON_STR_WIDTH)
        self.long_btn = tk.Button(self.root,text=long_str,bg="grey",fg="blue",command=self.long_clicked,width=constants.CHSR_COL_WIDTH)

        # self.short_btn.grid(row=1,column=0,pady=12)
        self.med_btn.grid(row=1,column=0,pady=12)
        self.long_btn.grid(row=1,column=1,pady=12)

        self.root.mainloop()

    def enter_pressed(self,event:'tk.Event'):
        tmp_symbol = self.sym_var.get()
        symbol = ""
        for char in tmp_symbol:
            symbol += char.upper()
        if self.short_term_flag:
            create_longterm_plots(symbol=symbol)
        if self.med_term_flag:
            create_medterm_plots(symbol=symbol)
        if self.long_term_flag:
            create_longterm_plots(symbol=symbol)

    def short_clicked(self):
        self.short_term_flag = True
        self.short_btn.destroy()
        return

    def med_clicked(self):
        self.med_term_flag = True
        self.med_btn.destroy()
        return
    
    def long_clicked(self):
        self.long_term_flag = True
        self.long_btn.destroy()
        return
