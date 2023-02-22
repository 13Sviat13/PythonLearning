
# task_1

class GPA:
    def __init__(self, name, hours, points):
        self.name = name
        self.hours = hours
        self.points = points

    def getinformation(self):
        return self.name, self.hours, self.points


    def getGPA(self):
        formula = self.points / self.hours
        if formula < 1.5 and self.hours == 30 or formula < 1.75 and self.hours == 60 or formula < 2.0:
            print(f"{self.name} have academic warnings")
            return formula
        else:
            print(f"{self.name} is good")


try:
    student1 = GPA(name=str(input("Write your student's name: ")),
             hours = int(input("Write students's hours studing: ")),
             points= float(input("Write employee's total point: ")))
    student2 = GPA(name=str(input("Write your student's name: ")),
             hours = int(input("Write students's hours studing: ")),
             points= float(input("Write employee's total point: ")))
    student3 = GPA(name=str(input("Write your student's name: ")),
             hours = int(input("Write students's hours studing: ")),
             points= float(input("Write employee's total point: ")))
    GPA.getGPA(student1)
    GPA.getGPA(student2)
    GPA.getGPA(student3)
except ValueError:
    print("You need write some information and hours must be in integer without point or any symbols")
#
#

# task_2
file = open('file.txt', 'w')
write = file.write("I want to write too long line to enter my error so i write and write until it happens")
file.close()

class ExceptionLineTooLong(Exception):
    def __init__(self, message):
        self.message = message

    def read_file(filename):
        with open(filename) as file:
            for line in file.readlines():
                if len(line) > 80:
                    raise ExceptionLineTooLong("Line is too long!")
                else:
                    print(line)


try:
    read_file = ExceptionLineTooLong
    read_file.read_file('file.txt')
except ExceptionLineTooLong as err:
    print(err)
except Exception as e:
    print(e)
except FileNotFoundError:
    print("No such file or directory")


# task3

file3 = open('task3.txt', 'w')
file3.write('12')
# file3.write('123.1')
file3.close()
class Check:

    @staticmethod
    def fileExists(filename) -> bool:
        try:
            with open(filename, 'r') as f:
                print("True")
        except FileNotFoundError:
            print("Talse")

    @staticmethod
    def isInt(s):
        with open(s, 'r') as f:
            for line in f.readlines():
                if int(line):
                    print("True")
                else:
                    raise ValueError

    @staticmethod
    def isDouble(s):
        with open(s, 'r') as f:
            for line in f.readlines():
                if float(line):
                    print("True")
                else:
                    raise ValueError


try:
    clas = Check()
    clas.fileExists('task3.txt')
    clas.isInt('task3.txt')
    with open('task3.txt', 'w') as f:
        f.write("123.1")
        f.close()
    clas.isDouble('task3.txt')
    clas.isInt('task3.txt')
except ValueError:
    print("False")


