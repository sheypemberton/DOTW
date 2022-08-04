# Project 1

## Overview
For this project you will create a simple calendar application. A user will insert a date (month-day-year), and your program will calculate and print each day of that week starting with Sunday, as well as any events that are on any of those dates. An example usage would look like this:

```
Enter a date: 12-30-2020

Sunday, December 27
 - No events
Monday, December 28
 - No events
Tuesday, December 29
 - No events
Wednesday, December 30
 - No events
Thursday, December 31
 - New Year's Eve
Friday, January 1
 - New Year's Day
Saturday, January 2
 - No events
```

## Instructions
One of the major goals of the projects in this class is to give you experience designing and programming more complex and involved applications. Despite looking simple, there are actually quite a few steps you have to do. You have to:

1) Read and validate the user's input
1) Determine the day of the week for the entered date
1) Determine the dates for the other days in the week
1) For each date in the week, search a collection of events (this may require sorting the events, depending on which search algorithm is being used)
1) Format all this data and print it

Below are some more detailed instructions for each step. Note that to make grading and testing doable, I am providing some of the structure for this project. This structure requires the exchange of dates among its various components. This date is going to be a 3 element tuple, where each element is an integer. The first element will be the month, the second the day, and the fourth the year. We will call this a **date tuple**. For example, April 7, 2024 would have the following date tuple ```(4, 7, 2024)```. Please note that this is using North America's strange convention where the month is the first element in the tuple, not the day. 

The program that will run this is ```project1.py```. So when ```project1.py``` is run it will ask the user for a date and print the week calendar. To accomplish this you will complete a series of functions in ```project1.py```, ```project1_dotw.py```, and ```project1_events.py```. To test your project, we will need to import ```project1.py```. When it is imported it should **not** run the program (asking for a date and printing the week).

### Reading and validating the user's input
To read the user's input, you will use the built-in ```input``` function. The expected input should be a string in the form ```month-day-year```. In ```project1.py``` you will complete the function ```validate_input``` so that it determines if the input is valid. It will take the input as its sole argument and return a date tuple if the input is valid. If the input is invalid, it should return ```None```.

The following constitute valid input:
* The input should be of the form ```month-day-year```
* The month should be an integer between 1 and 12
* The day should be an integer with a range that is determined by the month
  - For example, December has a range of 1 to 31, April has a range of 1 to 30, etc.
  - February should have a range of 1 to 28, unless the year is a leap year, in which case it has a range of 1 to 29
    * A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is divisible by 1000 (confusing, I know).
    * Examples: 1904 is a leap year, 1900 is not a leap year, 2000 is a leap year
* The year should be a 4 digit integer and must not be before the year 1000AD.

### How to calculate the day of the week
This method was first realized by mathematician John H. Conway by creating the following algorithm.

Before we start, lets define some terms:
   - **Day of the week (DOTW)**: Sunday, Monday, etc.
   - **Target date**: the date that we are trying to determine the day of the week for
   - **Target year**: the year of the target date
   - **Target month**: the month of the target date

First, we have to assign an indexable value to the day of the week. Starting with Sunday=0 and incrementing to Saturday=6. I have provided a dictionary that provides indices for each of the days of the week in ```project1_dotw.py``` called ```dotw_index```.

The second step is to find a reference date. This date must be in the same month as our target date. Conway's genius was in recognizing that each month has what Conway called a "doomsday", and all 12 doomsdays in any given year have the same day of the week. It will be this doomsday that we use as our reference date. The following are the doomsdays:
 - Jan. 3rd (or 4th if leap year)
 - Feb. 28th (or 29th if leap year)
 - March 14th
 - April 4th
 - May 9th
 - June 6th
 - July 11th
 - Aug. 8th
 - Sept. 5th
 - Oct. 10th
 - Nov. 7th
 - Dec. 12th

The basic steps are:
1) Determine the doomsday DOTW for the target date's year
1) Calculate the difference in number of days between the target date and the doomsday for the target date's month
1) Using this difference, calculate the DOTW for the target date

#### Calculating the doomsday DOTW for a given year
The first step will be to calculate the doomsday DOTW for any given year. Use the following steps to complete the ```get_doomsday_dotw``` function in ```project1_dotw.py```. This function will take an integer year as its sole argument and will return the doomsday DOTW index number.

To calculate the doomsday DOTW for a given year, we first need to know what the doomsday DOTW was for the first year of that century. To do this find the remainder of that century divided by 400. If the remainder is 0 the doomsday DOTW is a Tuesday. If it is 100 then Sunday, 200 then Friday, and 300 then Wednesday. We will call the index of that DOTW the **century index**. For example, if I wanted to calculate the doomsday DOTW for 1952, I would first need to calculate the doomsday DOTW for 1900 by dividing 1900 by 400, which would have a remainder of 300. Hence, the doomsday for 1900 would be a Wednesday and the century index for any year between 1900 and 1999 would be **3** (Wednesday's index is 3).

Next, figure out how many times the target year (not including the century) can be divided by 12, as well as the remainder. We then see how many times that remainder can be divided by 4. To continue our example, 52 (1952 not including the century) can be divided by 12 **4** times and would have a remainder of **4**. That remainder of 4 can be divided by 4 **1** time.

So now we have a century index, the number of times 12 can be divided by the target date year not including the century, the resulting remainder, and how many times that remainder can be divided by 4. For our example of 1952, that leaves us with the numbers 3, 4, 4, 1.

The final step is to add these four numbers up and divide by 7. The remainder is the doomsday DOTW index for that year. For 1952, the doomsday DOTW index is the remainder of 12/7, which is 5 (we got 12 by adding 3, 4, 4, and 1). As the 5 is the DOTW index for Saturday, all doomsdays in 1952 were Saturdays.

#### Calculate the DOTW for the target date
Now that you know what the doomsday DOTW for your target year is, and you know the doomsday for your target month, you can calculate what the DOTW is for your target date. Use the following steps to complete the ```get_dotw``` function in ```project1_dotw.py```. The function has a date tuple as its sole argument and will return the DOTW index number.

First we need the difference between the target day of the month, and the doomsday. For example, if the target date is December 22, 1952 then the difference would be 10. This is 22 (the target day of the month) minus 12 (the doomsday for December). We then add this number to the doomsday DOTW index. For our example this would be 15. This is 10 (from the previous calculation) plus 5 (the doomsday DOTW index for 1952). Finally divide this number by 7 and take the remainder to get the DOTW index for our target date. Four our example this would be 1 (15 / 7 has a remainder of 1). This means that December 22, 1952 was a Monday (Monday's index is 1).

#### Tips
I know that this is confusing, and there is a lot to it, but please stick with it. Feel free to look up more information on this technique, it's called the Doomsday Rule. What you are **not** allowed to do is find code or algorithms that show you how to implement the Doomsday Rule. Another great resource is [this YouTube video](https://youtu.be/714LTMNJy5M).

When programming in general, but particularly so for a complex series of steps such as this, it is helpful to test along the way. As soon as you complete a step, do some testing to make sure that you are receiving the output that you expect. This helps you determine where a logic error is by eliminating the possible locations of that error. For example, after completing the first step of this process (determining the doomsday DOTW for a given year) run that section of the code a few times with different years. Then compare that output with a doomsday (April 4 for example) of that year.

Also remember that the modulus operator (```%```) will give you the remainder of a division operation.

### Calculating the other dates for the week
Once you know the DOTW for the input date, you should be able to calculate how many dates are before and after it in the week. For example, if the input date is a Wednesday then you know there are three dates before it (Sunday, Monday, Tuesday) and three after (Thursday, Friday, Saturday) in that particular week. To calculate the dates you will call the functions ```next_date``` and ```previous_date``` in ```project1.py```, which you need to complete.

```next_date``` will take a date tuple as its sole input and return a date tuple that represents the next date. For example, if it received ```(1, 23, 2023)``` as the argument value, it would return ```(1, 24, 2023)```.

```previous_date``` will take a date tuple as its sole input and return a date tuple that represents the previous date. For example, if it received ```(1, 23, 2023)``` as the argument value, it would return ```(1, 22, 2023)```.

Be careful to include edge cases, such as wrapping from one month to another, or even one year to another. Also make sure to account for February 29 if it is a leap year.

### Search for events
At this point you should have a collection of 7 dates, one for each day of the week. For each of the dates you need to determine if there is an event on that day.

To do this you will need to complete the functions ```read_events```, ```get_events_binary_search```, and ```sort_events``` in ```project1_events.py```. Completing these functions will allow you to complete the project, but to get full points you will also need to complete the ```sort_events_fast``` function.

```read_events``` will read and parse the ```events.csv``` file. This is a Comma Separated Values (CSV) file. Each line of the CSV file represents one group of data points (in this case an event). The line will have values that are separated by commas. This file will contain (in order) the event's integer month, its integer day, and its name. For example, the New Year's Eve event will have a line in ```events.csv``` that looks like ```12,31,New Year's Eve```. Your job will be to parse and store each event into a Python list. The event should be stored in an **event tuple**. An event tuple is a 3 element tuple, where the first element is the month the event occurs (an integer), the second is the day of the month the event occurs (an integer), and the third is the name of the event (a string). The event tuple for New Year's Eve will look like ```(12, 31, "New Year's Eve")```. ```read_events``` will return this list of event tuples. Refer to previous labs for how to read files, though the parsing of the individual lines will be slightly different. Hint: use the Python [split function](https://python-reference.readthedocs.io/en/latest/docs/str/split.html).

```sort_events``` will take a list of event tuples as its sole argument and return a sorted list of event tuples (in ascending order). You may either implement Selection Sort or Insertion Sort in this function.

```sort_events_fast``` will take a list of event tuples as its sole argument and return a sorted list of event tuples (in ascending order). You may either implement Merge Sort or Quick Sort in this function.

```get_events_binary_search``` will take a date tuple as its sole argument. It will get a list of event tuples by calling ```read_events``` and sort them using either the ```sort_events``` function or the ```sort_events_fast``` function. It will then search the sorted list of event tuples to find all events that are on the same day as the input date tuple. If one or more events are found, it will return a list of the name(s) of the found event(s). If there is no matching event it will return an empty list. Binary search will only find one matching event, so you will need to repeat searching the list (removing any found events after each iteration) until there are no more matching events in the list.

**Note:** In order to complete the sorting and searching functions, you will need to have a way to compare the event tuples. I recommend creating two additional functions. The first will take two event tuples as arguments and return ```True``` if the first event argument happens before the second event argument (is "less than") and ```False``` otherwise. The second will do the same but return ```True``` if the first event argument happens after the second event argument (is "greater than") and ```False``` otherwise.

## Testing
As with some of the labs, there is a test file, ```lab1_tests.py```, included with the project. There are a series of tests that test the finished functions in the same order as laid out in the "Recommended Procedure" section. You are encouraged (though not required) to add additional tests to this file.

There are deliberate edge cases not covered by the provided testing. Edge cases are situations that happen rarely, but would result in a logic error if not accounted for. An example of an edge case error would be failing to account for leap days (if the year is 2004, the ```previous_date``` function with the date tuple ```(3, 1, 2004)``` as an argument should return the date tuple ```(2, 29, 2004)``` and not ```(2, 28, 2004)```). You should spend some time trying to identify edge cases and adding tests to make sure that they behave as they should.

**Note:** The graders will use a different test file than the one provided. It will include all of the tests in the test file provided, but it will also include more tests for edge cases that we have identified.

## Further Notes
* I have provided the bare bones structure for this project. There are additional variables and functions that you may need to create to assist with completing this project. What you create and how you use them are up to you, but I would recommend you put some thought into it before you start coding.
* You must not change the provided structure. All of the provided functions must have the names and argument names as provided. For example, it might be nice to have a function that returns the number of days in a month.
* You are encouraged to add more dates to ```events.csv``` for further testing. Be aware that doing this will probably break the existing tests in ```project1_tests.py```. I suggest making sure that your program passes all of the tests before editing ```events.csv```.

## Recommended Procedure
1) Complete ```validate_input``` and test.
1) Complete ```next_date``` and test.
1) Complete ```previous_date``` and test.
1) Complete ```get_doomsday_dotw``` and test.
1) Complete ```get_dotw``` and test.
1) Start the main program. At this point you should be able to take a date as input and print the rest of the days of that week, including the day of the week, starting on Sunday. This output should look like the example at the top of this document, but without any events.
1) Complete ```read_events``` and test.
1) Complete ```sort_events``` and test.
1) Complete ```get_events_binary_search``` and test.
1) Complete ```sort_events_fast``` and test.
1) Complete the main program and test.
1) Identify possible edge cases and modify ```project1_tests.py``` to test them.

## Documentation Requirements
* All docstrings at the start of the Python files must be edited to have your name and your x500.
* All functions (including functions that you add) must have a docstring that describe the function's purpose, its arguments, and what it returns.
* All code must have comments that describe the logical steps. This does not need to be line by line, but rather logical chunk by logical chunk.

## Rubric
Here I am laying out how points will be divided amongst the various components of the project. Each component has a max number of points, as well as the ways that points can be deducted. Note that you can not receive negative points for any of the components.
 
#### Documentation (8 points)
* 2 points: All docstrings at the start of the Python files have been edited to have your name and your x500.
  - -1 point if some, but not all docstrings have been edited
  - -2 points if no docstrings have been edited 
* 3 points: All functions (including functions that you add) have a docstring that describes the function's purpose, its arguments, and what it returns.
  - -1 point if most, but not all of the functions have a sufficient docstring
  - -2 points if some of the functions have sufficient docstrings
  - -3 points if none of the functions have sufficient docstrings
* 3 points: All code must has comments that describe the logical steps.
  - -1 point if most of the code is well commented
  - -2 points if some of the code is well commented
  - -3 points if none of the code is commented
#### Functionality (32 points)
* 3 points: ```validate_input``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```next_date``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```previous_date``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```get_doomsday_dotw``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```get_dotw``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```read_events``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```sort_events``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```sort_events_fast``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 3 points: ```get_events_binary_search``` works as described in the "Instructions" section.
  - -3 points if it is not implemented
  - -1 point if it fails one or more of the provided tests, but only a small correction is required to fix it.
  - -2 points if it fails one or more of the provided tests, and a large correction is required to fix it.
  - -1 point if it passes all of the provided tests, but fails one or more of the grader tests.
* 5 points: the main program works as described in the "Instructions" section.
  - -4 points if it is not implemented
  - -1 point if it runs when ```project1.py``` is imported
  - -2 points if it does not start the calendar with Sunday
  - -1 point if it fails to print events for days that should have events

**Total available points: 40**