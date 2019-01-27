import sys
import os.path

if len(sys.argv) < 2:
    print("Please pass a <file_name> to open a file")
else:
    if os.path.exists(sys.argv[1]):
        userfile = open(sys.argv[1],"r+")
        content = userfile.read()
        print("The contents of file are :- ")
        print(content)
        userfile.close()
    else:
        userfile = open(sys.argv[1],"w+")
        print("File did not exist, We've created "+ sys.argv[1] + " for you")
        userfile.close()