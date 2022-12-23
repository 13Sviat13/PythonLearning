import math
import time



#Task1
print("What's your name?  " )
name = input() + " "
print("Well..." + name.title() + "..." + "and.. what's your surname?")
surname = input()
full_name = name + surname
print("Heh I see " + full_name.title() +  " very interesting")

rep_of_names = name*5
print("Okay " + name + "your name..ha-ha some strange\nNo...no I'm not laughing but " + rep_of_names.upper()+"sorry.")
time.sleep(2)
print("Okay, just try again")
name2 = name.replace(" ", "\n")
time.sleep(3)
print("Well " + name2 + "Nice to meet you")

#task2

print(F"Now, my dear {name.title()} let's do some easy math exercise\n Don't worry, it's easy")
time.sleep(2)
print("Let's calculating the length of a circle and the area of a circle")
time.sleep(2)
print(name.title() + "Do you know math formula of calculating (write Yes or No)")
answer = input()
if answer == "Yes":
    time.sleep(4)
    print("Wow, you're very smart..heh, I have already said it")
elif answer == "No":
    time.sleep(4)
    print("I expected it, look in internet if you are interesting in it")
else:
    time.sleep(3)
    print("I don't understand, you know it's easy question. You need write yes or not. Well, don't worry")

time.sleep(3)
print("Okay, write me some radious")
R = float(input())
time.sleep(3)
print(F"Well...{R} cm Okay, What do you want to calculating? No, I decide it myself." )
print("The first it will be the length of a circle ")
L = (2 * math.pi * R)
time.sleep(3)
print(F"So it's {L} cm And the next is the area of a circle")
S = (math.pi * R ** 2)
time.sleep(3)
print(F"It will be {S} cm great!")
print(F"So the length  and the area of a circle will be {L} cm, {S} cm")

#task_3
dollar = float(36.65)
time.sleep(3)
print(name.title() + "Do you know, how much dollar is? (Write Yes or No)")
answer = input()
if answer == "Yes":
    time.sleep(4)
    print("Oh, we have the smartest person another one! Great")
elif answer == "No":
    time.sleep(3)
    print("Ha-ha, the robot and human 1:0")
else:
    time.sleep(3)
    print("I don't understand, you know it's easy question. You need write yes or not. Well, don't worry")
print("Now, write some sum of grn and I convert in dollars")
time.sleep(3)
grn = float(input())
print(F"Okay  {grn} grn. Let's see")
time.sleep(5)
conv = float(grn / dollar)
print("Okay, it will be:")
print(round(conv), 3)



