import csv
from os.path import splitext
import re
import sys

def print_student_infos():
    students = []
    with open("test.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

    for student in sorted(students, key= lambda student: student["name"]):
        print(f"{student['name']} lives in {student['house']}")




def add_student_infos(*args):
    valid_args = []
    with open("test.csv") as file:
        reader = csv.DictReader(file)
        fieldnames =reader.fieldnames
        for arg in args:
            if arg in fieldnames:
                valid_args.append(arg)
    
    new_row = {}
    with open("test.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        for arg in valid_args:
            new_row[arg] = input(f"Enter {arg}: ")

        writer.writerow(new_row)



email = input("Email: ").strip()

try:
    username, domain = email.split("@")
except ValueError:
    sys.exit("Invalid")

if re.search("edu", domain):
    print("Valid")
else:
    print("Indvalid")