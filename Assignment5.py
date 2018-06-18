#1.Check the year is leap or not
year=int(input("Enter the year:"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not a leap year")
else:
    if year%4==0:
        print("leap year")
    else:
        print("not a leap year")

#2.Take length and breadth input from user and check whether the dimensions
#  are of square or rectangle.
x=int(input("Enter the length:"))
y=int(input("Enter the Breadth:"))
if x==y:
    print("Square")
else :
    print("Rectangle")

#3. Take the input age of 3 people and determine oldest and youngest among them.
x=int(input("Enter the age of person x:"))
y=int(input("Enter the age of person y:"))
z=int(input("Enter the age of person z:"))
if x>y:
    if x>z:
        print("x is older")
    else:
        print("z is older")
else:
    if y>z:
        print("y is older")
    else:
        print("z is older")

 #4.Write an if statement to lets competitor know which of these prizes they won.
a=int(input("Enter the points:"))
f=1
if a<200:
    if 1<a<50:
        f=0
        print("No Prize")
    elif 50<a<150:
        prize="Wooden Box"
    elif 150<a<180:
        prize="Book"
    elif 180<a<200:
        prize="Chocolate"
    if f!=0:
        print("Congratulations! You won a {}".format(prize))


#5.Print total cost after getting discount.
n=int(input("Enter the n units:"))
p=n*100
if p>1000:
    disc=p*.1
    r=p-disc
    
    print('Total price=',r)
