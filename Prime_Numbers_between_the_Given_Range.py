"""
Prime Numbers between the Given range
first user enter the number which can store in variable num1
after user will have to enter the Second Number which can store in variable num2
when we start the execution program will print the all prime numbers between the num1 and num2
example
num1 = 1
num2 = 10
output : 2 3 5 7
above all numbers are prime numbers between 1 and 10
"""


def Prime_number_Check(num):
    count = 0  # count the total factors
    loop = 1  # while loop running variable
    while loop <= num:
        if num % loop == 0:
            count += 1
        loop += 1
    if count == 2:  # if number have only 2 factors which is prime
        return True
    else:  # number have more than one factors not prime
        return False



num1 = int(input("Enter the First Number:"))   # Takng Number one from user
num2 = int(input("Enter the Second Number:"))  # Taking NUmber two from user
for i in range(num1, num2):  # run the loop from num1 to num2
    if Prime_number_Check(i):  # Check the number is prime or not
        print(i, end=" ")   # if number is equals to prime the Print


"""
output:
Test case1:
    Enter the First Number:1
    Enter the Second Number:10
    2 3 5 7 
Test Case2:
    Enter the First Number:0
    Enter the Second Number:100
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
"""