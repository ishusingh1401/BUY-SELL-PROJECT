# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:09:06 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import messagebox
import pymysql
import userregispage as userreg_
import userwelcomepage as userwelcome__ 
from PIL import Image,ImageTk

#
def call_welcome_buy():
   mn_window= Toplevel(root)
   userwelcome__.met_user_welcome(mn_window)
   return



def call_userlogin():
    mn_window= Toplevel(root)
    met_login_user(mn_window)
    return

def call_user_regis():
    mn_window= Toplevel(root)
    userreg_.met_user_registerscreen(mn_window)
    return

def met_login_user(frm):
    global root
    root=frm
    root.geometry("500x500") 
    root.title("CUSTOMER LOGIN") 
    global UserID
    global password

    UserID=StringVar()
    password=StringVar()
    def cancel():
        status=messagebox.askyesno(title="Question",message='DO YOU WANT TO EXIT?')
        if status==True:
            root.destroy()
        else:
            messagebox.showwarning(title="Warning Message",message='MOVING TO USER LOGIN PAGE')
            call_userlogin()


    def resetact():
        UserID.set("")
        password.set("")
 
    def submitact(): 
        userid = UserID.get() 
        passw = password.get()
        if userid =="":
            messagebox.showwarning(title="Warning Message",message='ALL FIELDS ARE MANDATORY**')
            call_userlogin()
        if passw =="":
            messagebox.showwarning(title="Warning Message",message='ALL FIELDS ARE MANDATORY**')
            call_userlogin()
        else:
            print(f"The ID entered by you is {userid}  and password is {passw}") 
            logintodb(userid, passw) 
        
        print(f"The ID entered by you is {userid}  and password is {passw}") 
        logintodb(userid, passw) 
    def logintodb(userid, passw): 
        global savequery
        db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
        cursor = db.cursor() 
        savequery = "select * from user_login_details"
        checkRec=0
        try: 
            cursor.execute(savequery) 
            myresult = cursor.fetchall() 
          
            for x in myresult: 
                if x[0] == userid and x[1]==passw:
                    print("USER FOUND SUCCESSFULLY!! LOGIN SUCCESS!!")
                    checkRec=1
                    messagebox.showinfo(title="LOGIN STATUS:SUCCESS",message="YOU HAVE LOGGED IN")
                    call_welcome_buy()
                    
            if checkRec==0:
                messagebox.showinfo(title="LOGIN STATUS:ERROR",message="YOU HAVE ENTERED WRONG ID /PASSWORD")
                print("User Not Found!! Register Yourself!!")
        except ValueError as ve: 
            print(ve) 
        

    a= Label(root, text ="USER ID- ", ) 
    a.place(x = 50, y = 20) 
  
    x =Entry(root,textvariable=UserID, width = 35) 
    x.place(x = 150, y = 20, width = 300)
   
    b = Label(root, text ="PASSWORD- ") 
    b.place(x = 50, y =50 ) 
    
    y = Entry(root,show='*',textvariable=password ,width = 35) 
    y.place(x = 150, y = 50, width = 300) 

    btn_login =Button(root, text ="LOG IN",  
                      bg ='grey',command=lambda: submitact() ) 
    btn_login.place(x = 150, y = 150, width = 75)

    btn_reset =Button(root, text ="RESET",  
                        bg ='grey',command=resetact) 
    btn_reset.place(x = 250, y = 150, width = 75)
    
    btn_reset =Button(root, text ="REGISTER",  
                        bg ='grey',command=call_user_regis) 
    btn_reset.place(x = 350, y = 150, width = 75)
    btn_reset =Button(root, text ="EXIT",  
                        bg ='grey',command=cancel) 
    btn_reset.place(x = 450, y = 150, width = 75)
     # display Menu
    testimg = Image.open("loginimage2.jpg")
    testimg=testimg.resize((800,900),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(root,image=photo)
    label1.image=photo
    label1.place(x=550,y=50,height=900,width=1000)
    root.mainloop() 
 

