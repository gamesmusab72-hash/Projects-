
# This is my first mini project that I started and progressed with the course CS50 
# And i will be adding more mini projects to this file as I progress in the course and learn new concepts and skills.
import csv
import os


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


def manage_students():
    last_id = 0
    if os.path.exists("students.csv"):
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    last_id = int(row[0])

    while True:
        try:
            numOfStudents = int(input("Enter the number of students: "))
            break
        except ValueError:
            print("Enter a real number.")

    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name"])
        for i in range(numOfStudents):
            sName = input("Enter the student's name: ").strip()
            writer.writerow({"ID": last_id + i + 1, "Name": sName})

    question = input(
        "Do you want to search for a specific student by their ID? ").strip().lower()
    if question == "yes":
        while True:
            try:
                search_ID = int(input("Enter the student's ID: "))
                break
            except ValueError:
                print("Enter a valid student's ID (number).")

        found = False
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["ID"]) == search_ID:
                    print(
                        f"Student found: ID={row['ID']}, Name={row['Name']}")
                    found = True
                    break
        if not found:
            print("ID doesn't match anybody")


if __name__ == "__main__":
    manage_students()
