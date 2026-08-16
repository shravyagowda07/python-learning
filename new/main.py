file = open("new/notes.txt", "r")
contents = file.read()
print(contents)
file.close()


with open("student.txt", "w") as file:
    file.write("Name: Shravya\n")
    file.write("College: KVG College\n")
    file.write("Language: Python\n")
    print("Data written succesfully!")


with open("student.txt", "r") as file:
    data = file.read()
    print(data)


with open("student.txt", "a") as file:
    file.write("Learning: File Handling\n")
    print("New data added.")


with open("student.txt", "r") as file:
    text = file.read()
words = text.split()
print("Total words:", len(words))


def notes_manager():
    while True:
        print("\n1. Add Student Note")
        print("\n2. View Notes")
        print("3. Exit")

        choice = input("Select an option (1-3):").strip()

        if choice == "1":
            note = input("Enter the note:")
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            print("Note saved succesfully!")

        elif choice == "2":
            try:
                
                with open("notes.txt", "r") as file:
                    content = file.read().strip()
                    if content: 
                        print("\n---Saved Notes---")
                        print("content")
                    else:
                        print("\nNotes file empty.")
            except FileNotFoundError:
                print("\nNo notes found yet. Add a note first!")

        elif choice == "3":
            print("Exiting Notes Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3")
if __name__ == "__main__":
    notes_manager()


day_number = "Day 11"
topic = "File Handling"
time = "1 hour"
learn = "Today I learned how to read and write files using Python."
with open("daily_progress.txt", "a") as file:
    print(f"{day_number}\n")
    print(f"{topic}\n")
    print(f"{time}\n")
    print(f"{learn}\n")
