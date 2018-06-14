#1.Create a list with user defined inputs
x = int(input("Enter the value of x="))
y = int(input("Enter the value of y="))
z = int(input("Enter the value of z="))

l = [x,y,z]

print(l)

#2.Addition of two lists
x = int(input("Enter the value of x="))
y = int(input("Enter the value of y="))
z = int(input("Enter the value of z="))

l1 = [x,y,z]
l2 = ['google",apple",facebook",microsoft",tesla']
l=l1+l2
print(l)

#3.Count the number of time an object occurs in a list
x=[1,2,3,4,5,1,6,1,7,1,8]
print(x.count(1))

#4.Create a list with numbers and sort it in ascending order
x=[4,6,2,1,7,3,8,5]
x.sort()
print(x)

#5.Given two one-dimensional arrays A&B which are unsorted. Write a program to merge them into a single sorted array C that contains every items from arrays A&B in ascending order list. 
a=[5,7,3,1]
a.sort()
print(a)

b=[2,6,4,9]
b.sort()
print(b)

c=a+b
c.sort()
print(c)

#6.Stack and Queue
print("Stack")
l1=["My","new","list"]
print(l1)
l1.append("of")
print(l1)
l1.append("python")
print(l1)
print(l1.pop())
print(l1)
print(l1.pop())
print(l1)
print("\n")
print("Queue")
l2=["Easy","is","Python"]
print(l2)
l2.reverse()
print(l2)
print(l2.pop())
print(l2)

#7. Count the even and odd numbers
l3=[1,2,3,4,5]
print(l3)
even=0;
odd=0;
for numbers in l3:
	if (numbers%2==1):
		odd=odd+1
	if (numbers%2==0):
		even=even+1
print('number of evens is:',even)
print('number of odds is:',odd)