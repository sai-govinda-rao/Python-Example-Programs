print("Prime number check program")
# taking input from the user and store it in variable num
num = int(input("Enter the number:"))
count = 0  # initialize count = 0
for i in range(1, num+1):
    if num % i == 0:  # if our number divided by i then increment the count
        count += 1
if count == 2:  # if count is equals to 2 then our number is Prime
    print("Given number is Prime")
else:  # if count is more than 2 our number is Not Prime
    print("Give number is not Prime")








