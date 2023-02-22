import csv
import json

class Product:
    def __init__(self, category, name, price, quantity):
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'category: {self.category}\n {self.name}\n  Price: {self.price} UAH\n  ' \
               f'{"Є в наявності" if self.quantity > 0 else "Немає в наявності"}\n  '



class TV(Product):
    def __init__(self, name,  price, quantity,   brand, diagonin, smartTV):
        super().__init__('TV', name,  price, quantity)
        self.brand = brand
        self.diagonin = diagonin
        self.smartTV = smartTV

    def __str__(self):
        return f'Tелевізор {super().__str__()}'


class Headphones(Product):
    def __init__(self, name,  price, quantity,  brand, bluetooth, headphone, battery):
        super().__init__('Headphones', name,  price, quantity)
        self.brand = brand
        self.bluetooth = bluetooth
        self.headphone = headphone
        self.battery = battery

    def __str__(self):
        return f'Наушники {super().__str__()}'

class Bluetooth_speakers(Product):
    def __init__(self, name,  price, quantity,  brand, usb, version):
        super().__init__('Bluetooth', name,  price, quantity)
        self.brand = brand
        self.usb = usb
        self.version = version

    def __str__(self):
        return f'Блютуз колонка {super().__str__()}'





my_products = [
    TV("Samsung uniNewEra", 15000, 10,  "Samsung", '43', "true"),
    TV("LG airTV", 17999, 10,  "LG", '41', "true"),
    TV("Philips", 14780, 10,  "Philips", '47', "true"),
    Headphones("Apple AIRPODS PRO",  6450, 24, "Apple", "true", "in-ear", '6'),
    Headphones("Apple AIRPODS MAX",  31670, 12, "Apple", "true", "headphones", '12'),
    Bluetooth_speakers("Phillips VOME TRUE", 5785, 25, "Phillips", "true", 3.0)

]

with open("Product.csv", 'w', newline='') as csvfile:
    fieldnames = ['category', 'name',  'price', 'quantity', 'additional_fields']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for Product in my_products:
        if isinstance(Product, TV):
            writer.writerow({'category' : Product.category, 'name': Product.name,  'price': Product.price, 'quantity': Product.quantity,
                             'additional_fields': {"brand": Product.brand, "Diagonal" : Product.diagonin,
                                                   "SmartTV" : Product.smartTV}})
        elif isinstance(Product, Headphones):
            writer.writerow({'category' : Product.category, 'name': Product.name, 'price': Product.price, 'quantity': Product.quantity,
                             'additional_fields': {"brand": Product.brand, "bluetooth" : Product.bluetooth,
                                                   "headphone type":Product.headphone, "battery_hours" : Product.battery}})
        elif isinstance(Product, Bluetooth_speakers):
            writer.writerow({'category' : Product.category, 'name': Product.name, 'price': Product.price, 'quantity': Product.quantity,
                             'additional_fields': {"brand": Product.brand, "USB-port" : Product.usb,
                                                   "bluetooth_version" : Product.version}})


def read_products_from_file(file_path):
    with open(file_path, 'r') as r:
        csv_dict_reader = csv.DictReader(r)
        for row in csv_dict_reader:
            additional_fields = json.loads(row['additional_fields'])
            if row['category'] == 'TV':
                print(TV(
                    name=row['name'],
                    price=row['price'],
                    quantity=row['quantity'],
                    brand=additional_fields['brand'],
                    diagonin=additional_fields['diagonal'],
                    smartTV=additional_fields['smartTV']
                      ))
            elif row['category'] == 'Headphones':
                print(Headphones(
                    name=row['name'],
                    price=row['price'],
                    quantity=row['quantity'],
                    brand=additional_fields['brand'],
                    bluetooth=additional_fields['bluetooth'],
                    headphone=additional_fields['headphone_type'],
                    battery=additional_fields['battery_hours']
            ))
            elif row['category'] == "Bluetooth speakers":
                print(Bluetooth_speakers(
                    name=row['name'],
                    price=row['price'],
                    quantity=row['quantity'],
                    brand=additional_fields['brand'],
                    usb=additional_fields['USB-port'],
                    version=additional_fields['bluetooth_version']
                ))
            else:
                raise ValueError(f'Unknown category: {row["category"]}')


def menu():
    print("All products that we have")
    print(read_products_from_file('Product.csv'))

menu()

