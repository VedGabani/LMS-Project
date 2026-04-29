# Fundamental Booster

# Welcome

print("-_-" * 16)
print("\n----- Welcome to Fundamental Booster Program. -----\n")
print("-_-" * 16)

print("\n")

print("This Program will collect your Personal Detail..")
print("Perform some calculation & show you data type detail.")
print("Let's get Started")

print("\n")

# Information Collector

print("-_-" * 16)
print("\n----- Information Collector -----\n")
print("-_-" * 16)

print("\n")

name = input("Enter you Name -_- ")
age_str = input("Enter you Age -_- ")
height_str = input("Enter you Height in Meter -_- ")
fav_str = input("Enter you Favroute Number -_- ")

print("\n")

# Calculation, Converter and Arithmetic

age = int(age_str)
height = float(height_str)
fav = float(fav_str)
a = 2026
b = a - age
height_cm = height * 100
sum_value = age + fav
product_value = age * fav
heights = int(height)
ages = float(age)
age_str = str(age)

# Processing

print("-_-" * 16)
print("\n----- Processing -----\n")
print("-_-" * 16)

print("\n")

print(f"Your name is {name} Type -_- {type(name)} ID -_- {id(name)}")
print(f"Your age is {age} Type -_- {type(age)} ID -_- {id(age)}")
print(f"Your height is {height_str} Type -_- {type(height_str)} ID -_- {id(height_str)}")
print(f"Your favroute number is {fav} Type -_- {type(fav)} ID -_- {id(fav)}")
print(f"Your Born year as per your age is {b} Type -_- {type(b)} ID -_- {id(b)}")
print(f"Your Height in integer {heights} Type-_- {type(heights)} ID -_- {id(heights)}")
print(f"Your age in string {age_str} Type-_- {type(age_str)} ID -_- {id(age_str)}")
print(f"Your age in float {ages} Type-_- {type(ages)} ID -_- {id(ages)}")

print("\n")

# Display Opeartion
print("-_-"*16)
print("\n----- Display Operation -----\n")
print("-_-"*16)

print("\n")

print("Calculated Result")
print(f"Your height in centimeter is {height_cm} cm")
print(f"Sum of your age and favroute number is {sum_value}")
print(f"Multiplication of your age and favroute is {product_value}")

print("\n")

# String Concatination

print("-_-"*16)
print("\n----- String Concatination -----\n")
print("-_-"*16)

print("\n")

greeting = "Hello" + name + "!"
print(f"{greeting} Type -_- {greeting} ID -_- {greeting}")

print("\n")

# Summary Table

print("-_-"*16)
print("\n----- Summary Table -----\n")
print("-_-"*16)

print("\n")

print(f"\n {'name':<20}  {str(type(name)):<25} {id(name):<15}")
print(f"\n {'age':<20}  {str(type(age)):<25} {id(age):<15}")
print(f"\n {'height':<20}  {str(type(height)):<25} {id(height):<15}")
print(f"\n {'favroute':<20}  {str(type(fav_str)):<25} {id(fav_str):<15}")

print("\n")

# Closing Message

print("-_-"*16)
print("\n----- Closing Message -----\n")
print("-_-"*16)

print("\n")

print("Thank you using Personal Data collector \n")
print("you've been successfully explore -_- \n")
print("print() and input() function\n")
print("String, int, float, dat  types\n")
print("Arrithmetic operators ( + , * , / , - )\n")
print("type and id() built-in function\n")
print("string concatination\n")
print("Type casting\n")
