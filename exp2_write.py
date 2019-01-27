import sys
import os.path

if len(sys.argv) < 2:
    print("Please pass a <file_name> to write to a file")
else:
    if os.path.exists(sys.argv[1]):
        userfile = open(sys.argv[1],"a+")
        userfile.seek(0)
        content = userfile.read()
        print("The contents of file are :- ")
        print(content)
        choice = input("Do you want to write more to file ? (y/n)")
        if choice == 'y':
            newInput = input("Enter text here :")
            userfile.write("\n" + newInput)
        else:
            print("ok thanks!")
        userfile.close()
    else:
        userfile = open(sys.argv[1],"w+")
        print("File did not exist, We've created "+ sys.argv[1] + " for you")
        choice = input("Do you want to write to file ? (y/n)")
        if choice == 'y':
            newInput = input("Enter text here :")
            userfile.write(newInput)
        else:
            print("ok thanks!")
        userfile.close()