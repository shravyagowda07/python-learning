#re.search() method
import re
text = "My name is Rahul"
result = re.search("Rahul", text)
if result:
    print("Name found!")

#re.findall() method
import re
text = "My marks are 90, 85, 75 and 88"
numbers = re.findall(r"\d+", text)
print(numbers)

#re.match() method
import re
name = "Amith"
result = re.match("Ami", name)
if result:
    print("Match found!")


import re
text = "student Kavya scored 90 marks. Rahul scored 85 marks."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)
names = re.findall(r"[A-Z][a-z]+", text)
print("Words starting with capital letters:", names)


