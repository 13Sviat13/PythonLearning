import random

#task1
print("Now, let's see the random number:")
n = random.randint(0, 59)

if n <= 15 and n != 15:
    print(f"This is the {n} and it is in the first quartet")
elif n <= 30 and n != 30:
    print(f"This is the {n} and it is in the second quarter")
elif n <= 45 and n != 45:
    print(f"This is the {n} and it is in the third quarter")
else:
    print(f"This is the {n} and it is in the fourth quarter")

# task2

print("Okay, say me your birthday month number: ")
name_of_birth = int(input())

if (name_of_birth <= 3 or name_of_birth == 12) and name_of_birth != 3:
    if name_of_birth == 0:
        print("Emm, do you know this month of season? ")
    else:
        print(f"Winter({name_of_birth}) - It was snowing outside the window.")
elif name_of_birth <= 6 and name_of_birth != 6:
    print(f"Spring({name_of_birth})  - Everything around blossomed.")
elif name_of_birth <= 9 and name_of_birth != 9:
    print(f"Summer({name_of_birth})  - Children enjoyed the summer vacation.")
elif name_of_birth <= 12 and name_of_birth != 12:
    print(f"Autumn({name_of_birth})  - Everything around lit up with bright colors.")
elif str(name_of_birth):
    print(f"{name_of_birth}, man I have already said that number of month, I don't say you write any letter")
else:
    print("If you don't know, a year have 12 months")

print("Nah, that's too easy!\nSay me the month of your birthday")

name = str(input().title())

if name == "January" or name == "Februaru" or name == "December":
    print(f"Good boy {name}, this is winter I know")
elif name == "March" or name == "April" or name == "May":
    print(f"Wow...It's {name}, this is time when nature wakes up")
elif name == "June" or name == "July" or name == "August":
    print(f"You're hot guy. Its {name} and this is summer")
elif name == "September" or name == "October" or name == "November":
    print(f"Bruh...really? Is this {name}? It's always raining")
else:
    print("Man, you are really thinking, that I'm robot. Am I stupid?")

#task3
print("So let's find number that divisible by 6. Don't worry, I choose numbers myself")
n = [random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)]
sum_number = sum(n)
print(sum_number)
if sum_number % 3 == 0:
    print("As you see, the number devisible by 6")
else:
    print("As you see, the number doesn't devisible by 6")

#task_4
print("Now it is the last task, I think you're ready. I will need your help")
print("Now, we will see in which coordinate quarter the coordinate points are located")
print("So, please enter the points x and y: ")
x = float(input())
y = float(input())
print("So, let's check:")
if x > 0 and y > 0:
    print("It's easy points are located in I quarter")
elif x < 0 and y > 0:
    print("So, the points are located in II quarter")
elif x < 0 and y < 0:
    print("Hmm, the points are located in III quarter")
elif x > 0 and y < 0:
    print("The point are located in IV quarter")
elif x == 0 and y == 0:
    print("Ha-ha the points are at the beginning coordinate")
elif x == 0:
    print("The points are on the axis Y")
elif y == 0:
    print("The points are on the axis X")
print("So that's all. Have a nice day!")
