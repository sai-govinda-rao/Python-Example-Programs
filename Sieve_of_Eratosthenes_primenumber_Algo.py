"""
Sieve of Eratosthenes Prime Numbers Print Method less Efficiency (Less Time Complexity)
Print prime numbers for the below range
suppose we want to print all prime numbers below 100
this algo print all prime numbers below 100 by taking less time complexity
this algo better than two pointers algorithm

print below 100 prime numbers
two pointers algo take 0.000997304916381836 ms(milliseconds)
The Sieve of Eratosthenes take 0.0 ms
"""

import time
num = int(input("Enter The Number:"))
start = time.time()  # program start time
numbers_list = []
for i in range(num+1):
    numbers_list.append(True)

p = 2
while p*p <= num:

    if numbers_list[p]:

        for i in range(p*p, num+1, p):
            numbers_list[i] = False
    p += 1

for i in range(2, num+1):
    if numbers_list[i]:
        print(i, end=" ")
end = time.time()  # program end time
print()
print(end-start)