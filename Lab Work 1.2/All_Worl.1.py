# Lab Work 1.2

print("----- Lab Work 1.2 -----\n")

while True:
    print("\n===== Menu =====\n")
    print("1. Use of Sep and End")
    print("2. Name, Age and Hobby")
    print("3. Addition Subtraction etc")
    print("4. Declares variable of different Datatype")
    print("5. Height and Width")
    print("6. Boolean")
    print("7. Assigment opperator")
    print("8. End")

    print("\n")
    choice = input("Enter your Choice -_- ")

    if choice == '1':

        print("\n----- Use of Sep and End -----\n")

        print("A", "B", sep="-")
        print("Hello", end="!")

    elif choice == '2':

        print("\n----- Name, Age and Hobby -----\n")

        a = input("Enter your Name -_- ")
        b = input("Enter your Age -_- ")
        c = input("Enter your Hobby -_- ")

        print(f"My name is {a}. I am {b} years old. My hobby is {c}.")


    elif choice == '3':

        print("\n----- Addition Subtraction etc -----\n")

        a = int(input("Enter the First number -_- "))
        b = int(input("Enter the Second number -_- "))

        print("Addition is -_- ", a+b)
        print("Subtraction is -_- ", a-b)
        print("Division is -_- ", a/b)
        print("Multiplicaton is -_- ", a*b)
        print("Floor Division is -_- ", a//b)
        print("Expontiation is -_- ", a**b)
        print("Modulus is -_- ", a%b)

    elif choice == '4':

        print("\n----- Declares variable of different Datatype -----\n")
        
        # String to int

        print("----- String to int -----\n")

        num_str = "89"
        print("Type of num_str -_- ", type(num_str))
        num_int = int(num_str)
        print(f"string `{num_str}` -> int{num_int}, type:{type(num_int)}")

        print("\n")

        # Float to int

        print("----- Float to int -----\n")

        num_float = 3.14
        print(f"Float {num_float} -> int:{int(num_float)}")

        print("\n")

        # Boolean to int

        print("----- Boolean to int -----\n")

        print(" True -> ", int(True))
        print(" False -> ", int(False))

        print("\n")

        # Float to string

        print("----- Float to string -----\n")

        str_float_num = 3.14
        str_float = str(str_float_num)
        print(f"(str_float_num) -> str:{str_float}, type:{type(str_float)}")

        print("\n")

        # String to List/Type/set

        # List

        print("----- List -----\n")

        list1 = [1, 2, 3]
        print(list1)
        print(type(list1))

        print("\n")

        # Tuple

        print("----- Tuple -----\n")

        tuple1 = (1, 2, 3)
        print(tuple1)
        print(type(tuple1))

        print("\n")

        # Set

        print("----- Set -----\n")

        set1 = {1, 2, 3}
        print(set1)
        print(type(set1))

        print("\n")

        # Dict

        print("-----   -----\n")

        dict1 = {'a':1 , 'b':2}
        print(dict1)
        print(type(dict1))

        print("\n")

        # id() fuction memory address

        print("----- id() fuction memory address -----\n")

        a = int(input("Enter value for A -_- "))
        b = int(input("Enter value for B -_- "))
        c = int(input("Enter value for C -_- "))

        print(f"(a) : {id(a)}")
        print(f"(b) : {id(b)}")
        print(f"(c) : {id(c)}")

        print("\n")

        # With mutable obj

        print("-----  With mutable obj -----\n")

        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = list1

        print(f"\nid(list1) : {id(list1)}")
        print(f"\nid(list2) : {id(list2)}")
        print(f"\nid(list3) : {id(list3)}")

        print("\n")

        # List to Str

        print("----- List to Str -----\n")

        a = (1, 2, 3)
        b = str(a)
        print(f"(a) -> str:{b}, type:{type(b)}")

        print("\n")

        # List to Tulpe

        print("----- List to Tulpe -----\n")

        a = (1, 2, 3)
        b = tuple(a)
        print(f"(a) -> tuple:{b}, type:{type(b)}")

        print("\n")

        # List to Set

        print("----- List to Set -----\n")

        a = (1, 2, 3)
        b = set(a)
        print(f"(a) -> set:{b}, type:{type(b)}")

        print("\n")

    elif choice == '5':

        print("\n----- Height and Width -----\n")

        a = input("Enter Height -_- ")
        b = input("Enter Wedith -_- ")
        print(f"Height is {a}cm. Weidth is {b}cm.")

    elif choice == '6':

        print("\n----- Boolean -----\n")

        a = input("Enter True or False for A -_- ")
        b = input("Enter True or False for B -_- ")

        a = a.lower() == "true"
        b = b.lower() == "false"

        print("A and B -_- ", a and b)
        print("A or B -_- ", a or b)
        print("Not A -_- ", not a)

    elif choice == '7':

        print("\n----- Assigment Operator -----\n")

        x = int(input("Enter First Number -_- "))
        y = int(input("Enter Second Number -_- "))

        x+=y
        print("+= -_- ", x) # x=x+y

        x-=y
        print("-= -_- ", x) # x=x-y

        x*=y
        print("*= -_- ", x) # x=x*y
         
        x/=y
        print("/= -_- ", x) # x=x/y

        x%=y
        print("%= -_- ", x) # x=x%y
        print("%= -_- ", y) # y=x%y

        y**=x
        print("**= -_- ",y) # y=y**x

    elif choice == '8':

        print("\n----- End -----\n")

        print("Program is closing....")
        break

else:
    print("Invalid Choice.")
