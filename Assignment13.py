#Ques.1. Name and handle the exception occured in the following program:
a=3
try:
 if a<4:
    a=a/(a-3)
    print(a)
except Exception:
	print("Exception Occured")

#Ques.2.Name and handle the exception occurred in the following program: 
try:
	l=[1,2,3]
	print(l[3])
except Exception:
	print("Index Error")

'''Ques.3.What will be the output of the following code:
    Program to depict Raising Exception'''
 
try:
    raise NameError("Hi there")  # Raise Error
except Exception:
    print ("An exception")
    raise  # To determine whether the exception was raised or not

'''Output:Exception Occured
Index Error
An exception
Traceback (most recent call last):
  File "Assignment13.py", line 21, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there'''

'''Ques.4. What will be the output of the following code:
 Function which returns a/b'''
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

#Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

'''Output: -5
		 a/b result in 0'''
         
#Ques.5.Write a program to show and handle following exceptions: 
#1. Import Error
try:
	import Sarthak
	print("Studying in 3rd Year")
except Exception:
	print("Import Error")

#2. Value Error
try:
	x=int(input("Enter the value:"))
	print(x)
except Exception:
	print("Value Error")

#3.Index Error
try:
	l=[1,2,3]
	print(l[3])
except Exception:
	print("Index Error")

'''Ques.6.Create a user-defined exception AgeTooSmallError() that warns the user
  		  when they have entered age less than 18.
  		  The code must keep taking input till the user enters the appropriate age 
  		  number(less than 18).'''
class AgeTooSmallError(Exception):
 pass
a=1
while True:
  
 print("you have to enter the age 18 or more than 18")
 try:
  a=int(input("enter the age:"))
  if a<18:
   raise  AgeTooSmallError()
  print("Correct")
  break
     
 except Exception:
   print("Incorrect Age")
    

