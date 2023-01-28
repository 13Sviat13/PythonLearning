import numpy as np

def menu():
    print("Choose the task(write from 1 to 5)")
    print("Task_1. Output file without .dot\n"
          "Task_2. Output only surname from file\n"
          "Task_3. Output only data from file\n"
          "Task_4. Sort string by length and overwrites it from file")
    answer = input()
    if answer == '1':
        open_without()
    elif answer == '2':
        surname_journal()
    elif answer == '3':
        read_from_txt()
    elif answer == '4':
        sort_by_length()
    elif answer == '5':
        exit()


# task_1
def open_without():
    # this function output text from file in one line and without '.'
    with open('domains.txt', 'r') as file:
        for line in file:
            read = file.read()
            replace = read.replace('.', '')
            lines = replace.splitlines()
            print(lines)





# # task_2
def surname_journal():
    names = "17. Malynovskyi  France\n" \
             "15. Mudryk       England\n"\
             "3.  Sydorchuk    Ukraine\n"\
             "14. Zinchenko    England\n"\
             "13. Lunin        Spain\n"\
             "9.  Yaremchuk    Belgium\n"\
             "10. Tsigankov    Spain\n"\
             "7.  Yarmolenko   UAA"

    journal = open('names.txt', 'w')

    str = journal.write(names)
    arr = names.split()
    print(arr)
    our_array = np.array(arr)
    numpy = np.array_split(our_array, 24)
    chunked_list = [list(array) for array in numpy]
    print(chunked_list[1::3])



# task_3
def read_from_txt():
    opening = open('authors.txt', 'r')
    reading = opening.read()
    read = reading.split("\n")
    d = []
    for lines in read:
        date = lines.split("-")
        if date[0] and not date[0][0].isalpha():
            d.append(({"date": date[0]}))
        else:
            continue
    print(d)



def sort_by_length():
    new = "big better stongest\n" \
          "master mini fool\n" \
          "ki-ki karol binial"
    file = open("file with symbols.txt", "w")
    file_write = file.write(new)
    file.close()
    file1 = open("file with symbols.txt", "r+")
    line = file1.readlines()
    print(line)
    line1 = sorted(line, key=len)
    file1.seek(0)
    file1.writelines(line1)
    print(line1)
    file1.close()


menu()