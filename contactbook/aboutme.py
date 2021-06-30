from tkinter import * 
import datetime
from tkinter import messagebox


date = datetime.datetime.now()

class aboutMe(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+350+150")
        self.title("Contact's Information")
        self.resizable(False,False)

        self.top = Frame(self, height = 140, bg = 'white')
        self.top.pack(fill = X)
    
        self.bottom = Frame(self, height = 380, bg = '#000000')
        self.bottom.pack(fill = X)

        # Top Frame designing 
        self.top_image = PhotoImage(file = "icons/mycontact3.png", height = 75, width = 80 )
        self.top_image_label = Label(self.top, image = self.top_image, bg = "white")
        self.top_image_label.place(x = 100, y = 30)

        self.heading = Label(self.top, text = "About Me ", font = "arial 25 bold", bg = "white", fg = "#000000")
        self.heading.place(x = 210, y = 40)

        # Adding date
        self.top_date = Label(self.top, text = date.strftime('%d %B,%Y'), bg = "white", font = "arial 10 bold")
        self.top_date.place(x = 500, y = 100)

        # Button

        self.close_button = Button(self.bottom, text = 'Back', width = 18, font = 'arial 12 bold', bg = '#cf0a0a', fg = 'black', command = self.function)
        self.close_button.place(x = 450, y = 332)

    def function(self):
        self.destroy()