# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:19:45 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import ttk
import pymysql
#user_name text,user_email_id text,user_comments text
def met_fetch_rateus(frm):
    lbl_message = Label(frm,text = "RATING DETAILS")
    lbl_message.pack()
    global root
    root=frm
    root.geometry("800x500") 
    root.title("FEEDBACK DETAILS")
    root.resizable(False,False)
    
    global tv
    frame1=Frame(root)
    frame1.pack(side=LEFT,padx=20)
    
    
    tv=ttk.Treeview(root,columns=(1),show="headings")#,height="S"
    tv.pack()
    
    tv.heading(1,text="RATING")
    btn_reset =Button(root, text ="EXIT",command=frm.destroy).pack()
    
    db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
    mycursor=db.cursor()
    sql="SELECT * FROM rate_user_table"
    mycursor.execute(sql)
    list0=mycursor.fetchall()
    total=mycursor.rowcount
    print("TOTAL DATA ENTRIES ARE:",str(total))
    for i in list0:
        tv.insert('','end',values=i)
  
    root.mainloop()



