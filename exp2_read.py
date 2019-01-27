import sys
import os.path

if len(sys.argv) < 2:
    print("Please pass a <file_name> to read a file")
else:
    if os.path.exists(sys.argv[1]):
        userfile = open(sys.argv[1],"r")
        content = userfile.read()
        print("The contents of file are :- ")
        print(content)
        userfile.close()
    else:
        print("Error 404: File Not Found")