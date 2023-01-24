
# task_1
# def open_without():
#     # this function output text from file in one line and without '.'
#     with open('domains.txt', 'r') as file:
#         for line in file:
#             read = file.read()
#             replace = read.replace('.', '')
#             lines = replace.splitlines()
#             print(lines)
#
#
# open_without()

# import numpy as np
# # task_2
# def surname_journal():
#     names  = "17. Malynovskyi  France\n" \
#              "15. Mudryk       England\n"\
#              "3.  Sydorchuk    Ukraine\n"\
#              "14. Zinchenko    England\n"\
#              "13. Lunin        Spain\n"\
#              "9.  Yaremchuk    Belgium\n"\
#              "10. Tsigankov    Spain\n"\
#              "7.  Yarmolenko   UAA"
#
#     journal = open('names.txt', 'w')
#
#     str = journal.write(names)
#     arr = names.split()
#     print(arr)
#     our_array = np.array(arr)
#     numpy = np.array_split(our_array, 24)
#     chunked_list = [list(array) for array in numpy]
#     print(chunked_list[1::3])
#
# surname_journal()

# task_3
def read_from_txt():
    my_dict = {}
    with open('authors.txt') as fileobj:
        for line in fileobj:
            key, value = line.split(":")
            my_dict[key] = value

    print(d)

read_from_txt()

