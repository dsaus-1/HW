
class Bottle:
    color = 'Оранжевая'
    volume = 0.33

bottle_1 = Bottle()
bottle_2 = Bottle()
bottle_3 = Bottle()
bottle_1.color = 'Красная'
bottle_1.volume = 0.7
bottle_2.color = 'Белая'
bottle_2.volume = 0.3
bottle_3.color = 'Черная'
bottle_3.volume = 1.0

# print(bottle_1.color, bottle_1.volume)
# print(bottle_2.color, bottle_2.volume)
# print(bottle_3.color, bottle_3.volume)


class Bottle:
    color = 'Оранжевая'
    contains = 100


    def __init__(self):
        self.contains = 0

    def get_content(self):
        return self.contains

    def fill(self, volume):
        self.contains += volume


# bottle_1 = Bottle()
# bottle_1.color = 'Красная'
#
# bottle_2 = Bottle()
# bottle_2.color = 'Синяя'
#
# print(bottle_1.color, bottle_1.get_content())
# bottle_1.fill(100)
# print(bottle_1.color, bottle_1.get_content())
# print(bottle_2.color, bottle_2.get_content())
# bottle_2.fill(500)
# print(bottle_2.color, bottle_2.get_content())



class TodoList:
    tasks = []

    def __init__(self):
        self.tasks = []

    def add_task(self, name_task):
        self.tasks.append(name_task)


todo_list = TodoList()

todo_list.add_task('Купить лампочку')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Выкинуть лампочку')


#print("\n".join(todo_list.tasks))


class DataBase:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, cls).__new__(cls)
        return cls.instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)
# print(db is db2)