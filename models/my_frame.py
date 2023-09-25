import tkinter as tk

from models import constants


class MyFrame:
    """parent class for my frames"""
    def __init__(self,title="cool title",geometry="500x500+200+200"):
        self.root = tk.Tk()
        # self.root.overrideredirect(True)
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.configure(bg=constants.BG_COLOR)
        self.root.resizable(width=True,height=True)
