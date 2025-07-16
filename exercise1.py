import datetime

def weekday(day, month, year):
    '''
    Determines the day of the week for a given date using Zeller's congruence formula.

    Preconditions:
    - `day` is an integer between 1 and 31, inclusive, representing the day of the month making sure it corresponds to months.
    - `month` is an integer between 1 and 12, inclusive, representing the month of the year.
    - `year` is a valid integer representing the year (e.g., 2024).

    Postconditions:
    - The function prints the correct name of the day of the week (e.g., "Monday", "Tuesday")
      for the given date.
    - The output will be one of: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
      "Friday", or "Saturday".

    :param day: The day of the month (integer from 1 to 31).
    :param month: The month of the year (integer from 1 to 12).
    :param year: The year as an integer (e.g., 2024).

    :return: None. Prints the name of the day of the week.

    Example:
    >>> weekday(15, 10, 2024)
    Tuesday
    '''

    #preconditions:
    datetime.datetime(year=year, month=month, day=day)
    # formula
    y = year - ((14 - month) // 12)
    x = y + (y // 4) - (y // 100) + (y // 400)
    m = month + (12 * ((14 - month) // 12)) - 2
    d = (day + x + ((31 * m) // 12)) % 7

    match d:
        case 0:
            print("Sunday")
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")

def main():

    weekday(9,10,2003)


if __name__ == "__main__":
    main()