 #1.Take 10 integers from user and print it on screen.
p=[]
for i in range(10):
	p.append(int(input("Enter any input")))

print(p)

#3.Create a list of integer elements by user input. Make a new list which will store square of elements of previous list. 
l=[]
s=[]
for x in range(3):
	l.append(int(input("Enter any Number:")))
for x in l:
        s.append(x**2)
print(l)
print(s)

#4.From a list containing int,strings and floats, make three lists to store them separatly. 
l=[1,3,5,4.5,'b',2.5,'a']
n=[]
f=[]
s=[]
for i in l:
    if type(i)==type(9):
        n.append(i)
    if type(i)==type(9.5):
        f.append(i)
    if type(i)==type('9'):
        s.append(i)
    
#5.Using range(1,101) make a list, containing even and odd numbers.
e=[]
o=[]
for i in range(1,101):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e,'\n',o)

  #6.Print the pattern.
for i in range (4):
    for j in range(i+1):
        print("*",end='')
    print('')

#7.Create a user defined dictionary and gets keys corresponding to the values 
# using for loop.
d={1:'a',5:'b','z':6}
for k,v in d.items():
	print(k,":",v)

#8.Perform Inputs And Search and deletion From User in a list.
l=[]
top=0
for x in range(5):
    x=int(input("enter the numbers:"))
    l.append(x)
print(l)
y=int(input("select any number you want to search"))
for x in l:
    if x==y:
        l.remove(x)
        top=1
print(l)
if top==0:
    print("the number you entered is not in the list")
        
#2.Write an infinte loop.

while(True):
    print("Hello World!")
