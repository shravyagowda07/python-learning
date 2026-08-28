from pathlib import Path

print("=== STUDENT FILE ORGANIZER ===")

#Current directory
print("Current folder:")
print(Path.cwd())

#check whether student.json exists
student_file = Path("student.json")
print(student_file.exists())

##Create a folder
folder = Path("Student_Data")
folder.mkdir(exist_ok = True)

print("\nStudent data folder exists:", folder.exists())

#create a file
info_file = folder/"info.txt"
info_file.write_text("Student Data Managment\nCreated using Python Pathlib.")

print("\nFileCreated:", info_file.is_file())

#Read the file
print("File Content:")
print(info_file.read_text())

#Display whether student.json exists.
print(f"student.json exists: {student_file.exists()}")

#Show files and folders
print("\nCurrent Directory contents:")
for item in Path.cwd().iterdir():
    print("=", item.name)