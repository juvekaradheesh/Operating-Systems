import os

print("The dirlist is: ")
print(os.listdir(os.getcwd()))
folderName = input("Enter directory name to create a new directory : ")
os.mkdir(folderName,744)
print("Directoy is created")
print("The dirlist is: ")
print(os.listdir(os.getcwd()))