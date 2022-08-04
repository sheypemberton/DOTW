"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Shelby Pemberton pembe020
"""

from project1 import check_leap_year

dotw_index = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def get_doomsday_dotw(year):
    """This function is passed an int representing a year and returns the DOTW index for the doomsdays that year. This
    is calculated according to John H. Conway's Doomsday Rule, part of which is outlined in the comments below."""
    target_year = year % 100
    century = year - target_year

    # get century index: doomsday DOTW for first year of the century, find remainder after dividing by 400
    century_remainder = century % 400
    if century_remainder == 0:
        century_index = 2
    elif century_remainder == 100:
        century_index = 0
    elif century_remainder == 200:
        century_index = 5
    elif century_remainder == 300:
        century_index = 3

    # use values of target year floor divided by 12 and remainder, and that remainder divided by 4
    a = target_year // 12
    b = target_year % 12
    c = b // 4
    # add these values to century index
    d = century_index + a + b + c

    # doomsday DOTW index is the remainder of the last sum divided by 7
    doomsday_dotw = d % 7

    return doomsday_dotw


def get_dotw(date):
    """This function is passed a tuple representing a month-day-year date, and returns a DOTW index value for that date.
    This is calculated according to John H. Conway's Doomsday Rule, part of which is outlined in the comments below."""

    # set doomsday to constant doomsday date, where January and February depend on whether the year is a leap year
    if date[0] == 1:
        if check_leap_year(date[2]):
            doomsday = 4
        else:
            doomsday = 3
    elif date[0] == 2:
        if check_leap_year(date[2]):
            doomsday = 29
        else:
            doomsday = 28
    elif date[0] == 3:
        doomsday = 14
    elif date[0] == 4:
        doomsday = 4
    elif date[0] == 5:
        doomsday = 9
    elif date[0] == 6:
        doomsday = 6
    elif date[0] == 7:
        doomsday = 11
    elif date[0] == 8:
        doomsday = 8
    elif date[0] == 9:
        doomsday = 5
    elif date[0] == 10:
        doomsday = 10
    elif date[0] == 11:
        doomsday = 7
    else:
        doomsday = 12

    # find the difference between the given day and the doomsday
    x = date[1] - doomsday
    # combine with the doomsday index obtained from the get_doomsday_dotw function
    y = x + get_doomsday_dotw(date[2])
    # remainder of that value divided by 7 is the index for the DOTW of given date
    dotw = y % 7

    return dotw
