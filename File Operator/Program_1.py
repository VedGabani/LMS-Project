from datetime import datetime

def main():

    while True:

        
        print("\n----- Let's Go -----\n")
        print("1. Add Entry\n")
        print("2. View all entry\n")
        print("3. Search all Entry\n")
        print("4. Delete Entry\n")
        print("5. Exit\n")

        d = int(input("Enter your choice -_- "))

        if d == 1:

            print("\n")

            add()

        elif d == 2:

            print("\n")

            view()

        elif d == 3:

            print("\n")

            search()

        elif d == 4:

            print("\n")

            delete()

        elif d == 5:

            print("\n")

            print("Program over")
            break

        else:

            print("\nEnter a valid choice")

def add():

    try:

        b = input ("Enter your file name with extention -_- ")

        entry = input("Enter your Journal entry -_- \n")

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")

        with open(b , "a") as file:
            file.write(f"\n[{time}]\n")
            file.write(entry + "\n\n")

        print("Entery added successfully")

    except Expection as e:

        print("Error -_- ", e)

def view():

    try:

        b = input ("Enter your file name with extention -_- ")

        with open(b , "r") as file:

            content = file.read()
            print(content)

    except FileNotFoundError:

        print("File not found")

def search():
    try:
        b = input("Enter your file name with extension -_- ")
        word = input("Enter the word you want to search for -_- ").lower()
        
        found = False
        with open(b, "r") as file:
            print(f"\n--- Search results for '{word}' ---")

            for line_number, line in enumerate(file, 1):
                if word in line.lower():
                    print(f"Line {line_number}: " , end = "")
                    found = True
                    
        if not found:
            print("Word not found in this file.")
            
    except FileNotFoundError:
        print("File not found")

def delete():

    try:

        b = input ("Enter your file name with extention -_- ")
        c = input("Are you sure you want to delete (yes/no) -_- ").lower()
            

        if c == "yes":

            with open(b , "w") as file:

                content = file.write("")

            print("File deleted successfully")

        elif c == "no":

            print("Content is safe")

        else:

            print("Enter correct yes or no")

    except FileNotFoundError:

        print("File not found")

main()
