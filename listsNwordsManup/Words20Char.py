fin=open('words.txt')
din =[]

for line in fin:
    word = line.strip()
    if len(word)>15:
        print(word)
        din.append(word)
        
        
print(din)
new=open('WordListWithGreater15Chars.docx', 'w+')
#new.write('WordList.txt', 'a+')
new.write('[')

for i in din:
    new.write("'%s',"%(i))
    
new.write(']')
new.close()
    