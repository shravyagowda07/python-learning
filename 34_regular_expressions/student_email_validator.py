#Student email validator
import re
print("==== STUDENT EMAIL VALIDATOR ====")
name = input("Enter student name: ")
email = input("Enter email: ")
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    status = "Valid Email"
else:
    status = "Invalid Email"

print("Student: ", name)
print("Email: ", email)
print("Status: ", status)
