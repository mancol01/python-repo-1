 
# the is_divisible function from the text book 
def is_divisible(x, y):
    if x%y==0:
        return True
    else:
        return False
    # (Downey, 2015)
        
# an is power function taking two arguments x and y     
def is_power(x, y):
    # base case when the first argument x is equal to 1
    if x==1:
        return True
    #base case when the second argument in this case y being equal to 1
    elif y==1:
        return False
    # base case when the two arguments are equal 
    elif x==y:
        return True
    #to take the values of x and y positive and greater than 1
    elif y>1:
        if x>1:
            # is_power will call is is_divisible function, 
            if is_divisible(x, y)==False:
                return False
    # is_power calling itself
    return is_power(int(x/y), y)
    
    
        
print("is_power(10, 2) returns:", is_power(10, 2))
print("is_power(27, 3) returns:", is_power(27, 3))
print("is_power(1, 1) returns:", is_power(1, 1))
print("is_power(10, 1) returns:", is_power(10, 1))
print("is_power(3, 3) returns:", is_power(3, 3))



'''
Reference

Downey, A. (2015).Think Python; How to think like a computer scientist (2nd ed.). Needham, Massachusetts. Green Tea 	Press. https://my.uopeople.edu/pluginfile.php/1276543/mod_book/chapter/284277/TEXT%20-%20Think%20Python%202e.pdf
'''