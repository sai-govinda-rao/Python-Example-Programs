"""
Taking year as input from user and calculate Which is leap year or not
leap year contains 366 days
normal year contains 365 days
leap year is happened once in 4 years
if year divided by 4 then we considered it's a leap Year
or else it's not a leap year
"""

year = int(input("Enter the Year:"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not leap year")

