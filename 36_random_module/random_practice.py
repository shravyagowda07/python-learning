#random.randint

import random
number = random.randint(1, 10)
print(number)

#random.choice
import random
students = ["Kavya", "Bhavya", "Rahul", "Amith"]
winner = random.choice(students)
print("Selected student: ", winner)


#random.shuffle
import random
student = ["A", "B", "C", "D"]
random.shuffle(student)
print(student)


#random.sample
import random
students = ["John", "David", "Ram", "Deepak"]
selected = random.sample(students, 2)
print(selected)



import random

print("==== RANDOM MODULE PRACTICE ====")
print("Random number:", random.randint(1, 100))

students = ["Ramya", "Kavya", "Bhavya", "Shravya", "Rahul"]
print("Random student:", random.choice(students))

random.shuffle(students)
print("Shuffled students: ", students)

team = random.sample(students, 3)
print("Random team: ", team)