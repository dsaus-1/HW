import json

class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        try:
            with open(self.__data_file, 'r') as open_file:
                json.load(open_file)
                #print('Файл уже существует.')
        except:
            with open(self.__data_file, 'w+') as open_fil:
                json.dump('[]', open_fil)
                #print('Создан новый файл.')


    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.__data_file, 'w') as open_file:
            try:
                file = json.load(open_file)
                file.append(data)
                json.dump(file, open_file)
            except:
                file = [data]
                json.dump(file, open_file)

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open(self.__data_file, 'r') as open_file:
            file = json.load(open_file)
            key = query[list(query.keys())[0]]
            new_file = [x for x in file if x[key] == query[key]]
            return new_file

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        pass
        #with open(self.__data_file, 'w') as open_file:
            #file = json.load(open_file)
            #new_file = [x for x in file if ]


if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)

    data_from_file = df.select({'id': 1})
    assert data_from_file == [data_for_file]

    df.delete(dict())
    data_from_file = df.select(dict())
    assert data_from_file == []