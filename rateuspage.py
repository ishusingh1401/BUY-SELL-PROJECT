# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:44:46 2021

@author: ishu singh
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
 


def met_rate_us(frm):
    #lbl_message = Label(frm,text = "RATE US ")
    #lbl_message.pack()
    global root
    root=frm
    root.geometry("500x500") 
    root.title("RATE US")

        
    frame_header = ttk.Frame(root)
    frame_header.pack()
    headerlabel = ttk.Label(frame_header, text='RATE US', foreground='orange',
                        font=('Arial', 24))
    headerlabel.grid(row=0, column=1)
    messagelabel = ttk.Label(frame_header,
                         text='PLEASE RATE US FROM THE SCALE 1 TO 10',
                         foreground='purple', font=('Arial', 10))
    messagelabel.grid(row=1, column=1)

    frame_content = ttk.Frame(root)
    frame_content.pack()
    myvar = StringVar()
    global entry_name
    namelabel = ttk.Label(frame_content, text='ENTER A NO FROM 1-10: ')
    namelabel.grid(row=1, column=1, padx=2, sticky='sw')
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
    entry_name.grid(row=2, column=1, padx=2, sticky='sw')
    #
    def clear():
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        
    #
    def submit():
        print('Rating:{}'.format(myvar.get()))
        a=format(myvar.get())

        messagebox.showinfo(title='Submit', message='Thank you for your Rating us.')
        db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
        with db:
            mycursor=db.cursor()
            sql="INSERT INTO rate_user_table VALUES(%s)"
            val=(a)
            mycursor.execute(sql,val)
            db.commit()
            print("inserted successfully")
    
        entry_name.delete(0, END)
        
    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=3, column=1,padx=2,sticky='e')#sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=3, column=2,padx=2, sticky='w')
    exitbutton = ttk.Button(frame_content, text='Exit', command=root.destroy).grid(row=4, column=3,padx=2, sticky='e')

    root.mainloop()


