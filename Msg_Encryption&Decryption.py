"""
Encrypt And Decrypt The Message by using key
Encryption is done by Sender
Suppose Our Message is "Hello World" and Key = 5
        H  e  l  l  o  W  o  r  l  d
        8  5 12 12 15 23 15 18 12  4
       +5 +5 +5 ..................+5
       13 10 17 17 20..............9
       m  j  q  q  t  b  t  w  q  i
our Encrypt message is mjqqtbtwqi

Decryption is done by Receiver
        m  j  q  q  t  b  t  w  q  i
       13 10 17 17 20  2 20  23 17 9
       -5 -5 -5 ..................-5
       8  5 12 12 15 23 15 18 12  4
       H  e  l  l  o  W  o  r  l  d

"""

letters = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encryption(a, b):
    encrypt_list = ""
    for i in a:
        if i == " ":
            encrypt_list += " "
        else:
            index = letters.index(i)
            x = (index + b) % 26
            char = letters[x]
            encrypt_list += char
    print(encrypt_list)


def decryption(a, b):
    decryption_list = ""
    for i in a:
        if i == " ":
            decryption_list += " "
        else:
            index = letters.index(i)
            x = (index - b) % 26
            char = letters[x]
            decryption_list += char
    print(decryption_list)


game_over = True
while game_over:
    answer = input("If you want to Encrypt type 'encrypt' and Decrypt type 'decrypt':").lower()
    if answer == "encrypt":
        word = input("Enter the word:").lower()
        key = int(input("Enter the key size:"))
        encryption(a=word, b=key)
    elif answer == "decrypt":
        word = input("Enter the word:")
        key = int(input("Enter the key size:"))
        decryption(a=word, b=key)
    test = input("If you want to test again type 'yes' other wise type 'no':").lower()
    if test == "yes":
        game_over = True
    elif test == "no":
        game_over = False

"""
Output:
If you want to Encrypt type 'encrypt' and Decrypt type 'decrypt':encrypt
Enter the word:Hello World
Enter the key size:5
mjqqt btwqi
If you want to test again type 'yes' other wise type 'no':yes
If you want to Encrypt type 'encrypt' and Decrypt type 'decrypt':decrypt
Enter the word:mjqqt btwqi
Enter the key size:5
hello world
If you want to test again type 'yes' other wise type 'no':no

"""
