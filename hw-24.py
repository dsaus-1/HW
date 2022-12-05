import csv
import os

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
    def partition(lst, low, high, sort_columns):
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


    def quick_sort(lst, sort_columns):
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
        return _quick_sort(lst, 0, len(list_file) - 1, sort_columns)


    try:
        with open('dump.csv', 'r', encoding='utf-8', newline='') as open_cache_file:
            reader_cache_file = csv.DictReader(open_cache_file)
            for cache in reader_cache_file:
                if cache['request'] == str([sort_columns, limit, group_by_name, order, filename]):
                    return cache['answer']
        raise Exception
    except:
        with open(filename, encoding='utf-8', newline='') as open_file:
            filename_reader = csv.DictReader(open_file)
            count = 0
            for line in filename_reader:
                if line[sort_columns[0]] == '':
                    line[sort_columns[0]] = '0'
                list_file.append(line)
            if group_by_name:

                '''
                Если присутствует фильтрация по нейму, то фильтруем весь файл по нейму и создаем файлы содержащие один нейм, 
                после чего проходимся по каждому файлу, фильтруем его по выбранному параметру и соединяем файлы
                '''
                list_name_middle_file = []
                list_for_middle_file = []
                for l in range(len(list_file)):
                    if list_for_middle_file == []:
                        list_for_middle_file.append(list_file[l])
                        continue
                    if l == len(list_file) -1 and list_file[l]["Name"] == list_file[l-1]["Name"]:
                        list_for_middle_file.append(list_file[l])
                        break
                    if list_file[l]["Name"] == list_file[l+1]["Name"]:
                        list_for_middle_file.append(list_file[l])
                        continue
                    else:
                        list_for_middle_file.append(list_file[l])
                        name_middle_file = list_file[l]["Name"] + '.csv'
                        if list_file[l]["Name"] == '':
                            name_middle_file = '1_.csv'
                        list_name_middle_file.append(name_middle_file)
                        with open(name_middle_file, 'w', encoding='utf-8', newline='') as middle_file:
                            fieldnames_middle_file = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
                            write_middle_file = csv.DictWriter(middle_file, fieldnames=fieldnames_middle_file)
                            write_middle_file.writeheader()
                            for name_line in list_for_middle_file:
                                write_middle_file.writerow(name_line)
                            list_for_middle_file = []
                list_file = []
                if order == 'asc':
                    final_list = []
                    ind = -1
                    while True:
                        name = list_name_middle_file[ind]
                        with open(name, 'r', encoding='utf-8') as middle_file_r:
                            read_middle_file_r = csv.DictReader(middle_file_r)
                            for line_ in read_middle_file_r:
                                list_file.append(line_)
                            quick_sort(list_file, sort_columns)
                            list_file = list_file[::-1]
                            final_list += list_file
                            list_file = []
                            if len(final_list) < limit:    #если длинна конечного списка меньше лимита, открываем следующий файл и
                                ind -= 1
                            else:   #если длинна больше или равна лимиту, то выходим из цикла
                                break
                    with open('dump.csv', 'a', encoding='utf-8', newline="") as cache_file:
                        fieldnames = ['request', 'answer']
                        write_cache_file = csv.DictWriter(cache_file, fieldnames=fieldnames)
                        size = os.path.getsize('dump.csv')
                        if size == 0:
                            write_cache_file.writeheader()
                        answer = []
                        for i in range(limit):
                            answer.append(list(final_list[i].values()))
                        write_cache_file.writerow({'request': [sort_columns, limit, group_by_name, order, filename], 'answer': answer})
                        return answer
                else:
                    final_list = []
                    ind = 0
                    while True:
                        name = list_name_middle_file[ind]
                        with open(name, 'r', encoding='utf-8') as middle_file_r:
                            read_middle_file_r = csv.DictReader(middle_file_r)
                            for line_ in read_middle_file_r:
                                list_file.append(line_)
                            quick_sort(list_file, sort_columns)
                            final_list += list_file
                            list_file = []
                            if len(final_list) < limit:  # если длинна конечного списка меньше лимита, открываем следующий файл и
                                ind += 1
                            else:  # если длинна больше или равна лимиту, то выходим из цикла
                                break
                    with open('dump.csv', 'a', encoding='utf-8', newline="") as cache_file:
                        fieldnames = ['request', 'answer']
                        write_cache_file = csv.DictWriter(cache_file, fieldnames=fieldnames)
                        size = os.path.getsize('dump.csv')
                        if size == 0:
                            write_cache_file.writeheader()
                        answer = []
                        for i in range(limit):
                            answer.append(list(final_list[i].values()))
                        write_cache_file.writerow(
                            {'request': [sort_columns, limit, group_by_name, order, filename], 'answer': answer})
                        return answer
            '''
            сортировка без нейма
            '''
            count = 0





#print(select_sorted(filename='all_stocks_5yr.csv', order='desc', limit=3))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc', limit=13))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=5))
# print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=5, sort_columns=['close']))
#print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=3, group_by_name=True))
#print(select_sorted(filename='all_stocks_5yr.csv', order='asc',limit=3))

