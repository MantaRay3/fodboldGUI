# importing tkinter module
from tkinter import *
from tkinter import messagebox


class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")
        Label(self.worstWindow, text="De værste betalere").pack()

#TODO:    showreverse list[:3] in table
        messagebox.showerror(parent=self.worstWindow, title="todo!", message="we're working on it")
#TODO: find a way to show bottom payers
