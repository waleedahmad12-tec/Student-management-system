students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        marks = input("Enter Marks: ")

        student = (name, age, marks)
        students.append(student)

        print("Student Added Successfully!")

    # Show Students
    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\nStudent Records:")

            for student in students:
                print(
                    "Name:", student[0],
                    "| Age:", student[1],
                    "| Marks:", student[2]
                )

    # Search Student
    elif choice == "3":

        search_name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student[0].lower() == search_name.lower():

                print("\nStudent Found:")
                print(
                    "Name:", student[0],
                    "| Age:", student[1],
                    "| Marks:", student[2]
                )

                found = True

        if found == False:
            print("Student Not Found")

    # Delete Student
    elif choice == "4":

        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:

            if student[0].lower() == delete_name.lower():

                students.remove(student)

                print("Student Deleted Successfully!")
                found = True
                break

        if found == False:
            print("Student Not Found")

    # Exit
    elif choice == "5":

        print("Program Closed")
        break

    else:
        print("Invalid Choice")