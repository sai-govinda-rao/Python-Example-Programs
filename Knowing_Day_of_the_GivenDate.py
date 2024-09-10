"""
To Calculate the Day of the Given Date
User give Date, Month, Year
System will calculate and tell the particular day of the specified date
Example:
    day = 31, month = 8, year = 2019
        Output: "Saturday"
        31st,Aug, 2019 is Saturday
"""
def Leap_year_Check(year):
    if (year%4 == 0 or year%400 == 0) and year%100 != 0:
        return True
    else:
        return False


date = int(input("Enter the Date:"))
month = int(input("Enter the Month:"))
year = int(input("Enter the Year:"))
days = {
        "0": "Sunday",
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday"
}
months = {
    "1": 3,
    "2": 0,
    "3": 3,
    "4": 2,
    "5": 3,
    "6": 2,
    "7": 3,
    "8": 3,
    "9": 2,
    "10": 3,
    "11": 2,
    "12": 3
}
completed_years = year-1
odd_val1 = completed_years % 100
odd_val2 = completed_years-odd_val1
odd_days1 = odd_val2 % 400
if odd_days1 == 100:
    val1 = 5
elif odd_days1 == 200:
    val1 = 3
elif odd_days1 == 300:
    val1 = 1
else:
    val1 = 0
val2 = (odd_val1+(odd_val1//4)) % 7
val3 = 0
for i in range(1, month):
    if i == 2 and Leap_year_Check(year):
        val3 += 1
    else:
        val3 += months[str(i)]
result = (val1+val2+val3+date) % 7
if date < 10:
    date = str(f"0{date}")
if month < 10:
    month = str(f"0{month}")
print(f"{date}-{month}-{year} is {days[str(result)]}")

"""
output:
example 1:
   Enter the Date:07
    Enter the Month:09
    Enter the Year:2024
    07-09-2024 is Saturday
   
example 2: 
    Enter the Date:11
    Enter the Month:11
    Enter the Year:2024
    11-11-2024 is Monday
"""


