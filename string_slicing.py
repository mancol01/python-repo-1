
topic = input('Enter the name of your favorite topic:\n')

print('The string to be sliced is:\n ', topic)
print('My first example, of slicing:')
cutOne=topic[:4]
print(cutOne)



print('The second example of slicing:')
cutTwo=topic[3::3]
print(cutTwo)

print('The third example of slicing:')
cutThree=topic[::-1]
print(cutThree)

print('The fourth example of slicing:')
cutFour=topic[2:-2:2]
print(cutFour)

print('The fifth example of slicing:')
print (topic[-2:-8:-2]+topic[7:10])


