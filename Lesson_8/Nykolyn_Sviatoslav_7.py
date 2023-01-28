import datetime
import json
import csv
from  collections import defaultdict

import numpy
from dateutil import parser
import pandas as pd

task_1
data = [{
    "Name": "Sviatoslav",
    "Surname": "Nykolyn",
    "Category": "Python Basic",
    "Rating": 2
    },
    {
        "Name": "Oleksandr",
        "Surname": "Osadchyi",
        "Category": "Python basic",
        "Rating": 1,
    },
    {
        "Name": "Mykyta",
        "Surname": "Klochko",
        "Category": "Python Basic",
        "Rating": 3,
    }]

def data_json():
    with open("task_1.json", "w+") as file:
        json.dump(data, file, indent=4)
        json_str = json.dumps(data, indent=4)
        print(json_str)


# data_json()

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


parse_csv()

#task_3
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


meteo = [(('temperature1', 42),
          ('date1', datetime.date(2017, 1, 22)),
          ('locations1', ('Berlin', 'Paris')),
          ('weather1', 'sunny')),
         (('temperature', -42),
          ('date', datetime.date(2017, 1, 22)),
          ('locations', ('Marseille', 'Moscow')),
          ('weather', 'cloudy'))]
arr = numpy.asarray(meteo, dtype=object)

fla_arr = arr.flatten()
print(fla_arr)
my_dict = Convert(fla_arr)
print(my_dict)


def turple():
    df = pd.DataFrame(my_dict)
    df.to_csv('task_3.csv', index=False, header=True)
    # with open('task_3.csv.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(meteo)

turple()