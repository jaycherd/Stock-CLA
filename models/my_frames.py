import tkinter as tk

class MyFrame:
    def __init__(self,title="cool title",geometry="500x500"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)


class ChooserFrame(MyFrame): # inherits from MyFrame
    def __init__(self,title="Stock Chooser",geometry="500x500"):
        super().__init__(title=title,geometry=geometry)
    
    def draw(self):
        self.root.mainloop()