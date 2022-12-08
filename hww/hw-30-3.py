import datetime

'''
возможна ли другая реализация списка tasks? не [None] * на какое-то число
чтобы в tasks всегда добавлялся элемент который мы хотим, даже если len изначального списка меньше индекса к которому присваиваем значение
'''

class Task:
    content = ''
    date = None

    def __init__(self, content):
        self.content = content
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f'{self.content} (создано {self.date})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content

    def __hash__(self):
        return hash(self.content)

    def __bool__(self):
        return bool(self.content)


class TodoList:

    def __init__(self):
        self.tasks = [None]*2

    def __setitem__(self, key, value):
        self.tasks[key] = value

    def __getitem__(self, item):
        return self.tasks[item]

    def __repr__(self):
        return str(self.tasks)

    def __delitem__(self, key):
        del self.tasks[key]

# todo_list = TodoList()
# todo_list[0] = Task('Сдать домашку')
# todo_list[1] = Task('Выпить кофе')
# todo_list
# todo_list[0]
# del todo_list[0]
# todo_list