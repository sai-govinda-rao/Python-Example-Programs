"""
Bank Management System
Create Bank Account creation, balance Enquire, withdrawal,  Deposit and keep record Account holder
details and...so on
"""



import random
import pandas as pd
#import pickle
#import Game_Elements

bank = """█▓▒▒░░░𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠 𝔹𝕒𝕟𝕜𝕄𝕒𝕟𝕒𝕘𝕖𝕞𝕖𝕟𝕥 𝕊𝕪𝕤𝕥𝕖𝕞░░░▒▒▓█"""
sbi = """
   _____ ____ _____ 
  / ____|  _ \_   _|
 | (___ | |_) || |  
  \___ \|  _ < | |  
  ____) | |_) || |_ 
 |_____/|____/_____|

        """

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def account_create():
    global name, balance
    global account_number
    global contact
    name = input("Enter Your Name:")
    while True:
        contact = input("Enter Your Mobile Number:")
        if contact.isdigit():
            contact = str(contact)
            if contact.__len__() == 10:
                contact = int(contact)
                break
            else:
                print("Enter 10 digit mobile number")
        else:
            print("Enter valid mobile number")
    account_number = ""
    for i in range(5):
        account_number += random.choice(digits)
    account_number = int(account_number)
    while True:
        #global balance
        balance = input("Enter Your Amount(Minimum Balance deposit balance is above 1500):")
        if balance.isdigit():
            balance = int(balance)
            if balance > 1500:
                break
            else:
                print("Minimum balance Required")
        else:
            print("Enter valid Amount")
    print(f"Mr.{name} Your Account Has Been Created")
    print(f"Name:{name} \nAccount Number:{account_number} \nContact Number:{contact}")
    details_file = open("AccountHolders.txt", "w")
    details_file.write(f"\nName: {name}\nAccount Number: {account_number}\nContact: {contact}")
    print()
    return balance


def total_details():
    take_account_holder_details = open("AccountHolders.txt", "r")   # create txt folder and give that txt folder path here
    take_account_holder_details.seek(0)
    print(take_account_holder_details.read())


def deposit():
    global balance
    while True:
        deposit_amount =input("Enter how much amount do you want to deposit:")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            balance += deposit_amount
            break
        else:
            print("Enter valid Amount")
    print(f"Successfully Amount Deposited")


def withdraw():
    global balance
    while True:
        withdrawal_amount = input("Enter How Much Money Do You Want to Withdraw:")
        if withdrawal_amount.isdigit():
            withdrawal_amount = int(withdrawal_amount)
            if balance >= withdrawal_amount:
                balance -= withdrawal_amount
                print("Amount Successfully Withdrawal")
                break
            else:
                print("insufficient balance")
        else:
            print("Enter Valid Amount")


def balance_check():
    while True:
        ac_no = int(input("Enter Your Account number:"))
        if ac_no == account_number:
            print(f"Your Account Balance is:{balance}.00 $")
            break
        else:
            print("Enter Valid Account Number")


def modify_account():
    global name, contact
    print("You can modify your name and mobile number")
    response = input("Which you want to change if you want to change your name then type 'n'\n"
                     "if you want to change your mobile number then type 'm' \n"
                     "if you want to change both type 'b':").lower()
    if response == "n":
        name = input("Enter your new name:")
        print(f"your updated name is:{name}")
    elif response == "m":
        contact = input("Enter your new contact")
        print(f"your updated contact number is:{contact}")
    elif response == "b":
        name = input("Enter your new name:")
        contact = input("Enter your new contact")
        print(f"your updated name is:{name}\nyour updated contact is:{contact}")


print(sbi)
print(bank)
while True:
    print(f"1.New Account\n2.Deposit\n3.Withdraw\n4.Balance Check\n5.Display Account List\n"
          f"6.Modify Account\n7.Exit")
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        account_create()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        balance_check()
    elif choice == 5:
        total_details()
    elif choice == 6:
        modify_account()
    elif choice == 7:
        print("THANKYOU")
        exit()
    else:
        print(f"Enter Valid Choice")




"""
output:
   _____ ____ _____ 
  / ____|  _ \_   _|
 | (___ | |_) || |  
  \___ \|  _ < | |  
  ____) | |_) || |_ 
 |_____/|____/_____|
       
        
█▓▒▒░░░𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠 𝔹𝕒𝕟𝕜𝕄𝕒𝕟𝕒𝕘𝕖𝕞𝕖𝕟𝕥 𝕊𝕪𝕤𝕥𝕖𝕞░░░▒▒▓█
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:1
Enter Your Name:Kornu Sai Govinda Rao
Enter Your Mobile Number:1234567890
Enter Your Amount(Minimum Balance deposit balance is above 1500):10000
Mr.Kornu Sai Govinda Rao Your Account Has Been Created
Name:Kornu Sai Govinda Rao 
Account Number:96891 
Contact Number:1234567890

1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:4
Enter Your Account number:96891
Your Account Balance is:10000.00 $
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:2
Enter how much amount do you want to deposit:2500
Successfully Amount Deposited
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:4
Enter Your Account number:96891
Your Account Balance is:12500.00 $
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:3
Enter How Much Money Do You Want to Withdraw:5000
Amount Successfully Withdrawal
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:4
Enter Your Account number:96891
Your Account Balance is:7500.00 $
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:5

Name: Kornu Sai Govinda Rao
Account Number: 96891
Contact: 1234567890
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:6
You can modify your name and mobile number
Which you want to change if you want to change your name then type 'n'
if you want to change your mobile number then type 'm' 
if you want to change both type 'b':b
Enter your new name:Sai
Enter your new contact1234543210
your updated name is:Sai
your updated contact is:1234543210
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:4
Enter Your Account number:96891
Your Account Balance is:7500.00 $

1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:5

Name: Kornu Sai Govinda Rao
Account Number: 96891
Contact: 1234567890
1.New Account
2.Deposit
3.Withdraw
4.Balance Check
5.Display Account List
6.Modify Account
7.Exit
Enter your Choice:7
THANKYOU
"""

