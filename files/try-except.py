'''
It is wise to use try and except for handling codes that can raise errors. We put our code im the body of the try statement in case if an error that has nothing to do with programming occurs. If the error occurs it is going to handeled by the except statement (Programiz, 2021).
Catching exceptions can help to handle file opening errors for example, when files do not exist in the directory. By using except statement, we can return a detailed error message to the user on what has occured. 
Example 1
Using try and except to remove error traceback information that is printed after an error is found. In our directory there is no thinkpython.pdf and anticipate a FileNotFoundError.
The Code:
'''

fn=open('thinkpython.pdf')
show=fn.readline()
print(show) 
'''
Output:

termuxblack > python DaU8Cs1001.py
Traceback (most recent call last):
  File "/storage/emulated/0/uop/wtwewwwq/DaU8Cs1001.py", line 1, in <module>
    fn=open('thinkpython.pdf')
FileNotFoundError: [Errno 2] No such file or directory: 'thinkpython.pdf'
termuxblack >
'''

#Using try
try:
  fn=open('thinkpython.pdf')
  show=fn.readline()
  print(show)
except FileNotFoundError as error:
  print(error)
  

'''
Output

termuxblack > python DaU8Cs1001.py
[Errno 2] No such file or directory: 'thinkpython.pdf'
termuxblack >

We have removed many error details that were previously display to make it simple.

Example 2
Handling a UnicodeDecodeError using try by customising the type of the error in the head of the except statement. This error occurs when the interpetor cannot open (decode) the type of a file (). This time we put the thinkpython.pdf file but we know our interpetor can not decode the file at the moment. This time we anticipate a UnicodeDecodeError.
The Code
'''


try:
  fn=open('thinkpython.pdf')
  show=fn.readline()
  print(show)
except FileNotFoundError as error:
  print(error)


'''
Output
termuxblack > python DaU8Cs1001.py
Traceback (most recent call last):
  File "/storage/emulated/0/uop/wtwewwwq/DaU8Cs1001.py", line 43, in <module>
    show=fn.readline()
  File "/data/data/com.termux/files/usr/lib/python3.9/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 11: invalid start byte
termuxblack >

Using try and except to handle UnicodeDecodeError

The Code
''''
try:
  fn=open('thinkpython.pdf')
  show=fn.readline()
  print(show)
except FileNotFoundError as error:
  print(error)
except UnicodeDecodeError:
  print('Oops! The file type cannot be opened.')
  

'''
Output
termuxblack > python DaU8Cs1001.py
Oops! The file type cannot be opened.
termuxblack >
Explanation
We can now see that instead of printing much detai,the except was classified to handle anticipated error and we did not removed the previous except which was skipped due different type of error.

Example 3
We are going to use a file called process_math.txt which will have some integer, strings and boolean expressions some string to anticipate a _______ after evaluating using eval function. We will write the results in the results.txt. 
'''

fldir=open('process_data.txt')
res=open('results.txt','w+')
count=1

res.write(str(count) +'\t\t'+'It begins here:\n--->>\n')
for ln in fldir:
  try:
    r=eval(ln)
    print(r)
    
    res.write(str(count) +'\t\t'+f'{r}\n')
    count+=1
  except:
    
    res.write(str(count) +'\t\t'+'This is new, I cant process\n')
    count+=1
res.write(f"{count}---->> \n{count+1} Yes, its done!")
res.close()
'''

Output
If our program encounters any challenge, it goes to the except statement where it will write ' this is new I cant process'


If i was writing a large program that opens many files, for example, I am processing images for my classification algorithm. With a large dataset of uncleaned data, for instances, some images are corrupt, some are small, some are of different extension, by using try and except, I can automize my program to keep on going even if the data does not meet the requiremnts.
If there are no files in the directory, using try will make the code continue searching for other files and avoid focusing on files that no longer exists.
The same will work if the program mananges to find files in a pull different types of files but can not decode(open) the files. Using try and except will keep the code going looping and not concentrating on errors.
Lasty, while processing, the program can fail to process some of the images for program. Using try and except will stop the code from concentrating on the errors of processing and also keep going



References
Programiz.(2021, Jan 6).Python Exception Handling:
try...catch..finally | Python for Beginners [Video]. YouTube. https://youtu.be/brICUKrzVR0

'''

