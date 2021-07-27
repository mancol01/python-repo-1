# copied count down from text
'''
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
        
countdown()
'''
#value input for n
n = input('Enter the value of n:\n')
#converting n to interger
n= int(n)

#to count up with an increament of one
def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)
        
#to countdown with one
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        

#condition to run countdown when n >0 
if n>0:
    print('counting down!')
    countdown(n)
#condition to run countup when n<0
elif n<0:
    print('counting up!')
    countup(n)
# condition to choose when n is 0
else:
    if n==0:
        print('>>Press ')
        print('A to countup or B to countdown:\n')
        #take in a value to choose
        p =input('')
        if p=='a' or p=='A':
            n =int(n)
            print('counting up!')
            countup(n)
        elif p=='b' or p=='B':
            n = int(n)
            print('counting down')
            countdown(n)
        #return an error if the value chosen
        #is neither a or b
        else:
            print('ERROR - Please choose between A or B:')
            
