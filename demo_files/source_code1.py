from tkinter import Tk,Frame,Label,Entry,Button,messagebox
from PIL import Image,ImageTk
import mysql.connector
fonts = ('Times_New_Roman_Greek',15)
# font1 = ('Helvetica',18,'bold')

book_name_to_enter = 'Wings of Fire'
author_name_to_enter = 'Abdul Kalam'
blank_to_enter = "Good Book"

root = Tk()
class Library:
    def __init__(self,root):
        self.root = root
        self.page = Frame(self.root,width = 1000,height = 1000)
        self.page.place(x = 0, y = 0)


        self.image_logo = Image.open('../assets/2.png')
        self.image_logo = self.image_logo.resize((820,820))
        self.image_logo = ImageTk.PhotoImage(self.image_logo)
        self.image_logo_label = Label(self.page,image = self.image_logo)
        self.image_logo_label.place(x = 0,y = -100)

        
        self.image_logos = Image.open('../assets/1.png')
        self.image_logos = self.image_logos.resize((175,175))
        self.image_logos = ImageTk.PhotoImage(self.image_logos)
        self.image_logos_label = Label(self.page,image = self.image_logos)
        self.image_logos_label.place(x = 300,y = 60)

        self.book_name = Label(self.page,text = 'BOOK NAME',bg = 'green',fg = 'yellow',font = fonts,width = 15,height = 2)
        self.book_name.place(x = 100,y = 300)
        self.book_name_entry = Entry(self.page,width = 30,font = fonts)
        self.book_name_entry.place(x = 300,y = 310)
        
        self.author_name = Label(self.page,text = 'AUTHOR NAME',bg = 'green',fg = 'yellow',font = fonts,width = 15,height = 2)
        self.author_name.place(x = 100,y = 370)
        self.author_name_entry = Entry(self.page,width = 30,font = fonts)
        self.author_name_entry.place(x = 300,y = 380)
        
        self.button = Button(self.page ,text = 'SHOW',font = fonts,width = 9,bg = 'steel blue',command =self.result)
        self.button.place(x = 330,y = 470)


    def result(self):
        global book_name_to_enter, author_name_to_enter
        self.bname = self.book_name_entry.get()
        self.aname = self.author_name_entry.get()
        if self.bname == book_name_to_enter and  self.aname == author_name_to_enter:
           self.page.destroy()
           login_obj = Login(root)
        else:
            messagebox.showerror('INVALID','NO RESULT FOUND')
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('MY BOOK')
        self.page = Frame(self.root,width = 1000,height = 1000)
        self.page.place(x = 0,y = 0)

        self.image_logoss = Image.open('../assets/3.png')
        self.image_logoss = self.image_logoss.resize((820, 820))
        self.image_logoss = ImageTk.PhotoImage(self.image_logoss)
        self.image_logoss_label = Label(self.page, image=self.image_logoss)
        self.image_logoss_label.place(x=0, y=-200)


        self.bookAvai = Label(self.page,text = ' BOOK AVAILABLE!!',bg = 'green',fg = 'white',font = fonts,width = 20,height = 3)
        self.bookAvai.place(x = 250,y = 30)

        self.bookcontents = Label(self.page,text = ' BOOK CONTENTS : ',bg = 'grey',font = fonts,width = 16)
        self.bookcontents.place(x = 75,y = 120)

        self.booksection = Label(self.page,text = ' BOOK SECTION : ',bg = 'grey',font = fonts,width = 16)
        self.booksection.place(x = 75,y = 180)

        self.noofcopies = Label(self.page,text = 'NO OF COPIES : ',bg = 'grey',font = fonts,width = 16)
        self.noofcopies.place(x = 75,y = 240)

        self.bookratings = Label(self.page,text = ' BOOK REVIEWS : ',bg = 'grey',font = fonts,width = 16)
        self.bookratings.place(x = 75,y = 290)

        self.ratings = Label(self.page,text = ' RATING : ',bg = 'grey',font = fonts,width = 16)
        self.ratings.place(x = 75,y = 440)


        self.feedback = Label(self.page,text = ' FEEDBACK : ',bg = 'grey',font = fonts,width = 16)
        self.feedback.place(x = 75,y = 500)

        self.bookcontLabel = Label(self.page,text = 'It is a great story of Dedication & Achievement.',bg = 'white',font = fonts)
        self.bookcontLabel.place(x = 300,y = 120)

        self.noofcopLabel = Label(self.page,text = '23',bg = 'white',font = fonts,width = 15)
        self.noofcopLabel.place(x = 300,y = 240)

        self.booksection_label = Label(self.page,text = ' Autobiographies. ',bg = 'white',font = fonts,width = 20)
        self.booksection_label.place(x = 300,y = 180)

        self.bookratingsLabel1 = Label(self.page,text = 'Great Book. ',bg = 'white',font = fonts,width = 20)
        self.bookratingsLabel1.place(x = 300,y = 290)

        self.bookratingsLabel2 = Label(self.page,text = 'One must Read it. ',bg = 'white',font = fonts,width = 20)
        self.bookratingsLabel2.place(x = 300,y = 330)

        self.bookratingsLabel3 = Label(self.page,text = 'Excellent Book. ',bg = 'white',font = fonts,width = 20)
        self.bookratingsLabel3.place(x = 300,y = 370)

        self.bookratingsLabel4 = Label(self.page,text = ' 4.7 / 5 ',bg = 'white',font = fonts,width = 20)
        self.bookratingsLabel4.place(x = 300,y = 440)

        self.book_name_entry = Entry(self.page,width = 30,font = fonts)
        self.book_name_entry.place(x = 300,y = 500)

        self.button1 = Button(self.page ,text = 'BACK',font = fonts,width = 9,bg = 'steel blue',command = self.back)
        self.button1.place(x = 330,y = 550)


    def back(self):
        global blank_to_enter
        self.bln = self.book_name_entry.get()
        if self.bln == blank_to_enter or self.bln == "  ":
           self.page.destroy()
           lib = Library(root)
        else:
            messagebox.showerror('INVALID','NO RESULT FOUND')



root.geometry('750x600+400+100')
root.title('MY LIBRARY')
library = Library(root)
root.mainloop()







