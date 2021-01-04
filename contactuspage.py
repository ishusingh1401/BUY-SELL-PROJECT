# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:45:45 2021

@author: ishu singh
"""
from tkinter import *

def met_contact_us(frm):
    #lbl_message = Label(frm,text = "CONTACT US")
    #lbl_message.pack()
    global root
    root=frm
    #root = Tk()
    root.geometry("500x500") 
    root.title("CONTACT US") 
    
    a= Label(root, text ="PHONE NUMBER:- 23456789345",font=(14) ) 
    a.place(x = 50, y = 20)
    b = Label(root, text ="ADDRESS-E-2/414 VIRAT PLAZA",font=(14)) 
    b.place(x = 50, y =50 ) 
    c = Label(root, text ="LUCKNOW(UTTAR PRADESH)",font=(14)) 
    c.place(x = 50, y =80 ) 
    d = Label(root, text ="PIN CODE:226019",font=(14)) 
    d.place(x = 50, y =110 ) 
    e = Label(root, text ="LOCATION : INDIA",font=(14)) 
    e.place(x = 50, y =140 ) 
    btn_exit =Button(root, text ="EXIT",  
                        bg ='grey',font=(14),command=root.destroy) 
    btn_exit.place(x = 350, y = 150, width = 75)
    
    root.mainloop()
    return
    


