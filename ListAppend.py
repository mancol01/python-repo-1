#The list for input values to be modified
TBM = [1, 2, 3, 4, 5]
#Initiating the list to be modified after processing
Out = []

#The function to modify the intergers in a list to perfect cubes 
def perfectCube(T):
    #the for loop to transverse through the loop
    for num in T:
        # the statement for for processing elements (positive integers to new element (perfect cubes)
        P = num**3
        #for appending the list 
        Out.append(P)
        
#calling    the function   
perfectCube(TBM)
#printing the new appended list
print(Out)


'''

Our program has an object of type list with intergers from one to five. The object is referenced to the variable (alias) 'TBM'. The object has and identity that is mapped to the alias. In the function call we have the argument 'TBM' that is has the identity of the list and in simple we have a list in the function call. On the function header we also have a parameter 'T' different from 'TBM'. T parameter refers to argument 'TBM' for what to be used inside the body. By referring, they to each other, 'TBM' becomes an object with the identity similar to the identity of the list in memory. That is T = TBM = [1, 2, 3, 4, 5] = <an identity>. So TBM = [1, 2, 3, 4, 5] are now same objects with same identity at function level. The list now has two aliases 'T'and 'TBM'. Yes, by writing 'TBM' and 'T' as argument and parameter respectively, we have referenced them to each other. 


'''