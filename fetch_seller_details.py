# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:11:34 2021

@author: ishu singh
"""

from tkinter import * 
from tkinter import ttk
import pymysql

def met_fetch_seller(frm):
    lbl_message = Label(frm,text = "SELLER DETAILS")
    lbl_message.pack()
    global root
    root=frm
    root.geometry("2000x2000") 
    root.title("SELLER DETAILS")
    root.resizable(False,False)
    
    global tv
    frame1=Frame(root)
    frame1.pack(side=LEFT,padx=5)
    
    
    tv=ttk.Treeview(root,columns=(1,2,3,4,5,6,7),show="headings")
    tv.pack()
    
    tv.heading(1,text="SELLER ID")
    tv.heading(2,text="SELLER NAME")
    tv.heading(3,text="PRODUCT ID")
    tv.heading(4,text="PRODUCT NAME")
    tv.heading(5,text="DATE OF PURCHASE/MANUFACTURE")
    tv.heading(6,text="MARKED PRICE")
    tv.heading(7,text="SELLING PRICE")
    btn_reset =Button(root, text ="EXIT",command=frm.destroy).pack()
   
    db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
    mycursor=db.cursor()
    sql="SELECT * FROM seller_details"
    mycursor.execute(sql)
    list0=mycursor.fetchall()
    total=mycursor.rowcount
    print("TOTAL DATA ENTRIES ARE:",str(total))
    for i in list0:
        tv.insert('','end',values=i)
  
    root.mainloop()


