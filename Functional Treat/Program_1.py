print("<<<< Welcome To My Program :-- Function Treat >>>>")
print("\nWelcome To Data Analyzer And Transformer Program")

data = []

while True:
    print("\nMain Menu -_-")
    print("i. Input Data")
    print("ii. Display Data Summary (built-in function)")
    print("iii. Calculate Factorial (Recursion)")
    print("iv. Filter Data by Threshold (lambda function)")
    print("v. Sort Data")
    print("vi. Display Dataset Statistics")
    print("vii. Exit program")

    choice = input("\nChoose an option -_- ")

    if choice == "i":
        print("\nInput Data")
        
        print("\nEnter data for a 1d array")
        
        values = input("(separated by spaces) -_- ")
        
        data = list(map(int, values.split()))
        
        print("Data stored successfully!")
        
        print("Data -_- ", data)

    elif choice == "ii":
        print("\nDATA SUMMARY")
        
        if not data:
            
            print("Error -_- Dataset is empty")
        else:
            print("Dataset:", data)
            print("Total Elements -_- ", len(data))
            print("Sum of Values -_- ", sum(data))
            print("Minimum Value -_- ", min(data))
            print("Maximum Value -_- ", max(data))
            print("Average Value -_- ", sum(data) / len(data))

    elif choice == "iii":
        
        print("\nCalculate Factorial")
        
        number = int(input("Enter a number -_-  "))

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)

        print("Factorial is -_- ", factorial(number))

    elif choice == "iv":
        
        print("\nFilter Data by Threshold")
        
        if not data:
            print("Error: Dataset is empty.")
            
        else:
            threshold = int(input("Enter threshold value -_- "))
            
            filtered = list(filter(lambda x: x > threshold, data))
            
            print("Filtered Data -_- ", filtered)

    elif choice == "v":
        
        print("\nSort Data")
        
        if not data:
            
            print("Error: Dataset is empty.")
            
        else:
            print("1. Ascending Order")
            print("2. Descending Order")
            
            choice = input("Enter your choice -_- ")

            if choice == "1":
                
                print("Ascending Order -_- ", sorted(data))
                
            elif choice == "2":
                
                print("Descending Order -_- ", sorted(data, reverse=True))
                
            else:
                
                print("Invalid choice!")


    elif choice == "vi":
        
        print("\nDataset Statistics")
        
        if not data:
            
            print("Error: Dataset is empty.")
            
        else:
            
            print("Dataset:", data)
            print("Total Elements -_- ", len(data))
            print("Sum of Values -_- ", sum(data))
            print("Minimum Value -_- ", min(data))
            print("Maximum Value -_- ", max(data))
            print("Average Value -_- ", sum(data) / len(data))

    elif choice == "vii":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
        
    else:
        print("Invalid choice!")
