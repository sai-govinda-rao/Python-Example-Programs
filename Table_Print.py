"""
Print the Table upto 10
first we will take number from user and print that number table upto 10
ex
number = 10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100

"""
number = int(input("Enter The Number and Get that Number table:"))
count = 1
while count <= 10:
    print(f"{number} * {count} = {number*count}")
    count += 1

"""
output:
    20 * 1 = 20
    20 * 2 = 40
    20 * 3 = 60
    20 * 4 = 80
    20 * 5 = 100
    20 * 6 = 120
    20 * 7 = 140
    20 * 8 = 160
    20 * 9 = 180
    20 * 10 = 200
"""