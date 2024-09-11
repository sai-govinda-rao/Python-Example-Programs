# Calculator
def add(num1, num2):
    c = num1+num2
    return c


def sub(num1, num2):
    c = num1-num2
    return c


def mul(num1, num2):
    c = num1*num2
    return c


def div(num1, num2):
    c = num1/num2
    return c


operations_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    a = float(input("Enter The Number:"))
    while True:
        for i in operations_dict:
            print(i)
        operation = input("Enter Your Choice:")
        b = float(input("Enter The Number:"))
        answer = operations_dict[operation](a, b)
        print(f"{a}{operation}{b}={answer}")
        response = input("If you want to continue calculate with output then type 'y'\n"
                         "if you want to calculate new then type 'n'\nIf you want to Exit then type 'e':").lower()
        if response == "y":
            a = answer
        elif response == "n":
            calculator()
        else:
            exit()


if __name__ == "__main__":
    calculator()

"""
output:

Enter The Number:200
+
-
*
/
Enter Your Choice:*
Enter The Number:10
200.0*10.0=2000.0
If you want to continue calculate with output then type 'y'
if you want to calculate new then type 'n'
If you want to Exit then type 'e':y
+
-
*
/
Enter Your Choice:*
Enter The Number:10
2000.0*10.0=20000.0
If you want to continue calculate with output then type 'y'
if you want to calculate new then type 'n'
If you want to Exit then type 'e':n
Enter The Number:10
+
-
*
/
Enter Your Choice:+
Enter The Number:10
10.0+10.0=20.0
If you want to continue calculate with output then type 'y'
if you want to calculate new then type 'n'
If you want to Exit then type 'e':e

"""



