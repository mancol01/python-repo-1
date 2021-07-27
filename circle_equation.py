# the program will return the equation of a circle given the coordinates of center and radius 

g = int(input("Enter the x-coordinate of the centre:\n"))
f = int(input("Enter the y-coordinate of the center:\n"))
r = int(input("Enter the radius of the circle:\n"))

#The function circle_eq to return the equation of a circle using parameters g,  f and r
def circle_eq(g, f,  r):
    #base case when the center is at the origin
    if g==0 and f==0:
        print("The equation of a circle with center(0,0) and radius = %s units is:"%(r))
        return print("x^2 + y^2=%s"%(r**2))
    elif g<0 and f>0:
        print("The equation of a circle with center(%s,%s) and radius = %s units is:"%(g, f, r))
        return print("(x+%s)^2 + (y-%s)^2=%s"%(-g, f, r**2))

    elif g<0 and f==0:
        print(f==0)
        print(g, f) 
        print("The equation of a circle with center(%s, 0) and radius = %s units is:"%(g,  r))
        return print("(x+%s)^2 + y^2=%s"%(-g,  r**2))
    elif g==0 and f<0:
        print("The equation of a circle with center(0, %s) and radius = %s units is:"%(g,  r))
        return print("x^2 + (y+%s)^2=%s"%(-f,  r**2))
    elif g==0 and f>0:
        print("The equation of a circle with center(0, %s) and radius = %s units is:"%(f,  r))
        return print("x^2 + (y-%s)^2=%s"%(f,  r**2))
    elif g<0 and f<0:
        print("The equation of a circle with center(%s, %s) and radius = %s units is:"%(g, f, r))
        return print("(x+%s)^2 + (y+%s)^2=%s"%(-g, -f, r**2))
    elif g>0 and f>0:
        print("The equation of a circle with center(%s, %s) and radius = %s units is:"%(g, f, r))
        return print("(x-%s)^2 + (y-%s)^2=%s"%(g, f, r**2))
    elif g>0 and f<0:
        print("The equation of a circle with center(%s,%s) and radius = %s units is:"%(g, f, r))
        return print("(x-%s)^2 + (y+%s)^2=%s"%(g, -f, r**2))
    
circle_eq(g, f,  r)

