"""
Print 1 to N numbers without loops Using is a crazy thing
Imagine how to do this..............?
I'll try to print 1 to N numbers without using loops
example:
    number = 10
    1 2 3 4 5 6 7 8 9 10
"""

num = int(input("Enter Number:"))   # taking number from user
count = 1  # initially count set to 1


def loop(count):  # create a function name loop and pass count parameter
    if count <= num:  # check if count less than or equals to N
        print(count, end=" ")  # if condition satisfies print count
        count += 1  # soon as increase count to 1
        loop(count)  # again call the loop function and pass incremented count
    """
    Above loop run until condition satisfies
    once condition is false Exit the function
    """


loop(count)

"""
output:
    Enter Number:20
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
    
    Enter Number:10
    1 2 3 4 5 6 7 8 9 10
"""