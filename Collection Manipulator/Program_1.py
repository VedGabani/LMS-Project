print("<<<< Welcome To Student Record Manager >>>>")

students = []

while True:

    print("\nSelect an option:")
    print("a. Add student")
    print("b. Display all students")
    print("c. Update student information")
    print("d. Delete student")
    print("e. Display subjects stored")
    print("f. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "a":

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        subjects = input("Enter Subjects: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "subjects": subjects
        }

        students.append(student)
        

        print("Student Added Successfully")

    
    elif choice == "b":


            for student in students:

                print("\nStudent ID :", student["id"])
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Subjects :", student["subjects"])

  
    elif choice == "c":

        update_id = input("Enter Student ID: ")

        for student in students:

            if student["id"] == update_id:

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["subjects"] = input("Enter New Subjects: ")

                print("Student Updated Successfully")

    
    elif choice == "d":

        delete_id = input("Enter Student ID: ")

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                print("Student Deleted Successfully")

   
    elif choice == "e":

            print("\nStored Subjects:")

            for student in students:

                print(student["subjects"])

    elif choice == "f":
        print("thank you")
        break
