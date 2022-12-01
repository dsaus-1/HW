import csv


def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    list_file = []
    sort_index = {'date': 0, 'open': 1, "high": 2, 'low': 3, 'close': 4, 'volume': 5, 'Name': 6}
    def partition(list_file, low, high, sort_columns):
        '''
        расчет индекса и замена элементов при сортировке quick_sort
        '''
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = list_file[(low + high) // 2][sort_index[sort_columns[0]]]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while list_file[i][sort_index[sort_columns[0]]] < pivot:
                i += 1
            j -= 1
            while list_file[j][sort_index[sort_columns[0]]] > pivot:
                j -= 1
            if i >= j:
                return j
            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            list_file[i], list_file[j] = list_file[j], list_file[i]

    def quick_sort(list_file, sort_columns):
        '''
        реализация функции сортировки quick_sort
        '''
        # Создадим вспомогательную функцию, которая вызывается рекурсивно

        def _quick_sort(items, low, high, sort_columns):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = partition(items, low, high, sort_columns)
                _quick_sort(items, low, split_index, sort_columns)
                _quick_sort(items, split_index + 1, high, sort_columns)

        return _quick_sort(list_file, 0, len(list_file) - 1, sort_columns)


    with open(filename, encoding='utf-8') as open_file:
        filename_reader = csv.reader(open_file)
        count = 0
        for line in filename_reader:
            if count == 0:
                count += 1
                continue
            list_file.append(line)
        numline = len(open_file.readlines())
        quick_sort(list_file, sort_columns)
        if group_by_name:
            quick_sort(list_file, ["Name"])
        if order == 'asc':
            return list_file[:len(list_file)-limit-1:-1]
        return list_file[:limit]




print(select_sorted(filename='all_stocks_5yr.csv', order='desc', limit=3))

print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=3))

print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=3, group_by_name=True))

