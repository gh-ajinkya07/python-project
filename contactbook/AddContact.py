from tkinter import * 
import datetime
import psycopg2
from tkinter import messagebox



connection = psycopg2.connect(
                            
                            user = "postgres",
                            password = "passsql",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "contact_db" )
cursor = connection.cursor()


date = datetime.datetime.now()

class createContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+350+150")
        self.title("Add new contact")
        self.resizable(False,False)

        self.top = Frame(self, height = 140, bg = 'white')
        self.top.pack(fill = X)
    
        self.bottom = Frame(self, height = 380, bg = '#000000')
        self.bottom.pack(fill = X)

        # Top Frame designing 
        self.top_image = PhotoImage(file = "icons/mycontact3.png", height = 75, width = 80 )
        self.top_image_label = Label(self.top, image = self.top_image, bg = "white")
        self.top_image_label.place(x = 100, y = 30)

        self.heading = Label(self.top, text = "Add Contact", font = "arial 25 bold", bg = "white", fg = "#000000")
        self.heading.place(x = 210, y = 40)

        # Adding date
        self.top_date = Label(self.top, text = date.strftime('%d %B,%Y'), bg = "white", font = "arial 10 bold")
        self.top_date.place(x = 500, y = 100)

        # Name
        self.name_label = Label(self.bottom, text = "Name", font = 'arial 15 bold', fg = 'white', bg = 'black')
        self.name_label.place(x = 50, y = 30)
        
        self.entry_name = Entry(self.bottom, width = 30, bd = 3)
        self.entry_name.insert(1, "Enter First Name")
        self.entry_name.place(x = 230, y = 32)
        #surname
        self.sname_label = Label(self.bottom, text = "Surname", font = 'arial 15 bold', fg = 'white', bg = 'black')
        self.sname_label.place(x = 50, y = 80)

        self.entry_surname = Entry(self.bottom, width = 30, bd = 3)
        self.entry_surname.insert(1, "Enter Last Name")
        self.entry_surname.place(x = 230, y = 82)

        #email
        self.email_label = Label(self.bottom, text = "Email", font = 'arial 15 bold', fg = 'white', bg = 'black')
        self.email_label.place(x = 50, y = 130)

        self.entry_email = Entry(self.bottom, width = 30, bd = 3)
        self.entry_email.insert(1, "Enter Email")
        self.entry_email.place(x = 230, y = 132)

        #phone
        self.phone_label = Label(self.bottom, text = "Phone Number", font = 'arial 15 bold', fg = 'white', bg = 'black')
        self.phone_label.place(x = 50, y = 180)

        self.entry_phone = Entry(self.bottom, width = 30, bd = 3)
        self.entry_phone.insert(1, "Enter Number  ")
        self.entry_phone.place(x = 230, y = 182)

        #Address
        self.address_label = Label(self.bottom, text = "Address", font = 'arial 15 bold', fg = 'white', bg = 'black')
        self.address_label.place(x = 50, y = 230)

        self.entry_address = Entry(self.bottom, width = 30, bd = 3)
        self.entry_address.insert(1, "Enter Address ")
        self.entry_address.place(x = 230, y = 232)

        # Pincode
        self.pin_label = Label(self.bottom, text = "Pin Code", font = 'arial 15 bold', fg = 'white', bg = 'black')
        self.pin_label.place(x = 50, y = 280)

        self.entry_pincode = Entry(self.bottom, width = 30, bd = 3)
        self.entry_pincode.insert(1, "Enter Pincode ")
        self.entry_pincode.place(x = 230, y = 282)

        # Button

        self.submit_button = Button(self.bottom, text = "Add Contact", font = 'arial 12 bold', width = 18, bg = "#2de343", command = self.add_contact)
        self.submit_button.place(x = 226, y = 332)

    

    def add_contact(self):

        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        pincode = self.entry_pincode.get()

        if name != "Enter First Name" and surname != "Enter Last Name" and email != "Enter Email" and phone != "Enter Number  " and address != "Enter Address " and pincode != "Enter Pincode ":
            try:
                # Adding to database 

                querry = "insert into addressbook(first_name, last_name, email, phone, address, pincode) values( '{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(name, surname, email, phone, address, pincode)
                cursor.execute(querry)
                connection.commit()
                messagebox.showinfo("Success", "Contact Added Succefully")
                
            except Exception as e:
                print(e)
                messagebox.showerror("Error", str(e))    
        else:
            messagebox.showerror("Error", "Please fill all the details!", icon = "warning")
