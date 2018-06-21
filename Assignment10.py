#1.Create a class Animal as a base class and define method animal attribute.
# Create another class Tiger which is inheriting Animal and access the 
# base class method.

class Animal:
	def __init__(self,species):
		self.species=species
		
	def animal_attribute(self):
		print("tiger is:",self.species)
class Tiger(Animal):
	def display(self):
		print("Tiger is our national animal.")
		
		
species=input("enter the species of tiger")

a=Tiger(species)
a.display()
a.animal_attribute()

#2.What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
#print a.f(), b.f() 
#print a.g(), b.g() 

#this will give syntax error ..we need to place brackets after print.

#correct code=
print (a.f(), b.f()) 
print (a.g(), b.g())

#Output- Actual output= A B

#3. Create a class Cop. Initialize its name, age , work experience and designation.
#Define methods to add, display and update the following details. 
#Create another class Mission which extends the class Cop. 
#Define method add_mission _details. Select an object of Cop and access
#methods of base class to get information for a particular cop and
#make it available for mission.

class Cop:

	def __init__(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation
	
		
	def display(self):
		print("Details:")
		print(self.name)
		print(self.age)
		print(self.work_experience)
		print(self.designations)
		
	def update(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation

class Mission(Cop):
	fighter_planes=10
	tankers=3
	def add_mission_details(self):
		print("number of fighter planes:",self.fighter_planes)
		print("number of tankers:",self.tankers)
		
		
name=input("Name:")
age=int(input("Age:"))
work_experience=input("Work Experience:")
designation=input("Designation:")

a=Mission(name,age,work_experience,designation)
print("")
a.display()
print("")
a.add_mission_details()
print("")
a.update(input("Name:"),int(input("Age:")),input("Work Experience:"),input("Designation:"))
print("")
a.display()

#4.Create a class Shape.Initialize it with length and breadth Create the method Area. 
# Create class rectangle and square which inherits shape and access the method Area.

class Shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
		
		
	def area(self):
		self.result=self.length*self.breadth
		
		
class Rectangle(Shape):
	def arearect(self):
		print("area of rectangle:",self.result)
		
class Square(Shape):
	def areasq(self):
		print("area of square:",self.result)
		
		
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
c=Rectangle(length,breadth)
b=Square(length,breadth)
if length==breadth:
	b.area()
	b.areasq()
else:
	c.area()
	c.arearect()