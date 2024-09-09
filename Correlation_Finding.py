"""
Finding Correlation Between Two categorical Variables
Correlation: It is a statistical tool which is used to know the Association between
two or more categorical variables
Karl pearson Correlation coefficient Finding
formula
    correlation = summation(xy)/SquarerRoot(summation(x-square) summation(y-square))
    x-values = 105 104 102 101 .........Etc
    y-values = 101 103 100 98  .........Etc
"""


import math
import pandas as pd

print("Enter the Variables Which you want Find Co-Relation")
variable_1 = input("Enter The First Variable:")  # Enter Variable 1 Ex: Study
variable_2 = input("Enter The Second Variable:")  # Enter Variable 2 Ex: Mobile
# We will know the relation b/w them and how mobiles effect on study
a = input("Enter The Past Data From Variable 1 (values are Separated by space):")
b = input("Enter The Past Data From Variable 2 (values are Separated by space):")
# Enter Values separated by space
c = a.split(" ")
d = b.split(" ")
past_data_1 = []
count_1 = 0
for i in c:
    count_1 += 1
    i = int(i)
    past_data_1.append(i)
past_data_2 = []
count_2 = 0
for i in d:
    count_2 += 1
    i = int(i)
    past_data_2.append(i)


def finding_x_values():
    summation_x = 0
    x_values = []
    for values in past_data_1:
        summation_x += values
    x_bar = summation_x/count_1
    for i in past_data_1:
        x_values.append(i-x_bar)
    x_square_values = []
    for i in x_values:
        x_square_values.append(i**2)
    summation_x_square = 0
    for i in x_square_values:
        summation_x_square += i
    return summation_x_square, x_values , x_square_values


def finding_y_values():
    summation_y = 0
    y_values = []
    for values in past_data_2:
        summation_y += values
    y_bar = summation_y/count_2
    for i in past_data_2:
        y_values.append(i-y_bar)
    y_square_values = []
    for i in y_values:
        y_square_values.append(i**2)
    summation_y_square = 0
    for i in y_square_values:
        summation_y_square += i
    return summation_y_square, y_values, y_square_values


if count_1 == count_2:
    summation_x_square, x_values, x_square_values = finding_x_values()
    summation_y_square, y_values, y_square_values = finding_y_values()
    summation_xy = 0
    xy_values = []
    for i,j in zip(x_values,y_values):
        xy_values.append(i*j)
        summation_xy += i*j
    correlation = summation_xy/math.sqrt(summation_x_square*summation_y_square)
    data = {
        "IR": past_data_1,
        "ER": past_data_2,
        "X-values": x_values,
        "Y-values": y_values,
        "XY-values": xy_values,
        "X-Square": x_square_values,
        "Y-Square": y_square_values
    }
    table = pd.DataFrame(data)
    print(table)
    print(correlation)
    if correlation < 0.5:
        print(f"There is Weak Correlation Between {variable_1} and {variable_2}")
    else:
        print(f"There is Strong Correlation Between {variable_1} and {variable_2}")

"""
Output: 
Enter the Variables Which you want Find Co-Relation
Enter The First Variable:study
Enter The Second Variable:mobile
Enter The Past Data From Variable 1 (values are Separated by space):105 104 102 101 100 99 98 96 92 92
Enter The Past Data From Variable 2 (values are Separated by space):101 103 100 98 95 96 104 92 97 94
    IR   ER  X-values  Y-values  XY-values  X-Square  Y-Square
0  105  101       6.1       3.0       18.3     37.21       9.0
1  104  103       5.1       5.0       25.5     26.01      25.0
2  102  100       3.1       2.0        6.2      9.61       4.0
3  101   98       2.1       0.0        0.0      4.41       0.0
4  100   95       1.1      -3.0       -3.3      1.21       9.0
5   99   96       0.1      -2.0       -0.2      0.01       4.0
6   98  104      -0.9       6.0       -5.4      0.81      36.0
7   96   92      -2.9      -6.0       17.4      8.41      36.0
8   92   97      -6.9      -1.0        6.9     47.61       1.0
9   92   94      -6.9      -4.0       27.6     47.61      16.0
0.581181896736668
There is Strong Correlation Between study and mobile

"""