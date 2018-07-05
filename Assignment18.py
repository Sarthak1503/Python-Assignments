'''Ques.1 Create a dict with name and mobile number.
Define a GUI interface using tkinter and pack the label and 
create a scrollbar to scroll the list of keys in the dictionary.'''
class Person(object):
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile 
 
people = [Person("Name", "Sarthak"), Person("mobile number","474756590")]
mobile  = dict([ (p.name, p.mobile ) for p in people ])
print(mobile )

'''tkinter provides us with a variety of common GUI elements
 which we can use to build our interface – such as buttons, menus and various
 kinds of entry fields and display areas.
 We call these elements widgets.
 We are going to construct a tree of widgets for our GUI
 each widget will have a parent widget, all the way up to the root window 
 of our application.''' 

from tkinter import *
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for line in range(10):
 l.insert(END,"this is statement"+str(line))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
root.mainloop()



'''Ques.2 In the same tkinter file as created above, 
 		  create a function to insert items into the dictionary.'''
from tkinter import *
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for line in range(10):
 l.insert(END,"item"+str(line))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview)
root.mainloop()

from tkinter import *

items = ['1','2','3']

root = Tk()

buttons = {}

buttons['1st item'] = Button(root, text = '1st item', command = lambda: print('1st item'))
buttons['2nd item'] = Button(root, text = '2nd item', command = lambda: print('2nd item'))
buttons['3rd item'] = Button(root, text = '3rd item', command = lambda: print('3rd item'))

buttons['1st item'].pack()
buttons['2nd item'].pack()
buttons['3rd item'].pack()

root.mainloop()