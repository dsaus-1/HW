
class Person:

    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio):
            self.__fio = fio
        if self.verify_age(age):
            self.__age = age
        if self.verify_weight(weight):
            self.__weight = weight
        if self.verify_ps(passport):
            self.__passport = passport


    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        if len(fio.split(' ')) < 3:
            raise TypeError('Неверный формат записи ФИО')
        for i in fio.split(' '):
            if i.isalpha() == False:
                raise TypeError('В ФИО можно использовать только буквенные символы')
            if len(i) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
        return True

    @classmethod
    def verify_age(cls, age):
        if type(age) == int and 14 <= age <= 150:
            return True
        else:
            raise TypeError('Возраст должен быть целым числом от 14 до 150')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) == float and 25 <= weight:
            return True
        else:
            raise TypeError('Вес должен быть вещественным числом от 25 и выше')

    @classmethod
    def verify_ps(cls, passport):
        if type(passport) != str:
            raise TypeError('Паспорт должен быть строкой')
        if len(passport.split(' ')) != 2 or len(passport.split(' ')[0]) != 4 or len(passport.split(' ')[1]) != 6:
            raise TypeError('Неверный формат паспорта')
        if passport.split(' ')[0].isdigit() == False or passport.split(' ')[1].isdigit() == False:
            raise TypeError('Серия и номер паспорта должны содержать только числа')
        return True

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        if self.verify_fio(fio):
            self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if self.verify_age(age):
            self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if self.verify_weight(weight):
            self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if self.verify_ps(passport):
            self.__passport = passport

