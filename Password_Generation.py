"""
Random Strong Pass word Generation
First System asks to users the following questions
1. How many letters do you want to be in your password?
2. How many numbers do you want to be in your password?
3. How many symbols do you want to be in your password?
after user enter the values
strong password generated according to Specified lengths

"""

import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
        'X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '?']
l_len = int(input("How many letters do you want to be in your password:"))
n_len = int(input("How many numbers do you want to be in your password:"))
s_len = int(input("How many symbols do you want to be in your password:"))
password_list = []
for i in range(1, l_len+1):
    char = random.choice(letters)
    password_list += char
for j in range(1, n_len+1):
    num = random.choice(numbers)
    password_list += str(num)
for k in range(1, s_len+1):
    sym = random.choice(symbols)
    password_list += sym
random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print("Here is your Strong Password:" + password)

"""
Output : 
How many letters do you want to be in your password:8
How many numbers do you want to be in your password:3
How many symbols do you want to be in your password:2
Here is your Strong Password:^R0N81U$oftPO
"""