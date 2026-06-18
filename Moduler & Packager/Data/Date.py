from datetime import datetime
import time


def display_current_datetime():
    print("Current Date and Time:", datetime.now())


def date_difference():
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")

    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.strptime(d2, "%Y-%m-%d")

    print("Difference:", abs((date2 - date1).days), "days")


def format_date():
    d = input("Enter date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(d, "%Y-%m-%d")

    print("Formatted Date:", date_obj.strftime("%d-%m-%Y"))


def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()

    input("Press Enter to stop stopwatch...")
    end = time.time()

    print("Elapsed Time:", round(end - start, 2), "seconds")


def countdown_timer():
    sec = int(input("Enter seconds: "))

    while sec > 0:
        print(sec)
        time.sleep(1)
        sec -= 1

    print("Time's up!")