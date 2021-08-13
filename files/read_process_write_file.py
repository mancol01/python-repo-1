#initialising lists to be appended with data
RD=[]   #read data
BL=[]   #Big list

#open files with input data and to receive processed data
fin=open('data.txt')
res=open('processed_data.txt','w')

#function to generate a dictionary from input data
def dict_gen(*args):  #fetching all arguments as parameters
    for line in fin:
        RD.append(line)
    print('\nData from input file:\n\n',RD)
    
    e=RD[0]     #e is a list of planet names as a string
    g=RD[1]     #g is a list of data planets as a string
    f=e.split(',')  #splitting the string in e to tuple f
    k=g.split('|[+]|')  #splitting the string in g to tuple k
    '''
    splitting the strings again in k and appending 
    them to Big List - contains lists of spltted data
    '''
    for i in k:
        t=i.split(',')
        BL.append(t)
    global z            #globalising z
    z=dict(zip(f,BL))   #zipping lists to Dictionary
    return z

dict_gen(fin,RD,BL)     #function call

print('\n\nGenerated - Dictionary:\n\n',z)

# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

#inverting function 
def invert_dict(z):
    #initialising dictionary to be appended
    inverse = dict()
    for key in z:
        val = z[key]
        #traversing through the list values
        for i in val:
            if i not in inverse:
                inverse[i] = [key]
            else:
                inverse[i].append(key)

    return inverse
    
    
out=invert_dict(z)
print('\nMy inverted dictionary:\n\n',out)

tup=out.items()     #making a tuple of inverted dict items
line_count=1  #initialising line_count to print line number


res.write(f"{'_'*40}\n\n")  #drawing a line in output file
res.write('lines 1 to 6 shows the format of data:\n')

'''
1: traversing the tuple, writing 0 indexed item mapped to 1
    and 0 index since it is in a list
2: writing the mapped items starting with count them mapped
    items
'''

print('\n\n')

for i in tup:
    print(f"{line_count}\t{i[0]}\t\t\t>_{i[1][0]}")
    res.write(f"{line_count}{' '*4}{i[0]}{'_'*12}>_{i[1][0]}\n")
    line_count+=1
    
res.write(f"{'_'*40}")  #drawing a closing line in output file
res.close()
