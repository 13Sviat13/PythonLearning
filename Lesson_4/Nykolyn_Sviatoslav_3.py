import math
import string
import re

# task_1
def range_n(arg_from: int, arg_to: int, number: int) -> bool:

    if  number > arg_from and number < arg_to :
        return True
    else:
        return False


arg_from = (input("Write your range from: "))
arg_to = int(input("Write your range to: "))

if arg_from == "":
    arg_from = 0
number = int(input(f"Write number  from {arg_from} to {arg_to}: "))
print(range_n(arg_from, arg_to, number))




#task_2
def arithmetic (a: float, b: float, operator: str) -> None:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        print("Unknown action")


print("So, what do u want?")
a = float(input("a = "))
b = float(input("b = "))
operator = str(input("Choose a operation('+' '-' '*' '/'): "))
print(arithmetic(a = a, b = b, operator = operator))

#task_3
def palindrome(phrase:str):
    if phrase == str(phrase)[::-1]:
        print("It's palindrome")
    else:
        print("It's not palindrome")

phrase = str(input("Alright, write me the seventh phrase and still will check it if this phrase is palindrome: "))
print(palindrome(phrase))

#task_4
def rewrithing(sent, *unwanted_char):
    _char = str((input("Write unwanted char:")))

    rewrite = sent.replace(_char, '')
    print(rewrite)
    print("If you want delete some symbol write 'y'")
    answer = str(input())
    if answer == 'y':
        return rewrithing(rewrite)
    else:
        exit()




sent = str(input("Say me some interesting with symbols: "))
print("Oh, interesting...")
print(rewrithing(sent))


