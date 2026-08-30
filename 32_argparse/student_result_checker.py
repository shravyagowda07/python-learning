import argparse
parser = argparse.ArgumentParser(description="Student Result Checker")

parser.add_argument("name")
parser.add_argument("marks", type=int)
parser.add_argument("branch")

args = parser.parse_args()

result = "PASS" if args.marks>= 40 else "FAIL"

print("=== STUDENT RESULT ===")
print("Name:", args.name)
print("Marks:", args.marks)
print("Branch:", args.branch)
print("Result:", result)

