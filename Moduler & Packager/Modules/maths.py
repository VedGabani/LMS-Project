import math

def factorial(n):
    a = int(input("Enter a number to calculate its factorial -_- "))
    print("Factorial -_- ", math.factorial(a))

def interest_calculator():
    p = float(input("Enter principal amount -_- "))
    r = float(input("Enter rate of interest (in %) -_- "))
    t = float(input("Enter time (in years) -_- "))

    simple_interest = (p * r * t) / 100
    print("Simple Interest -_- ", simple_interest)

    compound_interest = p * (1 + r / 100) ** t - p
    print("Compound Interest -_- ", compound_interest)

def trignometric_calculator():
    angle = float(input("Enter angle in degrees -_- "))
    radians = math.radians(angle)

    print("Sine -_- ", math.sin(radians))
    print("Cosine -_- ", math.cos(radians))
    print("Tangent -_- ", math.tan(radians))

def Geometry_calculator():
    print("Choose a shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = int(input("Enter your choice (1-3) -_- "))

    if choice == 1:
        radius = float(input("Enter radius of the circle -_- "))
        area = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius
        print("Area of Circle -_- ", area)
        print("Perimeter of Circle -_- ", perimeter)

    elif choice == 2:
        length = float(input("Enter length of the rectangle -_- "))
        width = float(input("Enter width of the rectangle -_- "))
        area = length * width
        perimeter = 2 * (length + width)
        print("Area of Rectangle -_- ", area)
        print("Perimeter of Rectangle -_- ", perimeter)

    elif choice == 3:
        base = float(input("Enter base of the triangle -_- "))
        height = float(input("Enter height of the triangle -_- "))
        area = 0.5 * base * height
        print("Area of Triangle -_- ", area)
    else:
        print("Invalid choice!")