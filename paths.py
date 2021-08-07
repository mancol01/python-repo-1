import os
 
 
cwd=os.getcwd()
print(cwd)

abs_path=os.path.abspath('words.txt') #gettimg the abspath for words.txt
'''
abspath does not depend on current directory
it begin with /
words.txt is a path called relative path 
'''

exists = os.path.exists('words.txt') # exists checks if a path or dir exists
print(exists)

isdir= os.path.isdir('/storage/emulated/0/uop/')#checks if its a dir
print(isdir)
