"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Shelby Pemberton pembe020
"""


def read_events():
    """This function reads and parses the events.csv file into a list of tuples and returns that list. """
    # create a list to store lines from the file
    event_list = []
    # open the file
    f = open('events.csv', 'r')
    # read in each line
    for line in f.read().split('\n'):
        if line:
            # for each line that is not empty, create a list item containing the string split by commas
            event_list.append(line.split(','))
    f.close()

    # change the first two strings in each list within the event_list into ints
    for an_event in event_list:
        x = 0
        while x < 2:
            an_event[x] = int(an_event[x])
            x += 1
    # convert the items in the list to tuples
    for num in range(len(event_list)):
        event_list[num] = tuple(event_list[num])

    return event_list


def sort_events(event_list):
    """This function takes the list of tuples and sorts it using selection sort, then returns the sorted list."""

    for num in range(len(event_list) - 1):
        # find index of smallest remaining event
        x = num
        for y in range(num + 1, len(event_list)):
            if before(event_list[y], event_list[x]):
                x = y
        # swap event at that index with smallest event index
        temp = event_list[num]
        event_list[num] = event_list[x]
        event_list[x] = temp

    return event_list


def sort_events_fast(event_list):
    """This function takes the list of tuples and sorts it using the quicksort and partition functions, then
    returns the sorted list."""
    # initialize variables for range of sorting
    low = 0
    high = len(event_list) - 1
    quicksort(event_list, low, high)
    return event_list


def quicksort(event_list, low, high):
    """This function is the quicksort function."""
    if low >= high:
        return
    x = partition(event_list, low, high)
    quicksort(event_list, low, x)
    quicksort(event_list, x + 1, high)
    return


def partition(event_list, low, high):
    """This function partitions for the quicksort function"""
    midpoint = low + (high - low) // 2
    pivot = event_list[midpoint]

    x = False
    while not x:
        while before(event_list[low], pivot):
            low += 1
        while before(pivot, event_list[high]):
            high -= 1
        # check if list is partitioned
        if low >= high:
            x = True
        # swap em
        else:
            temp = event_list[low]
            event_list[low] = event_list[high]
            event_list[high] = temp
            low += 1
            high -= 1
    return high


def get_events_binary_search(date):
    """This function takes a date tuple and returns a list of events that happen on that day. It gets a list of event
    tuples by calling read_events and then sorts them using sort_events, then it searches the sorted list of tuples
    to find all events that are on the same day as the input date. It will return a list of the names of the events,
    or an empty list if there are no matching events."""
    # create sorted event list by sorting the event tuples that are read in
    sorted_events = sort_events(read_events())
    # create array to store the names of the events
    events = []

    # initialize search variables
    low = 0
    high = len(sorted_events) - 1
    while high >= low:
        mid = (high + low) // 2
        if before(sorted_events[mid], date):
            low = mid + 1
        elif after(sorted_events[mid], date):
            high = mid - 1
        else:
            x = sorted_events[mid]
            # get the name of the event
            holiday = str(x[2])
            # add the event to the list
            events.append(holiday)
        # to make sure this function searches for multiple events on the same day, remove the event and research
        if len(events) > 0:
            del sorted_events[mid]
            high = len(sorted_events) - 1

    # return the list of events on the input date
    return events


def before(x, y):
    """This function takes two event tuples as arguments and returns True if the first event argument happens before
    the second event argument and returns False otherwise."""
    if x[0] < y[0]:
        return True
    elif x[0] == y[0]:
        if x[1] < y[1]:
            return True
        else:
            return False
    else:
        return False


def after(x, y):
    """This function takes two event tuples as arguments and returns True if the first event argument happens after
    the second event argument and returns False otherwise."""
    if x[0] > y[0]:
        return True
    elif x[0] == y[0]:
        if x[1] > y[1]:
            return True
        else:
            return False
    else:
        return False
