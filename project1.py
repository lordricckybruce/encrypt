#!/bin/python3
'''
from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
	print("")
def encrypt():
	password=code.get()
	if password=="1234":
		screen2=Toplevel(screen)
		screen2.title("decryption")
		screen2.geometry("400x200")
		screen2.configure(bg="#00bd56")
	
		message=text1.get(1.0,END)
		decode_message=message.encode("ascii")
		base64_bytes=base64.b64encode(decode_message)
		decrypt=base64_bytes.decode("ascii")

		Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
		text2=Text(screen2,font="Rpbote 10",bg="white", relief=GROOVE,wrap=WORD,BD=0)
		text2.place(x=10,y=40,width=380,height=150)
		
		text2.insert(END,decrypt)
	elif password=="":
		messagebox.showerror("encryption","Input Password")
	elif password !="1234":
		messagebox.showerror("encryption","Invalid Password")

def main_screen():
	global screen
	global code
	global text1
	screen=Tk()
	screen.geometry("375x398")
	#ICON	
	image_icon=PhotoImage(file="keys.png")
	screen.iconphoto(False,image_icon)
	screen.title("PctApp")
	def reset():
		code.set("")
		text1.delete(1.0,END)
	Label(text="Enter text for encryption and decryption", fg="black",font=("calbri",13)). place(x=10,y=10)
	text1=Text(font="Robote 20",bg="white",relief=GROOVE, wrap=WORD,bd=0)
	text1.place(x=10,y=50,width=355,height=100)

	Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)
	code=StringVar()
	Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
	screen.mainloop()
	Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command="encrypt").place(x=10,y=250)
	Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command="decrypt").place(x=200,y=250)
	Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
main_screen()
'''
#import the pckage
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('mykey.key', 'mb'):
	mykey.write(key)

