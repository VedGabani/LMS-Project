# Logic Box

def show_menu():

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Sandwhich maker")
    print("4. Simple Calculator")
    print("5. Pet Simulator")
    print("6. Rock,Papper and Scissors")
    print("7. Exit\n")


def analyze_range():

    start = int(input("\nEnter the start of the range -_- "))
    end = int(input("Enter the end of the range -_- "))

    total = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")

        total += num

    print(f"\nSum of all numbers from {start} to {end} is: {total}")


def generate_pattern():

    rows = int(input("\nEnter number of rows -_- "))
    for i in range(1, rows + 1):
        print("*" * i)

def sandwhich():

    bread = input("Choose your Bread (White/Brown) -_- ")
    filling = input("Choose your filling (Cheese/Jelly) -_- ")

    print("Here is your Silly sandwhich")
    print("["+bread + " bread + " + filling + " + Hot sause ]")

def calculator():

    a = int(input("Enter the First number -_- "))
    b = int(input("Enter the Second number -_- "))

    print("Addition is -_- ", a+b)
    print("Subtraction is -_- ", a-b)
    print("Division is -_- ", a/b)
    print("Multiplicaton is -_- ", a*b)
    print("Exponential -_- ", a**b)
    print("Floor Division -_- ", a//b)

def pet():

    pet = input("Select your Pet (Dog/Cat/Fish) -_- ")

    if pet == "Dog":
        print("Here is your Dog wof!")

    elif pet == "Cat":
        print("Here is your Cat meow!")

    elif pet == "Fish":
        print("Here is your Fish Blob")

    else:
        print("We don't have that Pet Sorry!")

def rock():

    import random

    choices = ["Rock", "Paper", "Scissors"]

    computer = random.choice(choices)
    player = input("Choose Rock,Paper and Scissors -_- ")

    if player == computer:
        print("It's Tie.......")

    elif (player == "Rock" and computer == "Scissors") or\
          (player == "Paper" and computer == "Rock") or\
          (player == "Scissors" and computer == "Paper"):
        print("You wins!!!!!")

    else:
        print("Computer Wins")

def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            generate_pattern()
        elif choice == 2:
            analyze_range()
        elif choice == 3:
            sandwhich()
        elif choice == 4:
            calculator()
        elif choice == 5:
            pet()
        elif choice == 6:
            rock()
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
main()
