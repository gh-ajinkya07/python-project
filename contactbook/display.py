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

class displayContact(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        # Fetching persons id

        self.person_id = person_id
        

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

        self.heading = Label(self.top, text = "Contact Details ", font = "arial 25 bold", bg = "white", fg = "#000000")
        self.heading.place(x = 210, y = 40)

        # Adding date
        self.top_date = Label(self.top, text = date.strftime('%d %B,%Y'), bg = "white", font = "arial 10 bold")
        self.top_date.place(x = 500, y = 100)

        # Adding Image

        self.image = PhotoImage(file = 'icons/person1.png')
        self.image_label = Label(self.bottom, image = self.image, bd = 5, bg = "black")
        self.image_label.place(x = 20, y = 10)


        # Fetching data for current person 

        querry = "select * from addressbook where person_id = {}".format(self.person_id)

        cursor.execute(querry)
        person_detail = cursor.fetchone()
        
        person_name = person_detail[1]
        person_surname = person_detail[2]
        person_email = person_detail[3]
        person_number = person_detail[4]
        person_address = person_detail[5]
        person_pincode = person_detail[6]

        self.name_label = Label(self.bottom, text = '{}'.format(person_name), font = "arial 18 bold", bg = 'black', fg = 'white')
        self.name_label.place(x = 200, y = 30)

        self.name_label = Label(self.bottom, text = '{}'.format(person_surname), font = "arial 18 bold", bg = 'black', fg = 'white')
        self.name_label.place(x = 300, y = 30)

        self.phone_label = Label(self.bottom, text = '{}'.format(person_number), font = "arial 18 bold", bg = 'black', fg = 'white')
        self.phone_label.place(x = 200, y = 80)

        self.email_label = Label(self.bottom, text = '{}'.format(person_email), font = "arial 18 bold", bg = 'black', fg = 'white')
        self.email_label.place(x = 200, y = 130)

        self.address_label = Label(self.bottom, text = '{}'.format(person_address), font = "arial 18 bold", bg = 'black', fg = 'white')
        self.address_label.place(x = 200, y = 180)

        self.pincode_label = Label(self.bottom, text = '{}'.format(person_pincode), font = "arial 18 bold", bg = 'black', fg = 'white')
        self.pincode_label.place(x = 200, y = 230)


        self.close_button = Button(self.bottom, text = 'Back', width = 18, font = 'arial 12 bold', bg = '#cf0a0a', fg = 'black', command = self.function)
        self.close_button.place(x = 200, y = 332)
        
    def function(self):
        self.destroy()
