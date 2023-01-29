import datetime
import json
import csv
from dateutil import parser
import pandas as pd


def menu():
    print("It's 3 task")
    print("(1)Task_1. Dict in Json file\n"
          "(2)Task_2. Dict from csv file\n"
          "(3)Task_3. Nasted Tuples in csv file\n"
          "(4)Exit")
    answer = input("Write what task you want: ")
    if answer == "1":
        data_json()
    elif answer == "2":
        parse_csv()
    elif answer == "3":
        task_3()
    elif answer == "4":
        exit()
    else:
        print("I don't understant, what you want...Okay let's try again")
        return menu()

def back():
    print("if you want to come back to menu enter 'back'. If you want to close the program write 'exit'")
    back = str(input().title())
    if back == 'Back':
        # this condition means return when typing "back" or close the program when typing "exit"
        return menu()
    elif back == 'Exit':
        exit()

# task_1
data = [{
    "Name": "Sviatoslav",
    "Surname": "Nykolyn",
    "Age": 18,
    "Study": "LNU",
    "Hobby": "History",
    "Book": "1984",
    "Film": "Back to future",
    "Married": "No",
    "Category": "Python Basic",
    "Rating": 1
    },
    {
        "Name": "Roman",
        "Surname": "Molchan",
        "Age": 18,
        "Study": "Politech",
        "Hobby": "football",
        "Book": "don't read",
        "Film": "dont't have",
        "Married": "No",
        "Category": "C++",
        "Rating": 2
    },
    {
        "Name": "Mykola",
        "Surname": "Mykhailuk",
        "Age": 19,
        "Study": "don't have",
        "Hobby": "Music",
        "Book": "Harry Potter",
        "Film": "Harry Potter",
        "Married": "Yes",
        "Category": "Python Basic",
        "Rating": 4
    }]

def data_json():
    with open("task_1.json", "w+") as file:
        json.dump(data, file, indent=10)
        json_str = json.dumps(data, indent=10)
        print(json_str)
        back()



# task_2
def parse_csv():

    data2 = [["Firstname", "Lastname", "Birthdate", "Marks", "Comments"],
             ['Ada', 'Lovelace', parser.parse('1985/12/10').date(), [4242,1010], 'The first one'],
             ["Linus", "Torvald", parser.parse('12/28/1969').date(), [42,21], "Have a problem with penguin"],
             ["Theo", "De Raadt", parser.parse('05/19/1968').date(), [18,19,20], "This guy is just crazy"],
             ["Dennis", "Ritchie", parser.parse('09/09/1941').date(), [20,20,20], "Like a boss"],
             ["Alan", "Turing", parser.parse('06/23/1912').date(), [42,42,42], "Shouldn't eat apple"]]



    with open("task2.csv", "w+") as file:
        writer = csv.writer(file)
        for row in data2:
            writer.writerow(row)

    with open("task2.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
        print(json.dumps(list_of_dict, indent=5))
    back()



#task_3
meteo = [(('temperature', 42),
          ('date', datetime.date(2017, 1, 22)),
          ('locations', ('Berlin', 'Paris')),
          ('weather', 'sunny')),
         (('temperature', -42),
          ('date', datetime.date(2017, 1, 22)),
          ('locations', ('Marseille', 'Moscow')),
          ('weather', 'cloudy'))]





def task_3():
    my_dict = list(map(dict, meteo))
    print(my_dict)

    with open("task_3.csv", "w+") as file:
        datf = pd.DataFrame.from_dict(my_dict)
        datf.to_csv(r'task_3.csv', index=False, header=True)


    with open("task_3.csv", "r") as f:
            dict_reader = csv.DictReader(f)
            list_of_dict = list(dict_reader)
            print(json.dumps(list_of_dict, indent=4))
    back()


menu()
