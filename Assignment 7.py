#1. Create a function to calculate area of a circle.
def Area(r):
    pi=3.14
    ar=pi*(r**2)
    return ar
rad=float(input('Enter radius for Circle'))
print('Area of circle is {}.'.format(Area(rad)))

#2.Write a function perfect and perform task

def Perfect(n):
    s=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s=s+i
    if s==n:
        print(n,'is a perfect number')
    return 
for i in range(1,1001):
    Perfect(i)

#3.Print multiplication table 12 using recursion

def table(n,i):
    if i==1:
        print('{} * {} = {}'.format(n,i,n*i))
        return
    else:
        table(n,i-1)
        print('{} * {} = {}'.format(n,i,n*i))
table(12,10)

#4.Using recursion write a function to calculate the power

def pow(a,b):
    if b==0:
        return 1
    else:
        return pow(a,b-1)*a
a=int(input('enter any number'))
b=int(input('enter thr power '))
print('Power of a to b is {}'.format(pow(a,b)))

#5.Write a function to find a factorial

def factor(n):
    if n==1:
        return 1
    else:
        return n*factor(n-1)
n=int(input('Enter any number for calculating factorial'))
v=factor(n)
d={}
d[n]=v
print('Factor of a number {} is {}'.format(n,v))
