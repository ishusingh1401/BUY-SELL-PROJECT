# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:25:33 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import userpage as userpage_
import usersellingpage as userselling__

def call_userpage():
   mn_window= Toplevel(root)
   userpage_.met_welcome(mn_window)
   return
  
def call_userselling():
    mn_window= Toplevel(root)
    userselling__.met_user_selling(mn_window)
    return

def met_user_welcome(frm):
    global root
    root=frm
    root.geometry("500x500") 
    root.title("WELCOME PAGE")
    F1=Frame(root)
    F1.grid(row=1)
    testimg = Image.open("welcomadminimage.jpg")
    testimg=testimg.resize((1920,1000),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(F1,image=photo)
    label1.place(x=500,y=500,width=500,height=500)
    label1.image=photo
    label1.pack(fill=BOTH,expand=YES)
    btn_plot =Button(F1, text ="BUY",  
                      bg ='white',font=(14),command=call_userpage ) 
    btn_plot.place(x = 150, y = 150, width = 200)

    btn_view =Button(F1, text ="SELL",  
                        bg ='white',font=(14),command=call_userselling) 
    btn_view.place(x = 450, y = 150, width = 200)
    
    btn_exit =Button(F1, text ="EXIT",  
                        bg ='white',font=(14),command=root.destroy) 
    btn_exit.place(x = 750, y = 150, width = 75)
    
    
    root.mainloop() 
 

    
 




