# This is code for the command line interface to check on relevant package information
from datetime import datetime

STARTING_TIME = datetime(2022, 3, 18, 8, 0, 0)
STARTING_DATE = '2022-03-18'

def check_on_delivery_status():
    while True:
        time = input(
            "Enter a time after 08:00:00 (in military time, i.e., 0900) to check package status or 'X' to exit: ")
        print()
        if time.upper() == 'X':
            break
        elif len(time) == 4 and time.isdigit() and time > STARTING_TIME:
        else:
