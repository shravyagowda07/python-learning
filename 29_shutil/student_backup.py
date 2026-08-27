import shutil
import os

print("=== STUDENT BACKUP ===")

#Find the file
if os.path.exists("student.json"):
    print("student.json found.")

#Create a backup folder
if not os.path.exists("Backup"):
    os.mkdir("Backup")
    print("Backup folder created.")
else:
    print("Backup folder already exists.")

#copy the file
shutil.copy("student.json","Backup/student_copy.json")


#check copied file
if os.path.exists("Backup/student_copy.json"):
    print("Student data backed up succesfully!")

print("Backup file: Backup/student_copy.json")