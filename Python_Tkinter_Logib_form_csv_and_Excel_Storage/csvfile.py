# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:45:48 2021

@author: HP
"""

from  tkinter import *
import tkinter as tk 
import csv 
from csv import writer


main=Tk()
main.title("details")
main.geometry("800x500")
main.config(highlightbackground="black",highlightthickness=2)


    
def submit():
    y=name.get()
    z=user.get()
    z1=passEntry.get()
    y1=emailentry.get()
    print(y)
    print(z)
    print(z1)
    print(y1)
    
    with open('demo.csv','w',newline='') as f:
        csv_writer=writer(f)
        csv_writer.writerows([[y],[z],[z1],[y1]])
    
    
    
  

    
        


frame1=LabelFrame(main,text='login details').pack(expand='yes',fill='both')
Label(frame1,text="Name").place(x=50,y=30)
Label(frame1,text="username").place(x=50,y=70)
Label(frame1,text="Password").place(x=50,y=110)
Label(main,text="mail id").place(x=50,y=150)

'''frame2=LabelFrame(main,text='oter details').pack(expand='yes',fill='both')'''
name=Entry(frame1)
name.place(x=250,y=30)

user=Entry(frame1)
user.place(x=250,y=70)

password=StringVar()
passEntry=Entry(frame1,textvariable=password,show='*')
passEntry.place(x=250,y=110)

emailentry=Entry(frame1)
emailentry.place(x=250,y=150,width=250)



Button(frame1,text="subscribe",command=submit).place(x=300,y=250)
main.mainloop()
        

    

         
    
    
  
         
    
    
    

    

