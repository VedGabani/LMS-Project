from datetime import datetime
import time


def display_current_datetime():
    print("Current Date and Time -_-:", datetime.now())


def date_difference():
    d1 = input("Enter first date (YYYY-MM-DD) -_- ")
    d2 = input("Enter second date (YYYY-MM-DD) -_- ")

    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.strptime(d2, "%Y-%m-%d")

    print("Difference -_-", abs((date2 - date1).days), "days")


def format_date():
    d = input("Enter date (YYYY-MM-DD) -_- ")
    date_obj = datetime.strptime(d, "%Y-%m-%d")

    print("Formatted Date -_- ", date_obj.strftime("%d-%m-%Y"))


def stopwatch():
    input("Press Enter to start stopwatch -_- ")
    start = time.time()

    input("Press Enter to stop stopwatch -_- ")
    end = time.time()

    print("Elapsed Time -_- ", round(end - start, 2), "seconds")


def countdown_timer():
    sec = int(input("Enter seconds -_- "))

    while sec > 0:
        print(sec)
        time.sleep(1)
        sec -= 1

    print("Time's up!")