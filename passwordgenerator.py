from tkinter import *
from tkinter import filedialog
import string
import random
import pyperclip

root = Tk()
root.geometry('294x290')
root.title('Password Generator')
root.resizable(0,0)
root.config(bg="black")

def generatePassword():
    sml_alpha = string.ascii_lowercase
    cpt_alpha = string.ascii_uppercase
    spcl_char = string.punctuation
    num = string.digits

    passwordmix = cpt_alpha+sml_alpha+spcl_char+num
    headingpasswordLength = int(Password_length_box.get())

    password = random.sample(passwordmix,headingpasswordLength)
    Password_field_box.insert(0,password)

def delete_password():
    Password_field_box.delete(0, "end")

def copy():
    password_copy = Password_field_box.get()
    pyperclip.copy(password_copy)

def save():
    file_types = [("Text Files", "*.txt"),("All Files", "*")]
    file_path = filedialog.asksaveasfilename(filetypes=file_types)
    passworddata = Password_field_box.get()
    file_writer = open(file_path, mode= "w")
    file_writer.write(passworddata)
    file_writer.close()

heading = Label(root, text="Password Generator", font=('arial',20, 'bold'), bg="black", fg="white")
heading.grid(pady=5,padx=10)

heading2 = Label(root, text="Strong Password", font=('arial',10, 'bold'), bg="black", fg="white")
heading2.grid(pady=5)

headingpasswordLength = Label(root, text="Enter Password Length", font=('arial',10, 'bold'), bg="black", fg="white")
headingpasswordLength.grid(pady=5)

Password_length_box = Spinbox(root, from_=4, to=12, font=("arial", 15, "bold"))
Password_length_box.grid(pady=5)

randompasswordbtn = Button(root, text="Random Generate Password", font=('arial',10, 'bold'), bg="black", fg="white",command=generatePassword)
randompasswordbtn.grid(pady=5)

Password_field_box = Entry(root, width=20, bd=2, font=('arial',15, 'bold'), bg="black", fg="white")
Password_field_box.grid(pady=5)

cancelbtn = Button(root, text="Cancel", font=("arial",10, "bold"), bg="black", fg="white", command=lambda :delete_password())
cancelbtn.place(x=50,y=232)

copybtn = Button(root, text="Copy", font=("arial",10, 'bold'), bg="black", fg="white", command=lambda :copy())
copybtn.place(x=129,y=232)

savebtn = Button(root, text="Save", font=("arial",10, 'bold'), bg="black", fg="white", command=save)
savebtn.place(x=200,y=232)

root.mainloop()