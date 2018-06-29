# Q.1- Write a Python program to read last n lines of a file.
f=open('file1.txt','r')
n=int(input('Enter the number of last lines'))
l=f.readlines()
for i in l[-n:]:
	print(i)
f.close()

# Q.2- Write a Python program to count the frequency of words in a file.

f=open('file1.txt','r')
d={}
for i in f:
	i=i.split(' ')
	for j in i:
		if j in d.keys():
			d[j]+=1
		else:
			d[j]=1
for i,v in d.items():
	print( i,' : ',v)
f.close()

# Q.3- Write a Python program to copy the contents of a file to another file.
with open("file2.txt","r",encoding="utf8") as f1:
    with open("file1.txt","w") as f2:
        for line in f1:
            f2.write(line)

'''Q.4- Write a Python program to combine each line from first file with the 
       corresponding line in second file.'''
with open("file1.txt") as fh1, open("file2.txt",encoding="utf8") as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

'''Q.5- Write a Python program to write 10 random numbers into a file. 
     Read the file and then sort the numbers and then store it to another file.'''
import random

with open("file1.txt", "w") as f:
    for i in range(10):
        numbers = str(random.randint(1, 100))
        f.writelines(numbers + '\n')
        print(numbers)

with open("file1.txt") as f1, open("file2.txt", "w") as f2:
    numbers = f1.read().split()
    numbers.sort()
    print(numbers)
    for n in numbers:
        f2.write(n)
        f2.write("\n")
