
my_list = []


def menu():
    # this function responsible for the menu
    print("Choose some function that you want to use with your note")
    print("Choose:"
        "\n1.Add the element"
        "\n2.From earliest to latest"
        "\n3.From latest to earliest"
        "\n4.From longest to shortest"
        "\n5.From shortest to longest"
        "\nExit")
    answer = str(input("Your choice is(You need enter from 1 to 5. If you want close the program enter 'exit'):\n"))
    if answer == '1':
        return add()
    else:                    #if everithing good this  condition responsible for performing others functions
        if len(my_list) == 0:  # if you want to choose some function but in your list don't exist any elements program
            # back to function add() to complete at least 2 elements
            print("ERROR!!!!To use this functions  you need fill out min 2 elements in your list:")
            return add()
        elif answer == '2':
            return earliest()
        elif answer == '3':
            return latest()
        elif answer == '4':
            return longest()
        elif answer == '5':
            return shortest()
        elif answer.title() == "Exit":
            exit()
        else:
            print("I don't really understand what do you write...Fine, let's do it again")
            return menu()


def add():
    # this function means to add a note. The user enters the text of the note,
    # which is stored in the program and is valid until its completion
    while True:
        # this function will continue until you enter stop
        element = str(input("Please enter a number to add to list(if you finish write 'stop'): "))
        if element == 'stop':
            return menu()
        else:
            my_list.append(element)
            print(f"Updated List {my_list}")




def earliest():
    # this function displays preserved notes in chronological order - rom the newest to the latest
    print(list(my_list)[::-1])
    print("if you want to come back to menu enter 'back'. If you want to close the program write 'exit'")
    back = str(input().title())
    if back == 'Back':
        # this condition means return when typing "back" or close the program when typing "exit"
        return menu()
    elif back == 'Exit':
        exit()

def latest():
    # this function displays the saved notes in chronological order - from the most recent to the most recent
    print(list(my_list)[0::])
    print("if you want to come back to menu enter 'back'. If you want to close the program write 'exit'")
    back = str(input().title())
    if back == 'Back':
        # this condition means return when typing "back" or close the program when typing "exit"
        return menu()
    elif back == 'Exit':
        exit()

def longest():
    # this function displays the saved notes in order of their length - from longest to shortest
    print(sorted(my_list, key=len)[::-1])
    print("if you want to come back to menu enter 'back'. If you want to close the program write 'exit'")
    back = str(input().title())
    if back == 'Back':
        # this condition means return when typing "back" or close the program when typing "exit"
        return menu()
    elif back == 'Exit':
        exit()

def shortest():
    # this function displays the saved notes in the order of their length - from shortest to longest
    print(sorted(my_list, key=len)[0::])
    print("if you want to come back to menu enter 'back'. If you want to close the program write 'exit'")
    back = str(input().title())
    if back == 'Back':
        # this condition means return when typing "back" or close the program when typing "exit"
        return menu()
    elif back == 'Exit':
        exit()







print("Hey, I have some easy program that can some manipulation with note")
menu()
