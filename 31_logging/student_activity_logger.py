import logging

logging.basicConfig(
    filename="student_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("==== STUDENT ACTIVITY LOGGER ====")

n = int(input("How many students: "))
for i in range(n):
    name = input(f"Enter student {i + 1} name: ")
    marks = int(input(f"Enter marks {i + 1}: "))
    if marks < 45:
        logging.warning(f"{name} has low marks: {marks}")
    else:
        logging.info(f"{name} scored {marks} marks")
