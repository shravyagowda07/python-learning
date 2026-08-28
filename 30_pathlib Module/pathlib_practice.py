from pathlib import Path

print("=== PATHLIB PRACTICE ===")

#current directory
print("Currrent folder:")
print(Path.cwd())

#Create folder
folder = Path("Practice")
folder.mkdir(exist_ok=True)

print("\nPractice folder exists:", folder.exists())
print("Is it a folder?", folder.is_dir())

#create a file
file = folder/"notes.txt"
file.write_text("I am learning Python pathlib.")

print("\nFilecreated:", file.is_file())

#Read the file
print("File content:")
print(file.read_text())

#Show files and folders
print("\nCurrent directory contents:")
for item in Path.cwd().iterdir():
    print("-", item.name)