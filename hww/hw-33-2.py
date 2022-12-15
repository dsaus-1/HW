import timeit
from functools import partial


class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class PersonTest:
    __slots__ = ('name', 'address', 'email')

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


def get_set_delete(person):

    # def set_data():
    #     return person.name, person.address, person.email
    #
    # def get_data():
    #     person.name = 'Дима'
    #     person.address = "143441 Sadovaya ul."
    #     person.email = "test@mail.ru"
    #
    # def del_data():
    #     del person.name
    #     del person.address
    #     del person.email
    #
    # set_data()
    # del_data()
    # get_data()
    tmp = person.name
    person.email += tmp
    del person.address
    person.address = '143441 Sadovaya ul.'



def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=50000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=50000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")


if __name__ == "__main__":
    main()
