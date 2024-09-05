"""
Check Given Number is palindrome or not
number = 1234
phase 1:
    rem = 1234%10 = 4
    reverse = 0*10 + 4 = 4
    number = 1234//10 = 123
phase 2:
    rem = 123 % 10 = 3
    reverse = 4*10 + 3 = 43
    number = 123//10 = 12
phase 3:
    rem = 12 % 10 = 2
    reverse = 43*10 + 2 = 430+2 = 432
    number = 12//10 = 1
phase 4:
    rem = 1 % 10 = 1
    reverse = 432*10 + 1 = 4321
    number = 1//10 = 0
loop condition False 
reverse number = 4321
given number is not palindrome

if number = 12321
reverse number = 12321
both are same. we called number is palindrome

"""
number = int(input("Enter The Number:"))  # taking number from user
num = number
reverse = 0
while num != 0:
    remainder = num % 10  # Store the reminder
    reverse = reverse*10+remainder  # multiply previous reverse*10 and add remainder
    num //= 10  # finally number divided by 10

if reverse == number:
    print("Number is palindrome")
    print(f"reverse number is {reverse}")
else:
    print("Number is not palindrome")

