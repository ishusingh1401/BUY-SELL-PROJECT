# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 08:36:45 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import messagebox
import pymysql
import adminwelcomepage as admin_welcom_
from PIL import Image,ImageTk


def call_adminlogin():
    mn_window= Toplevel(root)
    met_login_admin(mn_window)
    return

###########################################################################################

def call_admin_welcome_page():
    mn_window= Toplevel(root)
    admin_welcom_.met_admin_welcome(mn_window)
    return
############################################################################################
def met_login_admin(frm):
    lbl_message = Label(frm,text = "ADMIN LOGIN PAGE")
    lbl_message.pack()
    global root
    root=frm
    #root = Tk()
    root.geometry("500x500") 
    root.title("ADMIN LOG IN PAGE") 
    global AdminID
    global password
    AdminID=StringVar()
    password=StringVar()
    def cancel():
        status=messagebox.askyesno(title="Question",message='DO YOU WANT TO EXIT?')
        if status==True:
            root.destroy()
        else:
            messagebox.showwarning(title="Warning Message",message='MOVING TO ADMIN LOGIN PAGE')
            call_adminlogin()
#####################################################################################################            
    def resetact():
        AdminID.set("")
        password.set("")
#######################################################################################################        
    def submitact(): 
        admin_id = AdminID.get() 
        passw = password.get() 
        if admin_id =="":
            messagebox.showwarning(title="Warning Message",message='ALL FIELDS ARE MANDATORY**')
            call_adminlogin()
        if passw =="":
            messagebox.showwarning(title="Warning Message",message='ALL FIELDS ARE MANDATORY**')
            call_adminlogin()
        else:
            print(f"The ID entered by you is {admin_id}  and password is {passw}") 
            logintodb(admin_id, passw) 
            
##################################################################################################    
    def logintodb(admin_id, passw):
        global savequery
        db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
        cursor = db.cursor() 
        savequery = "select * from admin_login_details"
        checkRec=0
        try: 
            cursor.execute(savequery) 
            myresult = cursor.fetchall() 
          
            for x in myresult: 
                if x[0] == admin_id and x[1]==passw:
                    messagebox.showinfo(title="LOGIN STATUS:SUCCESS",message="YOU HAVE LOGGED IN")
                    print("USER FOUND SUCCESSFULLY!! LOGIN SUCCESS!!")
                    checkRec=1
                    call_admin_welcome_page()
            if checkRec==0:
                messagebox.showinfo(title="LOGIN STATUS:ERROR",message="YOU HAVE ENTERED WRONG ID /PASSWORD")
                print("User Not Found!! Register Yourself!!")
        except ValueError as ve: 
            print(ve) 
    a= Label(root, text ="ADMIN ID-" ) 
    a.place(x = 50, y = 20) 
    
    x =Entry(root,textvar=AdminID, width = 35) 
    x.place(x = 150, y = 20, width = 200)
   
    b = Label(root, text ="PASSWORD-") 
    b.place(x = 50, y =50 ) 
    
    y = Entry(root,show='*',textvar=password ,width = 35) 
    y.place(x = 150, y = 50, width = 200) 
    
    btn_login =Button(root, text ="LOG IN",  
                      bg ='grey',font=(14),command=submitact ) 
    btn_login.place(x = 150, y = 150, width = 75)

    btn_reset =Button(root, text ="RESET",  
                        bg ='grey',font=(14),command=resetact) 
    btn_reset.place(x = 250, y = 150, width = 75)
    
    btn_exit =Button(root, text ="EXIT",  
                        bg ='grey',font=(14),command=cancel) 
    btn_exit.place(x = 350, y = 150, width = 75)
    # display Menu
    testimg = Image.open("loginimage2.jpg")
    testimg=testimg.resize((800,900),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(root,image=photo)
    label1.image=photo
    label1.place(x=550,y=50,height=900,width=1000)
    root.mainloop()
 



