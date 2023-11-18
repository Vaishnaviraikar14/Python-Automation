from sys import *
import os

def DirectoryTravel(Dirname):
    print("We are going to scan the directory :",Dirname)

    for foldername, subfoldername, filename in os.walk(Dirname):
        for fname in filename:
            print(fname)

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
        DirectoryTravel(argv[1])

if __name__ == "__main__":
    main()

#python FileAutomation1.py Directory_name