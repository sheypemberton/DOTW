"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Shelby Pemberton pembe020
"""


def validate_input(date_string):
    """This function checks user input of a date in month-day-year format to see if it is a valid date. It is passed a
    string and returns a tuple (month, date, year) if it is a valid date and None if not. First, it checks if the str
    has enough characters for it to be a valid date. Then, it splits the string into a list by removing the dashes,
    then converts that list of strings into ints and creates a tuple of those ints. Then it checks if the tuple has
    three objects (for month, date, and year) and if so, then it checks if each is a valid month, date, or year."""

    # if the string doesn't contain at least 9 characters, it's not in valid x-x-xxxx format
    if len(date_string) < 8:
        return None
    # create tuple from string made of ints, split by the dash
    x = date_string.split('-')
    for num in range(len(x)):
        x[num] = int(x[num])
    date = tuple(x)

    # check if tuple is in valid month-day-year format
    if len(date) != 3:
        return None

    # check if year is valid (4 digits, not before 1000AD)
    if date[2] < 1000:
        return None
    elif date[2] > 9999:
        return None

    # if the day is 0, it is not a valid day
    if date[1] < 1:
        return None
    # use check_month function to see how many days should be in the month
    y = days_in_month(date)
    if y == 0:
        return None
    else:
        if date[1] > y:
            return None

    return date


def days_in_month(date_tuple):
    """This function is passed an int representing a month and returns how many days are in that month, or 0 if the int
    does not represent a valid month. It compares the month to values in two separate tuples which contain either the
    months that have 30 days or 31 days, unless the month is 2 or February, in which case the function returns 2 for
    further checking with the check_leap_year function."""
    x = list(date_tuple)

    # create tuples containing either months with 30 days or 31 days
    has31days = (1, 3, 5, 7, 8, 10, 12)
    has30days = (4, 6, 9, 11)

    # if the month is February, check for leap year conditions
    if x[0] == 2:
        if check_leap_year(x[2]):
            return 29
        else:
            return 28

    # if the month is in one of the tuples, return that amount of days for the month
    if x[0] in has31days:
        return 31
    if x[0] in has30days:
        return 30

    # if month is not between 1-12 return 0
    return 0


def check_leap_year(year):
    """This function is passed an int representing a year and True if it is a leap year and False if not. The
    conditions for a leap year are that the year is divisible by 4, but not by 100 unless it is divisible by 1000."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 1000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def next_date(date_tuple):
    """This function is passed a tuple that represents the date and returns a tuple that represents the date of the
    day after the passed date. First it converts the tuple to a list."""
    x = list(date_tuple)

    # check if it is the last day of the month
    if x[1] == days_in_month(date_tuple):
        # check if it is the last day of December, and if so, set date to (1, 1, next year)
        if x[0] == 12:
            x[0] = 1
            x[1] = 1
            x[2] += 1
        # if it is not the last day of December, increment the day and month by 1 and leave the year the same
        else:
            x[0] += 1
            x[1] = 1
    # if it is not the last day of the month, increment only the day
    else:
        x[1] += 1

    # put the list values into the tuple and return it
    date_tuple = tuple(x)
    return date_tuple


def previous_date(date_tuple):
    """This function is passed a tuple that represents the date and returns a tuple that represents the date of the day
    before the passed date. First it converts the tuple to a list."""
    x = list(date_tuple)

    # check if it is the first day of the month
    if x[1] == 1:
        # check if it is January, and if so, change date to (12, 31, last year)
        if x[0] == 1:
            x[0] = 12
            x[1] = 31
            x[2] -= 1
        # if it is not January, decrement the month and set the day to the last day of the month
        else:
            x[0] -= 1
            x[1] = days_in_month(x)
    # if it is not the first of the month, decrement the day
    else:
        x[1] -= 1

    # put the list values into the tuple and return it
    date_tuple = tuple(x)
    return date_tuple


def main():
    pass


if __name__ == "__main__":
    # import necessary modules
    from project1_dotw import get_dotw
    from project1_events import get_events_binary_search

    # create loop to repeat input if user desires
    while True:
        print("Enter a date: ", end = ' ')
        date_str = input()
        # check if date is valid
        date = validate_input(date_str)
        # if date is not valid, prompt user to try another date
        if date is None:
            print("The date needs to be in the month-day-year format, where the year is four digits.")
        else:
            x = list(date)
            dotw = get_dotw(x)
            # back up until it is the sunday before input date
            while dotw != 0:
                x = previous_date(x)
                dotw = get_dotw(x)

            # here are dictionaries for int: string for days and months to make printing easier
            days = {
                0: "Sunday",
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            }
            months = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }

            print()
            # print each day in the week and the events if there are any on that day
            for n in range(7):
                print(days[get_dotw(x)] + ", " + months[x[0]] + " " + str(x[1]))
                # get the list of events if any
                holidays = get_events_binary_search(x)
                if len(holidays) == 0:
                    print(" - No events")
                else:
                    for h in holidays:
                        print(" - " + h)
                # get the next date
                x = next_date(x)

        # prompt user for another date
        again = input('\nEnter another date? (yes/no) ')
        if again == 'no':
            break
        elif again != 'yes':
            print("I'm not sure what that means. Go ahead and try again!")
        print()
    print('Goodbye!')
    exit(-1)

