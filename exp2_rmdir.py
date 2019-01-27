import os

print("The dirlist is: ")
print(os.listdir(os.getcwd()))
folderName = input("Enter directory name to delete that directory : ")
if os.path.exists(folderName):
    os.rmdir(folderName)
    print("Directory deleted successfully!")
else:
    print("Directory does not exist")
print("The dirlist is: ")
print(os.listdir(os.getcwd()))