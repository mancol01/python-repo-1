# the input to fetch in the name of the month
x=input('Fullname of the month:\n')
#converting to string datatype
x=str(x)
#converting the string to lower case
x=x.lower()

#the universal set to hold months in a year
u_s={'january', 'february', 'march', 'april', 'may', 'june', 'july',
     'august', 'september', 'october', 'november', 'december'}

# a list to hold cold months in my country Zimbabwe
c_m=['may', 'june', 'july', 'august']

#the fuction to seperate or classify cold and warm months with parameter x
def winter(x):
    if x in u_s:
        if x in c_m:
            print('Its cold this time in Zimbabwe, include warm clothes')
        else:
            print('Its warm this time in Zimbabwe, wear loose clothes')
    else:
        print('Your month is unknown, try again')

#the function call with argument x from input function
winter(x)
