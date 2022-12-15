
class InvalidAgeError(Exception):
    try:
        age = int(input('Введите ваш возраст: '))
        if age < 0 or age >= 120:
            raise InvalidAgeError('Извините, этот возраст не корректен')
        print(f'Вам {age} лет')
    except ValueError:
        print('Возраст должен быть числом')
    except InvalidAgeError as e:
        print(e)


