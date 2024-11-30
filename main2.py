new_file=open('New_File.txt','x')
new_file.close()

import os
print("Checking if my_file exists or no...")
if os.path.exist("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file=open("my_file.txt","w")
my_file.write("Hi! I am Penguin and I am 1 tr old")
my_file.close()

os.removed('blah.txt')

os.rmdir('Folder')