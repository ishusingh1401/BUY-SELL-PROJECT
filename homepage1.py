# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 08:27:50 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk 
from PIL import Image,ImageTk
import userregispage as user_regis
import adminloginpage2 as admin_login
import userloginpage2 as user_login
import aboutuspage as aboutus_
import feedbackpage as feedback_
import rateuspage as rate_
import demopage as demo_
import contactuspage as contact_
import mailuspage as mail_
#
def call_user_registerscreen():
    mn_window= Toplevel(root)
    user_regis.met_user_registerscreen(mn_window)
    return
#
def call_adminlogin():
    mn_window= Toplevel(root)
    admin_login.met_login_admin(mn_window)
    return
#
def call_userlogin():
    mn_window= Toplevel(root)
    user_login.met_login_user(mn_window)
    return
#
def call_aboutus():
     mn_window= Toplevel(root)
     aboutus_.met_aboutus(mn_window)
     return
#
def call_feedback():
    mn_window= Toplevel(root)
    feedback_.met_feedback(mn_window)
    return

#
def call_rateus():
    mn_window= Toplevel(root)
    rate_.met_rate_us(mn_window)
    return
#
def call_demo():
    mn_window= Toplevel(root)
    demo_.met_demo_heart(mn_window)
    return

#
def call_contactus():
    mn_window= Toplevel(root)
    contact_.met_contact_us(mn_window)
    return
#
def call_mailus():
    mn_window= Toplevel(root)
    mail_.met_mail_us(mn_window)
    return
    
# creating tkinter window 
     
if __name__ == '__main__':
    global root
    root = Tk() 
    root.title('SHOPPING SITE ') 
    root.geometry("500x500")
    # Creating Menubar 
    menubar = Menu(root)
    
    #HOME
    home_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_command(label ='HOME',command=None) 
    
    #LOG IN
    login_page_menu =Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='LOG IN', menu = login_page_menu) 
    login_page_menu.add_command(label ='ADMIN LOGIN', command = call_adminlogin  ) 
    login_page_menu.add_command(label ='USER LOGIN' , command =call_userlogin  ) 
    login_page_menu.add_command(label ='USER REGISTER' , command = call_user_registerscreen)
    login_page_menu.add_separator()
    login_page_menu.add_command(label ='Exit', command = root.destroy)

    #ABOUT US
    aboutus_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_command(label ='ABOUT US ',command=call_aboutus) 

    #CONTACT US
    contactus_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='CONTACT US', menu = contactus_page_menu) 
    contactus_page_menu.add_command(label ='CALL US', command = call_contactus) 
    contactus_page_menu.add_command(label ='EMAIL US', command = call_mailus) 
    contactus_page_menu.add_separator() 


    #HELP
    help_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='HELP', menu = help_page_menu)  
    help_page_menu.add_command(label ='Demo', command = call_demo) 
    help_page_menu.add_separator()
    
    #FEEDBACK
    feedback_page_menu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='FEEDBACK', menu = feedback_page_menu) 
    feedback_page_menu.add_command(label ='SEND FEEDBACK', command =call_feedback) 
    feedback_page_menu.add_command(label ='RATE US', command = call_rateus) 
    feedback_page_menu.add_separator() 
    
    #EXIT
    exit_page_menu = Menu(menubar, tearoff =0) 
    menubar.add_command(label ='EXIT',command=root.destroy) 

    # display Menu
    testimg = Image.open("homepageimage1.jpg")
    testimg=testimg.resize((1920,1000),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(root,image=photo)
    label1.image=photo
    label1.place(x=550,y=50,height=900,width=1000)
    label1.pack(fill=BOTH,expand=YES)
    root.config(menu = menubar) 
    root.mainloop() 


