import sys

fin=open('words.txt')
din =[]

for line in fin:
    word = line.strip()
    din.append(word)
    #print(word)
    
    
print(din)
new=open('WordList.docx', 'w+')
#new.write('WordList.txt', 'a+')
new.write('[')

for i in din:
    new.write("'%s',"%(i))
    
new.write(']')
new.close()