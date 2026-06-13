from datetime import datetime

class journal:

    def add(self):

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

    def view(self):

        try:

            b = input ("Enter your file name with extention -_- ")

            with open(b , "r") as file:

                content = file.read()
                print(content)

        except FileNotFoundError:

            print("File not found")

    def delete(self):

        try:

            b = input ("Enter your file name with extention -_- ")
            c = input("Are you sure you want to delete (yes/no) -_- ")
            

            if c == "yes":

                with open(b , "w") as file:

                    content = file.write("")
                    print(content)

                print("File deleted successfully")

            elif c == "no":

                print("Content is safe")

            else:

                print("Enter correct file")

        except FileNotFoundError:

            print("File not found")

while True:
    print("\n----- Let's Go -----\n")
    print("1. Add Entry")
    print("2. Delete all entry")

    d = int(input("Enter your choice -_- "))

    if d == "1":

        self.add()

    elif d == "2":

        self.delete()

    elif d == "3":

        self.view()

    elif d == "4":

        print("Program over")
        break

    else:

        print("Enyter a valid choice")

