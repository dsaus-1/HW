from connector import Connector

class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, id: int, title: str, price: float, count: int, category: int):
        self.id = id
        self.title = title
        self.price = price
        self.count = count
        self.category = category



    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        return bool(self.count)

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        return self.count

class Category:
    id: int
    title: str
    description: str
    products: list

    def __init__(self, id: int, title: str, description: str, products: list):
        self.id = id
        self.title = title
        self.description = description
        self.products = products

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        #lst_name = [x["title"] for x in self.products]
        return bool(len(self.products))

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        lst = [x.title for x in self.products if x.count>0]
        return len(lst)


class Shop:
    """
    Класс для работы с магазином
    """
    products: list
    categories: list

    def __init__(self, *args, **kwargs):
        self.products = []
        self.categories = []

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        categories_connector = Connector('categories.json')
        categories = categories_connector.read_file()
        count = 0
        for i in categories:
            count += 1
            print(f'Категория {count}: {i["title"]}\nID категории: {i["id"]}')


    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """
        while True:
            category_number = input(f'Введите номер категории: ')
            if category_number.isdigit():
                break
            print('Необходимо ввести номер категории')
        product_connector = Connector('products.json')
        products = product_connector.select({"category": int(category_number)})
        count = 0
        for i in products:
            if i["category"] == int(category_number):
                count += 1
                print(f'{i["title"]}, цена - {i["price"]}, номер товара - {i["id"]} на складе осталось {i["count"]} шт.')
        if count == 0:
            print('Ни один товар из данной категории не был найден.')


    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        while True:
            product_number = input(f'Введите номер товара: ')
            if product_number.isdigit():
                break
            print('Необходимо ввести номер товара')
        product_connector = Connector('products.json')
        products = product_connector.select({"id": int(product_number)})
        for i in products:
            if i["id"] == int(product_number):
                print(f'Название товара: "{i["title"]}", id - {i["id"]}, номер категории - {i["category"]}, цена - {i["price"]}, на складе осталось {i["count"]} шт.')
                break
        else:
            print('Ни один товар с данным номером не был найден.')

if __name__ == '__main__':

    categor = []
    my_shop = Shop()
    my_shop.get_categories()
    my_shop.get_products()
    my_shop.get_product()