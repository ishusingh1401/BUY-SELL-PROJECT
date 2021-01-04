# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:12:20 2021

@author: ishu singh
"""
import pandas as pd
from tkinter import *
import fetch_feedback as fetch_feed
import fetch_rateus as fetch_rateus
import fetch_user_regis as fetch_user_regis_
import fetch_user_login as fetch_user_login_details_
import fetch_seller_details as fetch_seller

def call_fetch_seller():
    mn_window= Toplevel(frm)
    fetch_seller.met_fetch_seller(mn_window)
    return


def call_fetch_feed():
    mn_window= Toplevel(frm)
    fetch_feed.met_fetch_feedback(mn_window)
    return

def call_fetch_rateus():
    mn_window= Toplevel(frm)
    fetch_rateus.met_fetch_rateus(mn_window)
    return

def call_fetch_user_regis():
    mn_window= Toplevel(frm)
    fetch_user_regis_.met_fetch_user_regis(mn_window)
    return

def call_fetch_user_login():
    mn_window= Toplevel(frm)
    fetch_user_login_details_.met_fetch_user_login_details_(mn_window)
    return

def met_database_fetch_(fr):
    global frm
    frm = fr
    lbl_message = Label(frm,text = "WELCOME TO DATABASE DETAILS PAGE").pack()
    frm.title("Welcome")
    frm.geometry("800x600")
    btn_feedback =Button(frm, text ="VIEW FEEDBACK",command=call_fetch_feed).pack()
    btn_feedback =Button(frm, text ="VIEW RATING",command=call_fetch_rateus).pack()
    btn_regis_details =Button(frm, text ="VIEW USER REGISTRATION DETAILS",command=call_fetch_user_regis).pack()
    btn_login_details =Button(frm, text ="VIEW USER LOGIN DETAILS",command=call_fetch_user_login).pack()
    btn_seller_details =Button(frm, text ="VIEW SELLER DETAILS",command=call_fetch_seller).pack()
    btn_reset =Button(frm, text ="EXIT",command=frm.destroy).pack()

