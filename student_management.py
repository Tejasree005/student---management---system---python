students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    for roll_no, details in students.items():
        print("Roll Number:", roll_no)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("-" * 25)

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
