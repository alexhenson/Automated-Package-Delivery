from datetime import datetime

STARTING_TIME = datetime(2022, 3, 18, 8, 0, 0)
STARTING_DATE_STR = '2022-03-18'


# This is code for the command line interface to validate user input and
# return a time in seconds to be used to report on the package deliveries
def return_time_info():
    while True:
        time = input(
            "Enter a time after 08:00:00 but before 17:00:00 (in military time, i.e., 0900) to check package status "
            "or 'X' to exit: ")

        if time.upper() == 'X':
            break
        elif len(time) != 4 or not time.isdigit() or 800 > int(time) > 1700:
            continue

        dt_tuple = tuple([int(x) for x in STARTING_DATE_STR.split('-')]) + tuple([int(time[:2])]) + tuple(
            [int(time[2:])])
        dt_obj = datetime(*dt_tuple)
        time_difference = dt_obj - STARTING_TIME

        if dt_obj > STARTING_TIME:
            return time_difference.total_seconds()
