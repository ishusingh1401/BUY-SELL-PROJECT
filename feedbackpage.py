# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:44:03 2021

@author: ishu singh
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
 

def met_feedback(frm):
    global root
    root=frm
    root.geometry("500x500") 
    root.title("FEED BACK FORM")

        
    frame_header = ttk.Frame(root)
    frame_header.pack()
    headerlabel = ttk.Label(frame_header, text='CUSTOMER FEEDBACK', foreground='orange',
                        font=('Arial', 24))
    headerlabel.grid(row=0, column=1)
    messagelabel = ttk.Label(frame_header,
                         text='PLEASE TELL US WHAT YOU THINK',
                         foreground='purple', font=('Arial', 10))
    messagelabel.grid(row=1, column=1)

    frame_content = ttk.Frame(root)
    frame_content.pack()

    myvar = StringVar()
    var = StringVar()
    namelabel = ttk.Label(frame_content, text='Name')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')
    global entry_name
    global entry_email
    global textcomment
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
    entry_name.grid(row=1, column=0)

    emaillabel = ttk.Label(frame_content, text='Email')
    emaillabel.grid(row=0, column=1, sticky='sw')
    entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
    entry_email.grid(row=1, column=1)

    commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
    commentlabel.grid(row=2, column=0, sticky='sw')
    textcomment = Text(frame_content, width=70, height=10)
    textcomment.grid(row=3, column=0, columnspan=2)
    textcomment.config(wrap ='word')
        
    def clear():
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)
        
    def submit():
        #global entry_name
        #global entry_email
        #global textcomment
        print('Name:{}'.format(myvar.get()))
        print('Email:{}'.format(var.get()))
        print('Comment:{}'.format(textcomment.get(1.0, END)))
        a=format(myvar.get())
        b=format(var.get())
        c=format(textcomment.get(1.0, END))
        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
        with db:
            mycursor=db.cursor()
            sql="INSERT INTO feedback_user_table VALUES(%s,%s,%s)"
            val=(a,b,c)
            mycursor.execute(sql,val)
            db.commit()
            print("inserted successfully")
    
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)
        
    
    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0,sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1,sticky='w')
    exitbutton = ttk.Button(frame_content, text='Exit', command=root.destroy).grid(row=5, column=0,sticky='e')

    root.mainloop()



    
    
