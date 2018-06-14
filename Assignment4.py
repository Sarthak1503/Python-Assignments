#1.Find the length of tuple
t=(2,4,6,9,1)
print(len(t))

#2.Find the largest and smallest element of a tuple.
t=(2,4,6,8,1)
print(max(t))
print(min(t))

#3.Write a program to find the product os all elements of a tuple.
def pro(t):
    r=1
    for i in t:
        r=r*i
    return r
t=(1,2,3,4)
p=pro(t)
print(p)

#4.Calculate difference between two sets.
s1=set([1,2,4,6,9])
s2=set([2,3,4,5,7])
print(s1-s2)

#5.Print the result of intersection of two sets.
s1=set([1,2,5])
s2=set([2,3,4])
print(s1 & s2)

#6.Create a Dictionary to store names and marks of 10 students by user input.
d={}
for i in range(10):
    name=input('enter your name')
    marks=int(input('enter marks'))
    d[name]=marks
print(d)

#7.Sorting of Dictionary
d={'a':60,'b':100,'c':80}
print(d)
value_list=list(d.values())
print(value_list)
value_list.sort()
print(value_list)

#8.Count the number of occurence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
l=list("MISSISSIPPI")
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['P']=l.count('P')
print(d)

