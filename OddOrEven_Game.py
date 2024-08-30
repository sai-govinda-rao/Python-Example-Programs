"""
Odd Or Even Game
first Enter a number and your choose
computer can choose a number randomly
result = your number+computer number
if result is odd number and your choice is odd
you won the match
ex: your number = 1
    and choice = even
    computer number = 3   if computer number = 6
    result = 1+3 = 4      result = 1+6 = 7
    you won the match     you lose the match
"""
import random
random_number = random.randint(1, 10)
number = int(input("Enter Your Number:"))
while True:
    choice = input("Enter Your Choose (If you want to choose even then type even other wise type odd):").lower()
    if choice == "even" or choice == "odd":
        break
    else:
        print("Enter valid Choice")
print(f"Computer number is {random_number}")
if (random_number+number) % 2 == 0 and choice == "even":
    print("You Won the match")
else:
    print("You Lose The Match")

