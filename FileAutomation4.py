#check given path is absolute or not

from sys import *
import os
import time

def DirectoryTravel(Dirname):
    print("We are going to scan the directory :",Dirname)

    flag = os.path.isabs(Dirname)

    if flag == False:
        Dirname = os.path.abspath(Dirname)

    exist = os.path.isdir(Dirname)

    if exist:

        for foldername, subfoldername, filename in os.walk(Dirname):
            print("Current Directory :",foldername)

            for subname in subfoldername:
                print("Subfolder name is :",subname)

            for fname in filename:
                print("File name is :",fname)
                print(os.path.abspath(fname))
                #print(fname, " : ",os.path.getsize(foldername+"/"+fname), "bytes")

    else:
        print("Invalid path")

def main():
    print("-------------------Automation Script----------------------")

    print("Automation Script Name :",argv[0])

    if(len(argv)  != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):         # flag for displaying help
        print("This automation script is used to perform file automations ")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Name_Of_Script First_Argument ")
        print("Example : Demo.py Marvellous") #marvellous directory name means folder name 
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as :",endtime - starttime)

        

if __name__ == "__main__":
    main()

#python FileAutomation1.py Directory_name