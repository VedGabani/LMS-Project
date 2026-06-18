import random

def random_number():
    a = int(input("Enter the lower limit -_- "))
    b = int(input("Enter the upper limit -_- "))

    print("Random Number -_- ", random.randint(a, b))

def random_list():
    n = int(input("Enter the number of elements in the list -_- "))
    a = int(input("Enter the lower limit for random numbers -_- "))
    b = int(input("Enter the upper limit for random numbers -_- "))

    rand_list = [random.randint(a, b) for _ in range(n)]
    print("Random List -_- ", rand_list)

def random_password():
    length = int(input("Enter the length of the password -_- "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Random Password -_- ", password)

def random_otp():
    r = random.randint(100000, 999999)
    print("Random OTP -_- ", r)