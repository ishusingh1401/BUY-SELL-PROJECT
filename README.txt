1) GROUP NO. 20
  Team Members:- NAMES                   EMAIL ID:                     UNIVERSITY ROLL NO:-
  	      1)ISHU SINGH		ishusingh058@gmail.com	       1705610050	
  	      2)HARSH GUPTA 		harshgupta6660@gmail.com       1705610044
  	      3)HARSHIT SAXENA		harshitsaxena278@gmail.com     1705610048

2)TECHNOLOGIES USED:-
		 a) PLATFORM: SPYDER(ANACONDA 3)
		 b) DATABASE: MySQL Workbench 8.0 CE
		 c) Programming Language: Python and MySql Queries
		 d) Libraries: tkinter,pymysql,GUI
3)Assumptions:-
		1) You must have MySQL Workbench 8.0 CE and SPYDER(ANACONDA 3)(or any puthon programming platform) on your system
		2) You need  to create a new schema in the connected server in MySQL Workbench named "shoppingdb" and execute all queries given in "database_query"
 		   document provided.
		3) Admin details:-ID:- 6029148 password:- ishusingh
		4) User login details:- 818185 password:- ishu1401
		5) You need to provide a gmail id with setting of "less secure on" and password in "mailus.py" file for sending email.
		6) We have provided a "Bill Records" document for maintaing a record of bill generated during buying of product
		7) We also provided a "Menu" document that shows list of item available for buying

4)Responsibilities:
		   1)ISHU SINGH:- Project organising and Integration, Database work ,Admin realted all work ,Buying operation,Mailing page,User related work
		   2)HARSH GUPTA:-Project testing,Selling operation
		   3)HARSHIT SAXENA:-Security constraints and validation,Feedback and rating page
5)Steps:-
	1)After fulfilling all requirements mentioned in assumptions.
        2)Run the "homepage1.py" file
	3)Home page will open
	4)There will be HOME,LOGIN,ABOUT US,CONTACT US, HELP,FEEDBACK and EXIT options on Menu bar
	5) a)HOME:- will return to home page




	   b)LOGIN will provide a drop down menu consisting of:
	      1)ADMIN LOGIN:- It will direct you to a Admin login page.(adminloginpage2.py)
			a)In admin login if you will type a wrong ADMIN ID and PASSWORD then it will not open as validation is applied.
			b)When you will enter right password then it will direct you to the Admin welcome page(adminwelcomepage.py) which consists of two options:- 
		 	 "View database" and "Exit" option.
                	c) If you choose View database option then it will direct to a page which consists of all database record .(database_detail_fetch.py)
		  	 VIEW FEEDBACK(fetchfeedback.py)
	           	 VIEW RATING(fetch_ratus.py)
		   	 VIEW USER REGISTRATION DETAILS(fetch_user_regis.py)
		   	 VIEW USER LOGIN DETAILS(fetch_user_login.py)
		   	 VIEW SELLER DETAILS(fetch_seller_details.py)
		   	 EXIT
			d)If you will Exit option choose then it will direct you to the homepage(homepage1.py).

	      2)USER LOGIN:- It will direct you to a User login page.(userloginpage2.py)
			a)In user login if you will type a wrong USER ID and PASSWORD then it will not open as validation is applied.
			b)When you will enter right password then it will direct you to the User welcome page(userwelcomepage.py) which consists of three options:- 
			c)"BUY" ,"SELL" and "Exit" option.
	           	  BUY will direct you to (userpage.py) SHOPPING PAGE where you can buy product and generate bill.
	          	  SELL will direct you to (userselling.py) SELLING PAGE where you can register for product you want to sell.

	      3)USER REGISTER:- It will direct you to a user registration page.(userregispage.py) incase you are not registered.
	      4)EXIT	:- It will exit you from the home page.

	   c)ABOUT US will consist of details of team members



	   d)CONTACT US will provide a drop down menu consisting of:
							1)CALL US :-It will direct you to a Call us page that provide our address and contact details.(contactuspage.py)
							2)EMAIL US:-It will direct you to a Email us page.(mailuspage.py)
	   e)HELP will provide a drop down menu consisting of:
							1)DEMO
           f)FEEDBACK will provide a drop down menu consisting of:
							1)SEND FEEDBACK:- SEND FEEDBACK will direct you to a  feedback page where you can send feedback.(feedbackpage.py)
							2)RATE US :- RATE US will direct you to a  rate page where you can send rating.(rateuspage.py)
	   e)EXIT will exit you from the home page.
	   




		
	
		