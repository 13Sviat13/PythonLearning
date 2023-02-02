
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
        add()
    else:                    #if everithing good this  condition responsible for performing others functions
        if len(my_list) == 0:  # if you want to choose some function but in your list don't exist any elements program
            # back to function add() to complete at least 2 elements
            print("ERROR!!!!To use this functions  you need fill out min 2 elements in your list:")
            add()
        elif answer == '2':
            earliest()
        elif answer == '3':
            latest()
        elif answer == '4':
            longest()
        elif answer == '5':
            shortest()
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


def add(e=""):
    # # this function means to add a note. The user enters the text of the note,
    # # which is stored in the program and is valid until its completion
    # while True:
    #     # this function will continue until you enter stop
    #     element = str(input("Please enter a number to add to list(if you finish write 'stop'): "))
    #     if element == 'stop':
    #         return menu()
    #     else:
    #         my_list.append(element)
    #         print(f"Updated List {my_list}")
    my_list.append(e)





def earliest():
    # this function displays preserved notes in chronological order - rom the newest to the latest
    print(list(my_list)[::-1])
    back()



def latest():
    # this function displays the saved notes in chronological order - from the most recent to the most recent
    print(list(my_list)[0::])
    back()



def longest():
    # this function displays the saved notes in order of their length - from longest to shortest
    return sorted(my_list, key=len)[::-1]
    # back()




def shortest():
    # this function displays the saved notes in the order of their length - from shortest to longest
    print(sorted(my_list, key=len)[0::])
    back()




print("Hey, I have some easy program that can some manipulation with note")
menu()

