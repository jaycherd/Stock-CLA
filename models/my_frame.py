import tkinter as tk


class MyFrame:
    """parent class for my frames"""
    def __init__(self,title="cool title",geometry="500x500"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
