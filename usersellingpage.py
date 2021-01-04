# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:10:39 2021

@author: ishu singh
"""
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql


def met_user_selling(frm):
    lbl_message = Label(frm,text = "SELLING PAGE")
    lbl_message.pack()
    global root
    root=frm
    #root = Tk()
    root.geometry("500x500") 
    root.title("Selling PAGE") 
    
#######################################################################################################   
    def resetact():
        SellerID.set("")
        Sellername.set("")
        ProductID.set("")
        Productname.set("")
        dateofpurchase.set("")
        mrpPRICE.set("")
        sellingPRICE.set("")
   ##############################################################################################
    SellerID=StringVar()
    Sellername=StringVar()
    ProductID=StringVar()
    Productname=StringVar()
    dateofpurchase=StringVar()
    mrpPRICE=StringVar()
    sellingPRICE=StringVar()
   # Seller_ID Seller_name Product_ID Product_name dateof_purchase mrp_price sp_price
   
    def submitact():
        Seller_ID = SellerID.get() 
        Seller_name = Sellername.get() 
        Product_ID=ProductID.get()
        Product_name=Productname.get()
        dateof_purchase=dateofpurchase.get()
        mrp_price=mrpPRICE.get() 
        sp_price=sellingPRICE.get()
         
        print(f"The details entered by you is {Seller_ID} {Seller_name} {Product_ID} {Product_name}  {dateof_purchase} {mrp_price}  {sp_price} ")
        db=pymysql.connect(user="root",password="ishu1401@I",host="localhost",database="shoppingdb")
        with db:
            mycursor=db.cursor()
            sql="INSERT INTO seller_details VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val=(Seller_ID,Seller_name,Product_ID,Product_name,dateof_purchase,mrp_price,sp_price)
            mycursor.execute(sql,val)
            db.commit()
            print("inserted successfully")
            messagebox.showinfo(title="STATUS:SUCCESS!",message="DATA INSERTED SUCESSFULLY!!")
    a= Label(root, text ="Seller Id", ) 
    a.place(x = 50, y = 20) 
  
    x =Entry(root,textvar=SellerID, width = 35) 
    x.place(x = 150, y = 20, width = 500)
   
    b = Label(root, text ="Seller Name") 
    b.place(x = 50, y =50 ) 
    
    y = Entry(root,textvar=Sellername ,width = 35) 
    y.place(x = 150, y = 50, width = 500) 

    f=Label(root, text ="Product Id") 
    f.place(x = 50, y = 80) 
    
    v =Entry(root,textvar=ProductID, width = 35) 
    v.place(x = 150, y = 80, width = 500) 

    e = Label(root, text ="Product name") 
    e.place(x = 50, y = 110) 
    
    u=Entry(root,textvar=Productname, width = 35) 
    u.place(x = 150, y = 110, width = 500) 
    

    c = Label(root, text ="Date of purchase/mfd: ") 
    c.place(x = 50, y = 140) 
    
    z= Entry(root,textvar=dateofpurchase, width = 35) 
    z.place(x = 150, y = 140, width = 500)
    
    d = Label(root, text ="Marked Price: ")
    d.place(x = 50, y = 170 ) 
    
    w =Entry(root,textvar=mrpPRICE, width = 35)
    w.place(x = 150, y = 170, width = 500) 

    
    g= Label(root, text ="Selling Price")
    g.place(x = 50, y = 200) 
    
    p =Entry(root,textvar=sellingPRICE, width = 35) 
    p.place(x = 150, y = 200, width = 500) 

    
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
    testimg = Image.open("usershoppingimage.jpg")
    testimg=testimg.resize((800,900),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(testimg)
    label1=Label(root,image=photo)
    label1.image=photo
    label1.place(x=800,y=50,height=900,width=1000)
    


    root.mainloop()
    
