import csv
import pandas

def input_data_to_csv():
    with open("demo.csv", "w") as file:
        header = ["First", "Second", "Third"]
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        data_frame = pandas.DataFrame(data, columns=header)
        data_frame.to_csv("task1.csv", index=False)
        data_read = pandas.read_csv('task1.csv')
        # print(data_read)
        print(data_read.columns)


input_data_to_csv()