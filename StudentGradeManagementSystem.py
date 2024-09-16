student_grades = {}


def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")


def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")


def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} Record has been deleted")
    else:
        print(f"{name} Record not Found")


def display_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")

    else:
        print("No Students Found/Added")

def main():
    while True:
        print("STUDENT GRADE MANAGEMENT SYSTEM")
        print("1. ADD STUDENT")
        print("2. UPDATE STUDENT")
        print("3. DELETE STUDENT")
        print("4. VIEW STUDENT")
        print("5. EXIT")

        choice = int(input("Enter Your Choice = "))
        if choice == 1:
            name = input("Enter Student Name =")
            grade = int(input("Enter Student Grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter Student Name =")
            grade = int(input("Enter Student Grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter Student Name =")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing The Programme...")
            break

        else:
            print("INVALID CHOICE")

main()


