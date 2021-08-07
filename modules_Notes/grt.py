def greet(name):
    print('hello' + name)
    
    
if __name__ == "__main__":
    n=input('put name:\n')
    print('was not imported')
    greet(n)
else:
    print(' imported')
    