'''
Part 2

Provide your own examples of the following using Python lists. Create your own examples. Do not copy them from another source. 

Nested lists 
The “*” operator 
List slices 
The “+=” operator 
A list filter 
A list operation that is legal but does the "wrong" thing, not what the programmer expects  
Provide the Python code and output for your program and all your examples. 
'''
#Nested lists

x=[1, 100, 1000, 10000]
r=[.9, .99, .999]
print('list x:\n', x)
print('list r:\n', r)
x.append(r)

print('\n')
print('This is a nested list:\n', x)

#using the '*' operator

y=r*2

print('\n')
print("The new list after using the '*'operator:\n", y)

#list slicing 
z=x[4:5]

print('\n')
print("The list 'x' sliced from index 3 to 4:\n", z)
#Using the += operator
nWL = []
def addValue(Rr5):
    for n in Rr5:
        n+=.1
        nWL.append(n)
    
    
addValue(y)

print('\n')
print('Our new list after adding value:\n', nWL)

    
#using filter 
#merging all list to make a big list 
longList = x + y + z + nWL

print('\n')
print('The long list is:\n', longList)


#initialising a new list 
nDp=[]
#for filtering elements of float datatype
def filtration(c):
    for i in c:
        
        if type(i) == float:
            nDp.append(i)
        #to handle element of nested lists
        elif type(i) == list:
            for j in i:
                nDp.append(j)

    
    
filtration(longList)

print('\n')
print('The filtrate of floats:\n', nDp)

#A legal list operation but outputting unexpected results 

print('\nThe sorted list of floats:\n', nDp.sort())

'''
termuxblack > python CS1001_LJ_U6P2.py
list x:
 [1, 100, 1000, 10000]
list r:
 [0.9, 0.99, 0.999]


This is a nested list:
 [1, 100, 1000, 10000, [0.9, 0.99, 0.999]]


The new list after using the '*'operator:
 [0.9, 0.99, 0.999, 0.9, 0.99, 0.999]


The list 'x' sliced from index 3 to 4:
 [[0.9, 0.99, 0.999]]


Our new list after adding value:
 [1.0, 1.09, 1.099, 1.0, 1.09, 1.099]


The long list is:
 [1, 100, 1000, 10000, [0.9, 0.99, 0.999], 0.9, 0.99, 0.999, 0.9, 0.99, 0.999, [0.9, 0.99, 0.999], 1.0, 1.09, 1.099, 1.0, 1.09, 1.099]


The filtrate of floats:
 [0.9, 0.99, 0.999, 0.9, 0.99, 0.999, 0.9, 0.99, 0.999, 0.9, 0.99, 0.999, 1.0, 1.09, 1.099, 1.0, 1.09, 1.099]

The sorted list of floats:
 None
termuxblack >
'''
