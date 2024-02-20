# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()

#        img = ImageTk.PhotoImage(Image.open("assets/img/cyl.png"))
#        panel = Label(self.listWindow, image=img)
#        panel.image = img
#        panel.pack(side="bottom", fill="both", expand="yes")

        #TODONE: show list in table
        #TODO: Get it into the list window
        debt=self.master.target
        for key, value in self.master.fodboldtur.items():
            if value == debt:
                print(f'{key} har betalt det hele')
            else:
                print(f' {key} har betalt {value} og mangler {debt - value}')

