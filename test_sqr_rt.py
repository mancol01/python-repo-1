
import math

#x=int(input("Enter the value of x:\n"))
#to fetch the value of a, to be calculated the square root 
a=int(input("Enter the least value of 'a' you want to output up to 25:\n"))

#the function my_sqrt that has the parameter a, and takes the argument a from the function call



def my_sqrt(a):
    #initializing x to be a which will be used in the while statement 
    x=a
    #while statement to iterate the value of y 
    while True:
        y = (x + a/x) / 2.0
        #the conditional statement to break the loop when you and x are equal.
        if abs(y-x) < epsilon:
                break
        #to update the value of x to used from second substitution onwards 
        x = y
    #returns y when the while loop breaks
    return y
    

 
 
epsilon=0.0000001

#the while expression will iterate through the functions, increamenting 'a' with 1 up to 25
while a<26:
    #a result from the function my_sqrt
    r=my_sqrt(a)
    #a result from square root from the built square root function 
    m=math.sqrt(a)
    #to find the difference between the two function 
    h= abs(m-r) 
    
    print('a = %d | my_sqrt(a) = %s | math.sqrt(a) = %s | diff = %s' % (a,  r, m, h))
    
    a+=1
    
    