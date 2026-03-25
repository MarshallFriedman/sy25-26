from traceback import print_exception

def initialize_records():
    students = [
        "Marshall,1.67",
        "Jordan,12",
        "David,10",
        "Aidian,11",
        "James,13",
        "Jacob,17",
        "Jack,9",
        "Mathew,13.4",
        "Jake,14.1",
        "Nate,6.7"
    ]
    with open("records.txt", "w") as file:
        for student in students:
            file.write(student + "\n")

def show_records():
    with open("records.txt", "r") as file:
        lines = file.readlines()

    records = []
    for line in lines:
        name, time = line.strip().split(",")
        records.append((name, float(time)))

    records = sorted(records, key=lambda x: x[1])
    for i in range(min(10, len(records))):
        print(records[i][0], records[i][1])

def add_records():
    name = input("Enter student name: ")
    time = input("Enter 100m dash time: ")
    with open("records.txt", "a") as file:
        file.write(name + "," + str(time) + "\n")

def average_time():
    with open("records.txt", "r") as file:
        lines = file.readlines()
    total = 0
    count = 0
    for line in lines:
        name, time = line.strip().split(",")
        total += float(time)
        count += 1
    if count > 0:
        average = total / count
        print(f"The average 100m dash run time is {average}.")
    else:
        print("No records to calculate average.")

def main():
    initialize_records()
    while True:
        print("Welcome to the Student Records 100m Dash! Type 1 to see student records. Type 2 to add student records. Type 3 to see student 100 m dash average. Type 4 to Search or Update a current record. Type 5 to Exit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_records()
        elif choice == "2":
            add_records()
        elif choice == "3":
            average_time()
        elif choice == "4":
            search_records()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def search_records():
    name = input("Enter the student's name to search: ")
    found = False
    with open("records.txt", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        student_name, student_time = line.strip().split(",")
        if student_name.lower() == name.lower():
            print(f"Found record: {student_name}, {student_time}")
            found = True
            choice = input("Do you want to update this record? (yes/no): ")
            if choice.lower() == "no":
                return
            elif choice.lower() == "yes":
                new_time = input("What would you like to change this student's record to? ")
                lines[i] = f"{student_name},{new_time}\n"
                with open("records.txt", "w") as file:
                    file.writelines(lines)
                print("Record updated.")
                return
    if not found:
        print("Record not found.")

main()