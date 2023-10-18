import os
# print(os.getcwd())     to print the path of current working directory
# os.mkdir("my_folder")   to create a folder
# os.rmdir("my_folder")    to delete a folder
# os.rename("my_folder","tttfolder1")     to rename a folder
# os.mkdir("D:\\ttttttt")         to create a folder on the another drive's path
# f=open("D:\\ttttttt\\read.txt","w")     to create a file on another path with f=open()
# os.remove("D:\\ttttttt\\read.txt")      to remove a file on another path with os.remove()
# os.rmdir("D:\\ttttttt")       to remove a folder on the another drive's path
# f=open("nnnn.txt","w")     to create a file in the current working directory with f=open()
# os.remove("nnnn.txt")     to remove a file in the current working directory with os.remove()

#reading,writing,append functions in a file:
f=open("myfile.txt","w")     #to create a file(write mode) by default it is read mode
# f=open("myfile.txt","a")        #append mode
# f.write("hey there")           #add some text or line to the existing file
f.write("Hello there,this is my Python file.")    #to write in a file
f.close()       #close it
f=open("myfile.txt","r")       #(read mode)
# print(f.read())            #to read a file
# print(f.read(10))        #to read the particular number of characters
# print(f.readline())
# f.close()                #close it

#Q.wap to count number of spaces in a text file
a=f.read()
c=0
for i in a:
     if i.isspace():
        c=c+1
print("Number of spaces: ",c)




"""1. r: open an existing file for a read operation.
2. w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
3. a: open an existing file for append operation. It won’t override existing data.
4. r+:  To read and write data into the file. The previous data in the file will be overridden.
5. w+: To write and read data. It will override existing data.
6. a+: To append and read data from the file. It won’t override existing data."""



"""
from typing import IO 
def create_file(filename):
    try:
       with open(filename, "w") as f:
           f.write("First line in the file\n")
       print("File "+filename+" created successfully")
    except IOError:
        print("Error: Unable to create the file "+filename)

def read_file(filename):
   try:
     with open(filename, "r") as f:
        contents = f.read()
        print(contents)
   except IOError:
     print("Error: Unable to read the file "+filename)

def append_file(filename, text):
  try:
    with open(filename, "a") as f:
      f.write(text)
    print("Text appended to "+filename+" successfully")
  except IOError:
    print("Error: Text not appended to "+filename)

def rename_file(filename, new_filename):
   try:
     os.rename(filename, new_filename)
     print("File "+filename+" renamed to "+new_filename+"successfully")
   except IOError:
     print("Error: could not rename file")

def delete_file(filename):
  try:
    os.remove(filename)
    print("File "+filename+" has been removed")
  except IOError:
    print("Error: could not remove file")

filename = "myfile.txt"
new_filename = "myfile1.txt"

create_file(filename)
read_file(filename)
append_file(filename, "The appended text")
read_file(filename)
rename_file(filename, new_filename)
read_file(new_filename)
delete_file(new_filename)      """