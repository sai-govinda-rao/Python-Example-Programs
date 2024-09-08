"""
Solving Coding And Decoding Problem
System will accept input from user like below
abc:efg::ejo:?
a ----> e, b ----> f, c ----> g
   +4         +4         +4
similarly System can solve ejo
display the result --> ins
"""

letters = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
question = input("Enter the Question(abc:fgh::sai:?) like This:")
list_1 = question.split("::")
list_2 = list_1[0]
list_3 = list_2.split(":")
first = list_3[0]
second = list_3[1]
answer_list = list_1[1].split(":")
length_1 = len(first)
length_2 = len(second)
count = 0
if length_1 == length_2:
    for i, j in zip(first, second):
        index_1 = letters.index(i)
        index_2 = letters.index(j)
        count += index_2-index_1
    total = count/length_1
    answer = ""
    for i in answer_list[0]:
        value = int((letters.index(i)+total) % 26)
        if value == 0:
            value = 26
        answer += letters[value]
    print(answer)
else:
    print("I Can't Solve This type of problems")
