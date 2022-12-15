import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        file_open = open(file, mode='rb')
    except  FileNotFoundError:
        #print(f'FileNotFoundError: [Errno 2] No such file or directory: {file}') # если нужен вывод без выброса ошибки, то можно реализовать через принт
        raise FileNotFoundError(f'[Errno 2] No such file or directory: {file}')
    else:
        print(file_open.read())
        file_open.close()
    finally:
        stpo_time = time.time()
        print(f'Time required for {file} = {stpo_time - start_time}')


video_data = read_file_timed('file_not_exist.mp4')
