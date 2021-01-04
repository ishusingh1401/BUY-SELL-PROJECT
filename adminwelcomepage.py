# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:09:06 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import messagebox
import pymysql
from PIL import Image,ImageTk
import pymysql
import database_detail_fetch as database_fetch_

def call_databse_fetch_details():
    mn_window= Toplevel(root)
    database_fetch_.met_database_fetch_(mn_window)
    return

def met_admin_welcome(frm):
    global root
    root=frm
    root.geometry("500x500") 
    root.title("ADMIN WELCOME PAGE")
    F1=Frame(root)
    F1.grid(row=1)
    testimg = Image.open("welcomadminimage.jpg")
    testimg=testimg.resize((1920,1000),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(F1,image=photo)
    label1.place(x=500,y=500,width=500,height=500)
    label1.image=photo
    label1.pack(fill=BOTH,expand=YES)
    btn_plot =Button(F1, text ="VIEW DATABASE",  
                      bg ='white',font=(14),command=call_databse_fetch_details ) 
    btn_plot.place(x = 150, y = 150, width = 200)

    btn_view =Button(F1, text ="EXIT",  
                        bg ='white',font=(14),command=root.destroy) 
    btn_view.place(x = 450, y = 150, width = 200)
    root.mainloop() 
 


