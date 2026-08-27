#shutil.copy("notes.txt", "backup_notes.txt")
#shutil.copy2("notes.txt", "backup_notes.txt")
#shutil.copytree("MyFolder", "MyFolder_Backup")
#shutil.move("notes.txt", "Documents/notes.txt")
#shuti.rmtree("OldFolder")


import shutil
import os

print("SHUTIL PRACTICE")

#create a test folder
if not os.path.exists("Test"):
    os.mkdir("Test")

#Create a file
with open("notes.txt", "w") as file:
    file.write("Python shutil practice")

#copy the file
shutil.copy("notes.txt", "Test/notes_copy.txt")

print("File copied successfully!")

#check copied file
if os.path.exists("Test/notes_copy.txt"):
    print("Copy exists")

#Move the copied file
shutil.move("Test/notes_copy.txt", "Test/moved_notes.txt")

print("File moved successfully!")

print("\nFiles inside Test:")
print(os.listdir("Test"))