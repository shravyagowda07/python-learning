

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("age", type=int)

args = parser.parse_args()

print("Name:", args.name)
print("Age:", args.age)