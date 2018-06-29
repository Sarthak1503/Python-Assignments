'''Ques.1. Extract the user id, domain name and suffix from the following 
		   email addresses. 
emails = "zuck26@facebook.com  page33@google.com jeff42@amazon.com"''' 

#METHOD 1: LIST TO TUPLE
import re
s= "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(s)
a=(result.group(1))
b=(result.group(2))
c=(result.group(3))
d=(result.group(4))
e=(result.group(5))
f=(result.group(6))
g=(result.group(7))
h=(result.group(8))
i=(result.group(9))
A=[a,b,c]
B=[d,e,f]
C=[g,h,i]
l=[tuple(A),tuple(B),tuple(C)]
print(l)

#METHOD 2: TUPLE TO LIST
import re
s= "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*)\.([a-z]+) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(s)
a=(result.group(1)),(result.group(2)),(result.group(3))
b=(result.group(4)),(result.group(5)),(result.group(6))
c=(result.group(7)),(result.group(8)),(result.group(9))
l=[]
l.append(a)
l.append(b)
l.append(c)
print(l)

'''Ques.2.Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
          text = "Betty bought a bit of butter, But the butter was so bitter,
          So she bought some better butter, To make the bitter butter better."'''
import re

s="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better"
p=re.compile(r"\b[Bb]\w+")
result=p.findall(s)
print(result)

'''Q.3.Split the following irregular sentence into words 
sentence = "A, very very; irregular_sentence"'''
import re

s="A, very very; irregular_sentence"
p=re.sub(r"[^\w]"," ",s)
b=re.sub(r"_"," ",p)
print(b)