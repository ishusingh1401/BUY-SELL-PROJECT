# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:43:47 2021

@author: ishu singh
"""
from tkinter import *
from PIL import Image,ImageTk
def met_aboutus(frm):
    lbl_message = Label(frm,text = "ABOUT US")
    lbl_message.pack()
    global root
    root=frm
    #root = Tk()
    root.geometry("500x500") 
    root.title("ABOUT US") 
    
    a= Label(root, text ="TEAM MEMBERS:-",font=(16) ) 
    a.place(x = 50, y = 20)
    b = Label(root, text =" ISHU SINGH(ishusingh058@gmail.com) (UNIVERSITY ROLL NO:1705610050)",foreground='purple',font=(16)) 
    b.place(x = 50, y =50 ) 
    c = Label(root, text ="HARSH GUPTA(harshgupta6660@gmail.com) (UNIVERSITY ROLL NO:1705610044)",foreground='purple',font=(16)) 
    c.place(x = 50, y =80 )
    d = Label(root, text ="HARSHIT SAXENA(harshitsaxena278@gmail.com) (UNIVERSITY ROLL NO:1705610048)",foreground='purple',font=(16)) 
    d.place(x = 50, y =110 ) 
    e = Label(root, text ="COLLEGE:- BABU BANARASI DAS NORTHERN INDIA INSTITUTE OF TECHNOLOGY",foreground='green',font=(16)) 
    e.place(x = 50, y =140 ) 
    e = Label(root, text ="COLLEGE CODE:- 056",font=(16)) 
    e.place(x = 50, y =170 ) 
    f = Label(root, text ="BUY/SELL PROJECT",font=(16)) 
    f.place(x = 50, y =200 ) 
    
    
    
    btn_exit =Button(root, text ="EXIT",  
                        bg ='grey',font=(14),command=root.destroy) 
    btn_exit.place(x = 70, y = 270, width = 75)
    
    
    root.mainloop()
    return
    
    
    
    


