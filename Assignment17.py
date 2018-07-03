#Ques.1 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter
from tkinter import *
import sys
def exit():
    sys.exit()

root=Tk()
root.title("My First GUI ")
root.geometry("400x400")
root.resizable(False,False)
a=Label(root,text="Hello World !",width=150)
a.pack()
b=Button(root,text="Exit",command=exit)
b.pack()

root.mainloop()

'''Ques.2 Write a python program to in the same interface as above and create a action
          when the button is click it will display some text.'''

import tkinter
from tkinter import *

def show():
    print("Welcome to our Website")

root= Tk()
root.title("GUI")
root.geometry("250x250")
b=Button(root,text="Submit",bg="navy",fg="White",command=show)
b.pack()

root.mainloop()

'''Ques.3 Create a frame using tkinter with any label text and two buttons.
          One to exit and other to change the label to some other text.'''
import tkinter
from tkinter import *
import sys
def Change():
    label.config(text= "It's GUI")
root = Tk()
label = Label(root ,text="Hello Guys")
label.grid(row = 0,)
a = Button(root, text="Change" ,command=Change)
a.grid(row= 1)
b = Button(root, text="Exit" ,command=sys.exit)
b.grid(row= 2)
root.mainloop()


#Ques.4 Write a python program using tkinter interface to take an input in the GUI program and print it.

import tkinter
from tkinter import *

def show():
    print(entry.get())

root=Tk()
root.title("GUI")
root.geometry("400x400")


entry=Entry(root,width=40)
entry.pack()
b=Button(root,text="Submit",width=10,bg="grey",command=show)
b.pack(side= TOP)

root.mainloop()