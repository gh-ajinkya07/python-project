
from tkinter import * 
from tkinter import messagebox
from AddContact import createContact
from update_contact import updateContact
from display import displayContact
import datetime
import psycopg2

connection = psycopg2.connect(
                            
                            user = "postgres",
                            password = "passsql",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "contact_db" )
cursor = connection.cursor()


date = datetime.datetime.now()

class MyContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+350+150")
        self.title("My Contancts")
        self.resizable(False,False)

        self.top = Frame(self, height = 140, bg = 'white')
        self.top.pack(fill = X)
    
        self.bottom = Frame(self, height = 380, bg = '#000000')
        self.bottom.pack(fill = X)

        # Top Frame designing 
        self.top_image = PhotoImage(file = "icons/mycontact2.png", height = 75, width = 80 )
        self.top_image_label = Label(self.top, image = self.top_image, bg = "white")
        self.top_image_label.place(x = 100, y = 30)

        self.heading = Label(self.top, text = "My Contacts", font = "arial 25 bold", bg = "white", fg = "#000000")
        self.heading.place(x = 210, y = 40)

        # Adding date
        self.top_date = Label(self.top, text = date.strftime('%d %B,%Y'), bg = "white", font = "arial 10 bold")
        self.top_date.place(x = 500, y = 100)

        # Adding a List Box

        self.scroll = Scrollbar(self.bottom, orient = VERTICAL)
       
        self.listBox = Listbox(self.bottom, width = 30, height = 27, font = "arial 10")
        self.listBox.grid(row = 0, column = 0, padx = (40, 0))

        self.scroll.config(command = self.listBox.yview)
        self.listBox.config(yscrollcommand = self.scroll.set)

        self.scroll.grid(row = 0, column = 1, sticky = N+S)

        # Printing The data
        
        querry = "select * from addressbook order by person_id"
        cursor.execute(querry)
        persons = cursor.fetchall()
        self.listBox.insert(0,"                  ")
        count = 1
        for person in persons:
            self.listBox.insert(count, "   "+str(person[0]) + ".   " + person[1] + " " + person[2])
            count += 1


        # Adding button

        self.Addbutton = Button(self.bottom, text = "Add Contact", width = 12, font = "arial 12 bold", command = self.add_contact, activebackground = "#03fcf8")
        self.Addbutton.grid(row = 0, column = 2, padx = 80, pady = 40, sticky = N)

        self.Delbutton = Button(self.bottom, text = "Delete Contact", width = 12, font = "arial 12 bold", command = self.delete_contact, activebackground = "#03fcf8")
        self.Delbutton.grid(row = 0, column = 2, padx = 80, pady = 100, sticky = N)

        self.Updatebutton = Button(self.bottom, text = "Update Contact", width = 12, font = "arial 12 bold", command = self.update_contact, activebackground = "#03fcf8")
        self.Updatebutton.grid(row = 0, column = 2, padx = 80, pady = 160, sticky = N)

        self.Displaybutton = Button(self.bottom, text = "Display Contact", width = 12, font = "arial 12 bold", command = self.display, activebackground = "#03fcf8")
        self.Displaybutton.grid(row = 0, column = 2, padx = 80, pady = 220, sticky = N)

        self.close_button = Button(self.bottom, text = 'Back', width = 12, font = 'arial 12 bold', bg = '#e62525', fg = 'black', command = self.function)
        self.close_button.place(x = 350, y = 330)

    
    def add_contact(self):
        new_contact = createContact()
        self.destroy()

    def update_contact(self):

        try:
            selected_item = self.listBox.curselection()

            person = self.listBox.get(selected_item)
            person_id = person.split(".")[0]
            person_id = int(person_id)

            update_page = updateContact(person_id)
        except:
            messagebox.showerror("Error", "Please Select a Contact!")
    
    def display(self):

        try:
            selected_item = self.listBox.curselection()

            person = self.listBox.get(selected_item)
            person_id = person.split(".")[0]
            person_id = int(person_id)
            
            display_contact = displayContact(person_id)
        except:
            messagebox.showerror("Error", "Please Select a Contact!")

    def delete_contact(self):
        try:
            selected_item = self.listBox.curselection()

            person = self.listBox.get(selected_item)
            person_id = person.split(".")[0]
            person_id = int(person_id)

            result = messagebox.askquestion("Deleting a Contact", "Are you sure you want to delete this contact? This contact will be deleted and there is no going back !", icon='warning')

            if result == "yes":    
                try:
                    querry = "delete from addressbook where person_id = {}".format(person_id)
                    cursor.execute(querry)
                    connection.commit()
                    messagebox.showinfo("Deleted", "Contact Deleted Succedully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                    print(e)
        except:
            messagebox.showerror("Error", "Please Select a Contact!")
    
    def function(self):
        self.destroy()