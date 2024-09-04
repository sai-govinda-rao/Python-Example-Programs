"""
Jackpot / LuckyDraw Program
System Randomly Select one number
User select one number
if both are same You won the jackpot
if both are not Same BTNXT
"""

import random
lottery = random.randint(1,100)  # System select one number from 1 to 100
# and Store it in lottery variable
lucky_number = int(input("Enter you lucky number:"))  # user Enter his Lucky number

print("Lottry number is:" + str(lottery))
if lottery == lucky_number:
    print("Congratulations you won the JACKPOT")
else:
    print("Better luck next time")