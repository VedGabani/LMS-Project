def add():
    a = input("Enter first number -_- ")
    b = input("Enter second number -_- ")  
    print("Result -_- ", float(a) + float(b))

def subtract():
    a = input("Enter first number -_- ")
    b = input("Enter second number -_- ")  
    print("Result -_- ", float(a) - float(b))

def multiply():
    a = input("Enter first number -_- ")
    b = input("Enter second number -_- ")  
    print("Result -_- ", float(a) * float(b))

def divide():
    a = input("Enter first number -_- ")
    b = input("Enter second number -_- ")  
    try:
        result = float(a) / float(b)
        print("Result -_- ", result)
    except ZeroDivisionError:
        print("Error -_- Cannot divide by zero")