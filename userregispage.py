# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:07:07 2021

@author: ishu singh
"""

#import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
def met_user_registerscreen(frm):
    lbl_message = Label(frm,text = "USER REGISTRATION PAGE")
    lbl_message.pack()
    global root
    root=frm
    #root = Tk()
    root.geometry("500x500") 
    root.title("USER REGISTERATION PAGE") 
    
#######################################################################################################   
    def resetact():
        UserID.set("")
        password.set("")
        contact.set("")
        emailid.set("")
        fname.set("")
        lname.set("")
        address_user.set("")
        user_city.set("")
######################################################################################################
    UserID=StringVar()
    password=StringVar()
    contact=StringVar()
    emailid=StringVar()
    fname=StringVar()
    lname=StringVar()
    address_user=StringVar()
    usercity=StringVar()
    def submitact():
        userid_user = UserID.get() 
        password_user = password.get() 
        contact_user=contact.get()
        emailid_user=emailid.get()
        fname_user=fname.get() 
        lname_user=lname.get()
        adress_user=address_user.get()
        user_city=usercity.get()
         
        print(f"The details entered by you is {userid_user} {password_user} {contact_user} {emailid_user}  {fname_user} {lname_user}  {adress_user} {user_city}")
        db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
        with db:
            mycursor=db.cursor()
            sql="INSERT INTO register_user_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(userid_user,password_user,contact_user,emailid_user,fname_user,lname_user,adress_user,user_city)
            mycursor.execute(sql,val)
            db.commit()
            print("inserted successfully")
            mycursor1=db.cursor()
            sql1="INSERT INTO user_login_details VALUES(%s,%s)"
            val1=(userid_user,password_user)
            mycursor1.execute(sql1,val1)
            db.commit()
            print("Login id and password saved successfully")
            messagebox.showinfo(title="STATUS:SUCCESS!",message="DATA INSERTED SUCESSFULLY!!")
        
                    
            
            
            
    a= Label(root, text ="User ID-", ) 
    a.place(x = 50, y = 20) 
  
    x =Entry(root,textvar=UserID, width = 35) 
    x.place(x = 150, y = 20, width = 500)
   
    b = Label(root, text ="Password -") 
    b.place(x = 50, y =50 ) 
    
    y = Entry(root,textvar=password ,width = 35) 
    y.place(x = 150, y = 50, width = 500) 

    f=Label(root, text ="Contact no -") 
    f.place(x = 50, y = 170) 
    
    v =Entry(root,textvar=contact, width = 35) 
    v.place(x = 150, y = 170, width = 500) 

    e = Label(root, text ="Email ID -") 
    e.place(x = 50, y = 140) 
    
    u=Entry(root,textvar=emailid, width = 35) 
    u.place(x = 150, y = 140, width = 500) 
    

    c = Label(root, text ="Fname-") 
    c.place(x = 50, y = 80) 
    
    z= Entry(root,textvar=fname, width = 35) 
    z.place(x = 150, y = 80, width = 500) 
    
    d = Label(root, text ="Lname-")
    d.place(x = 50, y = 110 ) 
    
    w =Entry(root,textvar=lname, width = 35)
    w.place(x = 150, y = 110, width = 500) 

    
    g= Label(root, text ="Address-")
    g.place(x = 50, y = 200) 
    
    p =Entry(root,textvar=address_user, width = 35) 
    p.place(x = 150, y = 200, width = 500) 


    h= Label(root, text ="CITY ")
    h.place(x = 50, y = 230) 
    
    q=Entry(root,textvar=usercity) 
    q.place(x = 150, y = 230, width = 500) 
    btn_submit =Button(root, text ="SUBMIT",  
    bg ='grey',command=submitact ) 
    btn_submit.place(x = 250, y = 350, width = 70)

    btn_reset =Button(root, text ="RESET",  
                      bg ='grey',command=resetact) 
    btn_reset.place(x = 450, y = 350, width = 70)
    btn_exit =Button(root, text ="EXIT",  
                      bg ='grey',command=root.destroy) 
    btn_exit.place(x = 650, y = 350, width = 70)
    # display Menu
    testimg = Image.open("registerimage2.jpg")
    testimg=testimg.resize((800,900),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(root,image=photo)
    label1.image=photo
    label1.place(x=800,y=50,height=900,width=1000)
    


    root.mainloop()
    


