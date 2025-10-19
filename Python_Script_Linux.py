import os

file = input("Enter a file name: ")

if os.path.isfile(file):
    print("The file exist")
else:
    print(f"The file does not exist\nCreating the file...\nDone.")
    os.system("touch {}".format(file))
    os.system("ls")