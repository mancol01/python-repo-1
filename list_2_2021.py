'''
Part 1

Write a Python program that does the following. 

Create a string that is a long series of words separated by spaces. The string is your own creative choice. It can be names, favorite foods, animals, anything. Just make it up yourself. Do not copy the string from another source. 

Turn the string into a list of words using split. 

Delete three words from the list, but delete each one using a different kind of Python operation. 

Sort the list. 

Add new words to the list (three or more) using three different kinds of Python operation. 

Turn the list of words back into a single string using join. 

Print the string. 


Part 3

Describe your experience so far with peer assessment of Programming Assignments.

How do you feel about the aspect assessments and feedback you have received from your peers?
How do you think your peers feel about the aspect assessments and feedback you provided them?
'''

#The string of names of wild animals
a = 'lion cheetah elephant buffalo eland kudu impala leopard hyena zebra giraffe tiger'

#for defining where to separate the characters
delimiter = ' '

# for spliting the string with delimiter as argument
b = a.split(delimiter)

print('I was a string of :\n',  a)
#for printing the newlist 
print('Now I am a new list:\n')
print(b)

print('\n')
c=b.pop(9)
print('I popped:', c)
print('Now I am:\n', b)

print('\n')
d=b.remove('giraffe')
print('Look, I removed something here')
print('Now I am:\n', b)

print('\n')
del b[2]
print('Yes!, I deleted another element')
print('At last I am:\n', b)

#For sorting the list
print('\n')
print('I am sorted now:\n')

#for sorting the list in ascending order 
print(sorted(b, reverse=False))

# adding words to the list 
#using the append function 
w='kangaroo'
b.append(w)
print('\n')
print('We appended the list with %s:\n%s'%(w,  b))

#using the extend function 
x=['monkey', 'fox']
b.extend(x)
print('\n')
print('We extended the list with:\n \n %s \n \n to get :\n \n%s'%(x, b))

#using the + operator
y=['Rhinoceros']
z=b+y
print('\n')
print('We added the list:\n \n %s \n \nwith \n \n%s\n \n to get :\n \n%s'%(b ,y , z))
# to reduce the elements of a list to a single string

print('\n')
opt=delimiter.join(z)
print('Our new string is:\n \n', opt)