import tkinter as tk

from models import constants as csts
from models.my_frame import MyFrame


class HomeFrame(MyFrame):
    def __init__(self,title="My Dope Stock App",geometry=csts.HOME_GEOM):
        super().__init__(title=title,geometry=geometry)
        self.viewstks_flag = False
        
        #produce left frame for buttons to go into
        self.left_frame = tk.Frame(master=self.root,width=280,height=csts.HOME_WINDOW_HEIGHT)
        self.left_frame.configure(bg=csts.BG_COLOR)
        self.left_frame.pack(side="left")

        #btn 1 - user to view stocks
        self.btn_view_stocks = tk.Button(master=self.left_frame,text="Lookup Charts",
                                         font=("Arial",12),
                                         width=csts.HOME_LFT_FR_BTN_WIDTH,
                                         height=csts.HOME_LFT_FR_BTN_HEIGHT,
                                         bg=csts.BG_COLOR,
                                         fg=csts.FG_COLOR,
                                         activebackground=csts.MY_GREEN,
                                         command=self.view_stks_clicked)
        self.btn_view_stocks.place(relx=0.5,rely=0,anchor=tk.N)

        self.root.mainloop()

    def view_stks_clicked(self):
        self.viewstks_flag = True
        self.root.destroy()