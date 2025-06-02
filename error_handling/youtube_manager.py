file=open('youtube.txt','w')

try:
    file.write('This is my first Python file. ')
finally:
    file.close() #not closing it means that your program is still holding the resource. This means that other processes cannot acquire that file until your program terminates

with open('youtube.txt','w') as file:
    file.write('This is my first Python file. using second method for writing the file')