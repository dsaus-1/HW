import csv


class Item:
    pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file) as open_file:
            read_file = csv.reader(open_file)
            count = 0
            for atr in read_file:
                if count == 0:
                    count +=1
                    continue
                cls.all.append(Item(atr[0], float(atr[1]), int(atr[2])))

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'


Item.instantiate_from_csv('items.csv')

for item in Item.all:
    print(item)
