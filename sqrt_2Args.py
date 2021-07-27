
############################################


x=int(input("Enter the value of x:\n"))
a=int(input("Enter the value of a :\n"))

def my_sqrt(a, x):
    print(x)
    while True:
        y = (x + a/x) / 2.0
        print(y)
        if y == x:
            break
        x = y
    return y
        
        
print(my_sqrt(a, x))
