from datetime import datetime, timedelta
print("==== STUDY TRACKER ====")
name = input("Enter student name: ")
study_hours = int(input("Enter study hours: "))

print("==== STUDY SESSION ====")

print("Student: ", name)
print("Study Hours: ", study_hours)

now = datetime.now()
print("\nDate: ", now.strftime("%d-%m-%Y"))
print("\nTime: ", now.strftime("%I:%M %p"))

next_day= now + timedelta(days=1)
print("\nNext Study Date: ", next_day.strftime("%d-%m-%Y"))