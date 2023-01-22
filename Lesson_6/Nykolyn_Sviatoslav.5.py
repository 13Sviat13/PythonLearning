import random

# task_1
list1 = []
list2 = []

#
def menu():
    # this function responsible for the menu
    print("Choose what task you want to check")
    print("Choose:"
        "\nTask 1. Sorted to lists"
        "\nTask 2. Dictionary of students"
        "\nTask 3. Determine the difference in values"
        "\nTask 4. Lists with 10000 numbers"
        "\nTask 5. List with space"
        "\nExit")
    answer = str(input("Your choice is(You need enter from 1 to 5. If you want close the program enter 'exit'):\n"))
    if answer == '1':
        return add()
    elif answer == '2':
        journal()
    elif answer == '3':
        if len(list1) or len(list2) == 0:  # if you want to choose some function but in your list don't exist any elements program
            # back to function add() to complete at least 2 elements
            print("ERROR!!!!To use this functions  you need fill out min 2 elements in your list:")
            add2()
        else:
            unique_numbers()
    elif answer == '4':
        listrange()
    elif answer == '5':
            print(space())
    elif answer.title() == "Exit":
            exit()
    else:
        print("I don't really understand what do you write...Fine, let's do it again")
        return menu()

def back():
    print("if you want to come back to menu enter 'back'. If you want to close the program write 'exit'")
    back = str(input().title())
    if back == 'Back':
        # this condition means return when typing "back" or close the program when typing "exit"
        return menu()
    elif back == 'Exit':
        exit()

def add():
    while True:
        element = input("Please enter a number to add to list(to fill out second list write 'stop'): ")
        if element == 'stop':
            while True:
                 element2 = input("Please enter a number to add to second list(to stop write 'finish': ")
                 if element2 == 'finish':
                      return two_set()
                 else:
                    list2.append(element2)
                    print(f"Updated List {list2}")
        else:
                list1.append(element)
                print(f"Updated List {list1}")


def add2():
    # this function means to add a note. The user enters the text of the note,
    # which is stored in the program and is valid until its completion
    while True:
        # this function will continue until you enter stop
        element = input("Please enter a number to add to list(to fill out second list write 'stop'): ")
        if element == 'stop':
            while True:
                element2 = input("Please enter a number to add to second list(to stop write 'finish': ")
                if element2 == 'finish':
                    return unique_numbers()
                else:
                    list2.append(element2)
                    print(f"Updated List {list2}")
        else:
            list1.append(element)
            print(f"Updated List {list1}")



def two_set():
    # this function find a similar values and dispalys it in ascending order
    list_1_to_list = set(list1)
    list_2_to_list = set(list2)
    list_3_to_list = list_1_to_list.intersection(list_2_to_list)
    list_res = list(list_3_to_list)
    print(list_res)
    print(sorted(list_res, reverse=False))
    return list_res
    



# # task_2
def journal():
    dict_journal  = {'Merlin Berlin': 12,
                    'Roman Molchan': 2,
                    'Mykola Mykhailyuk': 3,
                    'Kyrylo Dub': 5,
                    'Oleg_Suvorov': 9,
                    'Andriy Bevz': 10,
                    'Sirkan Bulat': 11,
                    'Dmytriy Gordon': 8}
    print(dict_journal)
    avarage_value = ((sum(dict_journal.values())/len(dict_journal.values())))
    print(avarage_value)

    for key, value in dict_journal.items():
        if value > avarage_value:
            print(key)
    back()



# task_3
def unique_numbers():
    list_1_to_set = set(list1)
    list_2_to_set = set(list2)
    print(list_1_to_set)
    print(list_2_to_set)
    list_3_to_list = list_1_to_set.symmetric_difference(list_2_to_set)
    print(list_3_to_list)
    print(len(list_3_to_list))
    back()


# task_4
def listrange():
    print("Hi, I can create random items in lists and sorted them")
    list1 = random.sample(range(1, 10000), 10)
    list2 = random.sample(range(1, 10000), 11 )
    print(list1)
    print(list2)
    print(sorted(list1, reverse=False))
    print(sorted(list2, reverse=False))
    back()


# task_5
def space():
    counts = dict()
    sentences = 'one two three one four five seven ten seven one'
    words = sentences.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts



menu()



