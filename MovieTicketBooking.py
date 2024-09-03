"""
Movie Ticket Booking Program
Fist of all User Choose the place
there are Three Types of places Available
Balcony - B
Middle - M
Low/Down - D
price calculate according to your selection
after this system asks question
do you want snacks if you want type Y
otherwise type N
then finally bill generated.
"""
ticket = input("Enter Which seat Do you want to Book (B/M/D):")
cost = 0  # initially out price is Zero
if ticket == 'B':
    print("ticket cost is 300")
    cost += 300
elif ticket == 'M':
    print("ticket cost is 200")
    cost += 200
else:
    print("ticket cost is 100")
    cost += 100
snacks = input("if you want to snacks press (Y/N):")
if snacks == 'Y':
    print("you will have to pay 200")
    cost += 200
else:
    print("you don't pay")
    cost += 0
print(f"your total bill is {cost}")
