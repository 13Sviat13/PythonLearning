
# Task_1
# class Employee:
#
#     def __init__(self, name, hours, salary):
#         self.name = name
#         self.hours = hours
#         self.salary = salary
#     def getInfo(self):
#         return self.name, self.salary, self.hours
#
#     def AddSal(self):
#         if self.salary < 500:
#             self.salary += 10
#         return self.salary
#
#
#     def AddWork(self):
#         if self.hours > 6:
#             self.salary += 5
#         return self.salary
#
#     def getFinalSalary(self):
#         return self.AddSal() and self.AddWork()
#
#
#
# e = Employee(name=str(input("Write your employee name: ")),
#              salary = int(input("Write employee's salary: ")),
#              hours= int(input("Write employee's hours work: ")))
# print(f'Final salary for {e.name} is {e.getFinalSalary()}')


# Task_2
class Pizza:

    def __init__(self, size, cheese_topping, pepperoni_topping, bacon_topping):
        self.__size = size
        self.__cheese_topping = cheese_topping
        self.__pepperoni_topping = pepperoni_topping
        self.__bacon_topping = bacon_topping


    def get_size(self):
        return self.__size

    def get_cheese_topping(self):
        return self.__cheese_topping

    def get_pepperoni_topping(self):
        return self.__pepperoni_topping

    def get_bacon_topping(self):
        return self.__bacon_topping

    def set_size(self, size):
        self.__size = size

    def set_cheese_topping(self, cheese_topping):
        self.__cheese_topping = cheese_topping

    def set_pepperoni_topping(self, pepperoni_topping):
        self.__pepperoni_topping = pepperoni_topping

    def set_bacon_topping(self, bacon_topping):
        self.__bacon_topping = bacon_topping

    def calc_cost(self):

        if self.__size == "small":
            cost = 10 + (2 * (self.__cheese_topping + self.__pepperoni_topping + self.__bacon_topping))
        elif self.__size == "medium":
            cost = 12 + (2 * (self.__cheese_topping + self.__pepperoni_topping + self.__bacon_topping))
        elif self.__size == "large":
            cost = 14 + + (2 * (self.__cheese_topping + self.__pepperoni_topping + self.__bacon_topping))
        return cost



    def get_description(self):
        return f"This pizza is a {self.__size} with {self.__cheese_topping} cheese toppings," \
               f" {self.__pepperoni_topping} pepperoni toppings, and {self.__bacon_topping} bacon toppings."




e = Pizza('small', 1, 2, 1)
print(f"{str(e.get_description())}... The price is {e.calc_cost()}")


# class PizzaOrder(Pizza):
#     def __init__(self):
#         self.__pizzas = []
#
#     def add_pizza(self, pizza):
#         self.__pizzas.append(pizza)
#
#     def get_pizzas(self):
#         return self.__pizzas
#
#     def get_total_cost(self):
#         cost = 0
#         for pizza in self.__pizzas:
#             cost += pizza.calc_cost()
#         return cost
#
#
#
# pizza1 = Pizza('large', 2, 0, 1)
# print(f"{str(pizza1.get_description())}... The price is {pizza1.calc_cost()}")
# pizza2 = Pizza('medium', 0, 0, 0)
# print(f"{str(pizza2.get_description())}... The price is {pizza2.calc_cost()}")
# pizza3 = Pizza('small', 2, 5, 2)
# print(f"{str(pizza3.get_description())}... The price is {pizza3.calc_cost()}")
# pizza4 = Pizza('large', 2, 1, 2)
#
#
# PizzaOrder()
