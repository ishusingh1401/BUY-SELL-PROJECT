# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:45:48 2021

@author: ishu singh
"""
from tkinter import *
import smtplib
from tkinter import messagebox

     


def met_mail_us(frm):
    def send_message():
        address_info = address.get()
        email_body_info = email_body.get()
        print(address_info,email_body_info)
        #sender_email = "####ENTERYOUREMAILHERE######" 
        #sender_email = "@gmail.com"
        #sender_password = "###ENTERYOURPASSWORDHERE#####"
        #sender_password = ""
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)
        print("Login successful")
        server.sendmail(sender_email,address_info,email_body_info)
        print("Message sent")
        address_entry.delete(0,END)
        email_body_entry.delete(0,END)
    global app
    app = frm
    app.geometry("500x500")
    app.title("MAIL US")
    heading = Label(app,text="MAIL US ",bg="purple",fg="yellow",font="10",width="500",height="2")
    heading.pack()
    address_field = Label(app,text="RECIPIENT EMAIL ID :")
    email_body_field = Label(app,text="MESSAGE :")
    address_field.place(x=15,y=70)
    email_body_field.place(x=15,y=140)
    address = StringVar()
    email_body = StringVar()
    address_entry = Entry(app,textvariable=address,width="30")
    email_body_entry = Entry(app,textvariable=email_body,width="30")
    address_entry.place(x=20,y=100)
    email_body_entry.place(x=20,y=180)
    button = Button(app,text="SEND MESSAGE",command=send_message,width="20",height="1",bg="grey")
    button.place(x=15,y=220)
    reset = Button(app,text="RESET",command=None,width="20",height="1",bg="grey")
    reset.place(x=200,y=220)
    exit_ = Button(app,text="EXIT",command=None,width="20",height="1",bg="grey")
    exit_.place(x=390,y=220)
    app.mainloop()
    return

