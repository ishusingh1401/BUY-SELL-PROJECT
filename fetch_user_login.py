# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:21:31 2021
@author: ishu singh
"""
from tkinter import * 
from tkinter import ttk
import pymysql
#create table user_login_details(user_id text, user_pass text);
def met_fetch_user_login_details_(frm):
    lbl_message = Label(frm,text = "FEEDBACK DETAILS")
    lbl_message.pack()
    global root
    root=frm
    root.geometry("800x500") 
    root.title("FEEDBACK DETAILS")
    root.resizable(False,False)
    
    
    global tv
    frame1=Frame(root)
    frame1.pack(side=LEFT,padx=20)
    
    
    tv=ttk.Treeview(root,columns=(1,2),show="headings")
    tv.pack()
    
    
    tv.heading(1,text="USER ID")
    tv.heading(2,text="USER PASSWORD")
    btn_reset =Button(root, text ="EXIT",command=frm.destroy).pack()
    
   
    db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
    mycursor=db.cursor()
    sql="SELECT * FROM user_login_details"
    mycursor.execute(sql)
    list0=mycursor.fetchall()
    for i in list0:
        tv.insert('','end',values=i)
  
    root.mainloop()



