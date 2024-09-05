"""
Guess Number game
First of all system asks which level do you want to paly easy or hard
if you choose easy you guess the correct number within 10 lifelines
if you choose hard you guess the correct number within 5 lifelines

after system choose on number randomly number is in between 1 and 50

after this you enter your guessing number if number is equals to system number you win
if your number is less then system number it will print following msg
Your Guessed Number is Too Lower Than Original Number
if your number is grater then system number it will print following msg
Your Guessed Number is Too Higher Than Original Number
this will continue until you have lifelines

"""


import random
print("Welcome to GUESS Puzzle Game")
number = random.randint(1, 50)
global game, choices
level = input("Which Type of level Do you want to play(type 'hard or easy'):").lower()
if level == "hard":
    choices = 5
elif level == "easy":
    choices = 10
while 0 < choices:
    guess_number = int(input("Enter The Guess Number(number is in between 1 to 50):"))
    if guess_number == number:
        print(f"Your Guessed Number {guess_number} correct")
        print("You Are very Intelligent")
        game = "win"
        break
    elif guess_number > number:
        print("Your Guessed Number is Too Higher Than Original Number")
        choices -= 1
        print(f"You Have {choices} lifelines")
    else:
        print("Your Guessed Number is Too Lower Than Original Number")
        choices -= 1
        print(f"You Have {choices} lifelines")
    if choices == 0:
        print("You Lose The Game")
        game = "lose"
if game != "win":
    print(f"Original Number is {number}")

"""
Welcome to GUESS Puzzle Game
Which Type of level Do you want to play(type 'hard or easy'):hard
Enter The Guess Number(number is in between 1 to 50):25
Your Guessed Number is Too Higher Than Original Number
You Have 4 lifelines

Enter The Guess Number(number is in between 1 to 50):12
Your Guessed Number is Too Lower Than Original Number
You Have 3 lifelines

Enter The Guess Number(number is in between 1 to 50):20
Your Guessed Number is Too Higher Than Original Number
You Have 2 lifelines

Enter The Guess Number(number is in between 1 to 50):15
Your Guessed Number is Too Lower Than Original Number
You Have 1 lifelines

Enter The Guess Number(number is in between 1 to 50):17
Your Guessed Number is Too Lower Than Original Number
You Have 0 lifelines
You Lose The Game
Original Number is 19

"""
