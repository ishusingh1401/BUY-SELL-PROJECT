# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:24:00 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import ttk
import pymysql
#register_user_table(user_id text, user_pass text, user_contact text, 
#user_email text, user_fname text, 
#user_lname text, user_address text);

def met_fetch_user_regis(frm):
    lbl_message = Label(frm,text = "USER REGISTRATION DETAILS")
    lbl_message.pack()
    global root
    root=frm
    root.geometry("2000x2000") 
    root.title("USER REGISTRATION DETAILS")
    root.resizable(False,False)
    
    global tv
    frame1=Frame(root)
    frame1.pack(side=LEFT,padx=5)
    
    
    tv=ttk.Treeview(root,columns=(1,2,3,4,5,6,7,8),show="headings")
    tv.pack()
    
    tv.heading(1,text="USER ID")
    tv.heading(2,text="USER PASSWORD")
    tv.heading(3,text="CONTACT NO")
    tv.heading(4,text="EMAIL ID")
    tv.heading(5,text="FIRST NAME")
    tv.heading(6,text="LAST NAME")
    tv.heading(7,text="ADDRESS")
    tv.heading(8,text="CITY")
    btn_reset =Button(root, text ="EXIT",command=frm.destroy).pack()
   
    db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
    mycursor=db.cursor()
    sql="SELECT * FROM register_user_table"
    mycursor.execute(sql)
    list0=mycursor.fetchall()
    total=mycursor.rowcount
    print("TOTAL DATA ENTRIES ARE:",str(total))
    for i in list0:
        tv.insert('','end',values=i)
  
    root.mainloop()


