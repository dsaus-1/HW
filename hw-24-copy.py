import csv

def get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv'):
    try:
        with open(filename, encoding='utf-8') as open_cache_file:
            for cache in open_cache_file:
                #line = line.split(';')[1]
                t = cache.split(';')[1]
                spl_1 = t.split('[')
                spl_2 = t.split(']')
                #answer = spl_2.replace('[', '')
                print(t)
                # for i in line:
                #     i = i.split(',')
                #     print(i)
                    #if i[6] == name and i[0] == date:
                      #  return i
            # for line in open_file:
            #     print(line.split(';')[1])
            #     line = line.split(';')[1]
            #     mid = 0
            #     start = 0
            #     end = len(line)
            #     step = 0
            #     while (start <= end):
            #         #print("Subarray in step {}: {}".format(step, str(array[start:end + 1])))
            #         step += 1
            #         mid = (start + end) // 2
            #
            #         if  line[mid][0] == date and line[mid][6] == name:
            #             return mid
            #
            #         if element < array[mid]:
            #             end = mid - 1
            #         else:
            #             start = mid + 1
            #     return -1
    except FileNotFoundError:
        return 'File not found'

#print(get_by_date(date='2017-08-07', name="PCLN", filename='dump.csv'))

def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    list_file = []
    def partition(list_file, low, high, sort_columns):
        '''
        расчет индекса и замена элементов при сортировке quick_sort
        '''
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = list_file[(low + high) // 2][sort_columns[0]]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while float(list_file[i][sort_columns[0]]) < float(pivot):
                i += 1
            j -= 1
            while float(list_file[j][sort_columns[0]]) > float(pivot):
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

    try:
        with open('dump.csv', encoding='utf-8') as open_cache_file:
            reader_cache_file = csv.DictReader(open_cache_file)
            for cache in reader_cache_file:
                print(cache)
                if cache['request'] == f'{sort_columns}, {limit}, {group_by_name}, {order}, {filename}':
                    return cache['answer']
        raise Exception
    except:
        with open(filename, encoding='utf-8') as open_file:
            filename_reader = csv.DictReader(open_file)
            for line in filename_reader:
                if line[sort_columns[0]] == '':
                    line[sort_columns[0]] = '0'
                list_file.append(line)
            quick_sort(list_file, sort_columns)
            # if group_by_name:
            #     quick_sort(list_file, ["Name"])
        with open('dump.csv', 'a', encoding='utf-8') as cache_file:
            fieldnames = ['request', 'answer']
            write_cache_file = csv.DictWriter(cache_file, fieldnames=fieldnames)
            if order == 'asc':
                write_cache_file.writerow({'request': sort_columns, limit, group_by_name, order, filename, 'answer': list_file[:len(list_file)-limit-1:-1]})
                return list_file[:len(list_file)-limit-1:-1]
            else:
                write_cache_file.writerow({'request': sort_columns, limit, group_by_name, order, filename, 'answer': list_file[:limit]})
                return list_file[:limit]


print(select_sorted(filename='all_stocks_5yr.csv', order='desc', limit=3))
#print(select_sorted(filename='all_stocks_5yr.csv', order='asc', limit=3))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc', limit=13))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=5))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=5, sort_columns=['close']))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=3, group_by_name=True))

