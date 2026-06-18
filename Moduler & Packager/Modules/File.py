def write():

    try:

        b = input ("Enter your file name with extention -_- ")

        content = input("Enter the content to write to the file -_- ")

        with open("Data/" +b , "w") as file:
            file.write(content)

        print("Content written to file successfully")

    except Exception as e:

        print("Error -_- ", e)

def create():

    try:

        b = input ("Enter your file name with extention -_- ")

        with open("Data/" +b , "a") as file:
            file.write("")

        print("File created successfully")

    except Exception as e:

        print("Error -_- ", e)

def view():

    try:

        b = input ("Enter your file name with extention -_- ")

        with open("Data/" +b , "r") as file:
            content = file.read()
            print("\nFile Content -_- \n")
            print(content)

    except Exception as e:

        print("Error -_- ", e)

def search():

    try:

        b = input ("Enter your file name with extention -_- ")

        search_term = input("Enter the term to search for -_- ")

        with open("Data/" +b , "r") as file:
            content = file.read()

            if search_term in content:
                print(f"'{search_term}' found in the file.")
            else:
                print(f"'{search_term}' not found in the file.")

    except Exception as e:

        print("Error -_- ", e)

def delete():

    try:

        b = input ("Enter your file name with extention -_- ")

        confirmation = input("Are you sure you want to delete this file? (yes/no) -_- ").lower()

        if confirmation == "yes":
            with open("Data/" +b , "w") as file:
                file.write("")
            print("File deleted successfully.")
        else:
            print("File deletion canceled.")

    except Exception as e:

        print("Error -_- ", e)