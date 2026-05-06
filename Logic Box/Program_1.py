# Logic Box

print("\n Welcome to the Pattern generator and Number analyzer\n")
print("Select an option -_- ")
while True:
    print("1. Right angle and Reverse angle Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")

    choice = input("Enter your choice -_- ")

    if choice == '1':
        print("\n----- Right Triangle -----\n")

        a = int(input("Enter number of Rows -_- "))
        for i in range(1 , a+1):
            print("*" *i)

        print("\n----- Reverse Triangle -----\n")
        a = int(input("Enter number of Rows -_- "))
        for i in range(a , 0 , -1):
            print("*" *i)

        if choice == '2':
            a = int(input("Enter the start of the range -_- "))
            b = int(input("Enter the start of the range -_- "))

            

else:
 print("Enter your valid choice")
