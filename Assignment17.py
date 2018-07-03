#Ques.1 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter
from tkinter import *
import sys
def display():
    sys.display()

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