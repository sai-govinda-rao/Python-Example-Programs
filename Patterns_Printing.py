"""
Print the following pattens
Pattern 1:
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
# code for above pattern
size = 5
for i in range(1, size+1):
    for j in range(1, size+1):
        print(i, end=" ")
    print()

"""
Pattern 2:
1
1 2 
1 2 3
1 2 3 4 
1 2 3 4 5
"""
# code for above pattern
size = 5
for i in range(1, size+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""
Pattern 3:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
# Code for above pattern
size = 5
for i in range(size, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()


"""
Pattern 4:
        1
      1   2
    1  2  3  4
  1  2  3  4  5  6
"""
# code for above pattern
size = 5
for i in range(1, size):
    for j in range(1, size-i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print(k, end=" ")
    print()

"""
Pattern 5:
    --> 1 2 3 4 5
        5 4 3 2 1 <--
    --> 1 2 3 4 5
        5 4 3 2 1 <--
"""
# Code for above pattern
num = 6
for i in range(num):
    if i%2 == 0:
        print("--> ", end="")
        for j in range(1, num+1):
            print(j, end=" ")
        print()
    else:
        print("    ",end="")
        for j in range(num, 0, -1):
            print(j, end=" ")
        print("<--")

