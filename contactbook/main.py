
from tkinter import *
import datetime
from mycontacts import MyContact
from AddContact import createContact
from aboutme import aboutMe
from PIL import Image, ImageTk


date = datetime.datetime.now()


class Application:
    def __init__ (self, master):
        self.master = master

        ## Frames
        self.top = Frame(master, height = 140, bg = 'white')
        self.top.pack(fill = X)
    
        self.bottom = Frame(master, height = 380, bg = '#000000')
        self.bottom.pack(fill = X)

        # Top Frame designing 
        self.top_image = PhotoImage(file = "icons/contactbook.png", height = 75, width = 60 )
        self.top_image_label = Label(self.top, image = self.top_image, bg = "white")
        self.top_image_label.place(x = 100, y = 30)

        self.heading = Label(self.top, text = "My Contact Book", font = "arial 25 bold", bg = "white", fg = "#000000")
        self.heading.place(x = 200, y = 40)
        ## Adding Date:
        self.top_date = Label(self.top, text = date.strftime('%d %B,%Y'), bg = "white", font = "arial 10 bold")
        self.top_date.place(x = 500, y = 100)

        ## button1 - view contacts
        self.view_button = Button(self.bottom, text = " View Contacts ", bg = "white", fg = 'black', font = "arial 15 bold", width = 15, command = self.view_contacts, activebackground = "#03fcf8")
        self.view_button.place(x = 400, y = 75)
        
        ## button2 - add contacts
        self.add_button = Button(self.bottom, text = " Add Contacts ", bg = "white", fg = "black", font = "arial 15 bold", width = 15, command = self.add_contact, activebackground = "#03fcf8")
        self.add_button.place(x = 400, y = 170)
        
        ## button3 - about us
        self.about_us = Button(self.bottom, text = " About Me", bg = "white", fg = "black", font = "arial 15 bold", width = 15, command = self.about_me, activebackground = "#03fcf8")
        self.about_us.place(x = 400, y = 265)

        ## Adding Background Image

        self.bg = ImageTk.PhotoImage(file = "icons/back1.jpg")
        background = Label(self.bottom, image = self.bg , bg = "black" ).place(x = 20, y = 0, relheight = 1)


    def view_contacts(self):
        contact = MyContact()
    
    def add_contact(self):
        add = createContact()

    def about_me(self):
        my_info = aboutMe()

def main():
    root = Tk()
    app = Application(root)
    root.title("Contact Book App")
    root.geometry("650x550+350+150")
    root.resizable(False, False)
    root.mainloop()




if __name__ == '__main__':
    main()