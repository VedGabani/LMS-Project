from Modules import File
from Modules import maths
from Modules import Random
from Modules import Date
from Modules import uuid

def Date():
    while True:
        print("\nDate and Time Operations -_-")
        print("1. Display Current Date and Time\n")
        print("2. Calculate Date Difference\n")
        print("3. Format Date\n")
        print("4. Stopwatch\n")
        print("5. Countdown Timer\n")
        print("6. Back to Main Menu\n")

        choice = int(input("Enter your choice (1-6) -_- "))

        if choice == 1:
            Date.display_current_datetime()
        elif choice == 2:
            Date.date_difference()
        elif choice == 3:
            Date.format_date()
        elif choice == 4:
            Date.stopwatch()
        elif choice == 5:
            Date.countdown_timer()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

def File():
    while True:
        print("\nFile Operations -_-")
        print("1. Create File\n")
        print("2. View File\n")
        print("3. Search in File\n")
        print("4. Delete File\n")
        print("5. Back to Main Menu\n")

        choice = int(input("Enter your choice (1-5) -_- "))

        if choice == 1:
            File.create()
        elif choice == 2:
            File.view()
        elif choice == 3:
            File.search()
        elif choice == 4:
            File.delete()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def Random():
    while True:
        print("\nRandom Operations -_-")
        print("1. Generate Random Number\n")
        print("2. Generate Random List\n")
        print("3. Generate Random Password\n")
        print("4. Generate Random OTP\n")
        print("5. Back to Main Menu\n")

        choice = int(input("Enter your choice (1-5) -_- "))

        if choice == 1:
            Random.random_number()
        elif choice == 2:
            Random.random_list()
        elif choice == 3:
            Random.random_password()
        elif choice == 4:
            Random.random_otp()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def Maths():
    while True:
        print("\nMath Operations -_-")
        print("1. Factorial\n")
        print("2. Interest Calculator\n")
        print("3. Trigonometric Calculator\n")
        print("4. Geometry Calculator\n")
        print("5. Back to Main Menu\n")

        choice = int(input("Enter your choice (1-5) -_- "))

        if choice == 1:
            maths.factorial()
        elif choice == 2:
            maths.interest_calculator()
        elif choice == 3:
            maths.trignometric_calculator()
        elif choice == 4:
            maths.Geometry_calculator()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def UUID():
    while True:
        print("\nUUID Operations -_-")
        print("1. Generate UUID\n")
        print("2. Back to Main Menu\n")

        choice = int(input("Enter your choice (1-2) -_- "))

        if choice == 1:
            uuid.generate_uuid()
        elif choice == 2:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nMain Menu -_-")
        print("1. Date and Time Operations\n")
        print("2. File Operations\n")
        print("3. Random Operations\n")
        print("4. Math Operations\n")
        print("5. UUID Operations\n")
        print("6. Exit\n")

        choice = int(input("Enter your choice (1-6) -_- "))

        if choice == 1:
            Date()
        elif choice == 2:
            File()
        elif choice == 3:
            Random()
        elif choice == 4:
            Maths()
        elif choice == 5:
            UUID()
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()