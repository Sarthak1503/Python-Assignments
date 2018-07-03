#Write a program that accepts a sentence and calculate the number of upper case letters
# and lower case letters.
uppv=0
lowv=0
sum="Hello world"
for i in sum:
	if i.isupper():
	   uppv=uppv+1
	else:
		if i.islower():
			lowv=lowv+1
print('UPPER CASE=',uppv)
print('LOWER CASE=',lowv)