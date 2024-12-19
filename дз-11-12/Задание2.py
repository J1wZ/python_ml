import zipfile
import multiprocessing


def get_paths(path_to_paths_zip: str):
    '''
    Функция get_paths находит все файлы с расширением txt в zip архиве.
    Потом она считывает содержание этих файлов(ссылку на файл в другом zip архиве).
    Функция возвращает список с путями к файлам во втором архиве 
    '''
    with zipfile.ZipFile(path_to_paths_zip, 'r') as zip_file:
        path_to_num = []
        file_info_list = zip_file.infolist()
        file_list = [file.filename for file in file_info_list if file.filename.endswith('.txt')]
        for file in file_list:
            content = zip_file.read(file).decode("utf-8").replace("\\", "/")
            path_to_num.append(content)
    return path_to_num


def get_numbers(path_to_num : str, path_to_zip : str):
    '''
    Функция get_numbers находит файлы по списку путей path_to_num в zip архиве path_to_zip.
    Она считывает из этих файлов число и прибавляет его к глобальной переменной sum_num.
    Функция возвращает номер из файла
    '''
    global sum_num
    with zipfile.ZipFile(path_to_zip, 'r') as zip_file:
        for path in path_to_num:
            number = int(zip_file.read(path).decode("utf-8"))
            with sum_num.get_lock():
                sum_num.value += number
    return number


if __name__ == "__main__":
    # sum_num - глобальный счетчик для multiprocessing
    sum_num = multiprocessing.Value('i',0)
    with multiprocessing.Pool() as pool:
        paths_to_num = get_paths('path_8_8.zip')
        arg_for_get_numbers = [(path, 'recursive_challenge_8_8.zip') for path in paths_to_num]
        result = pool.starmap(get_numbers, arg_for_get_numbers)
    print(f'Числа из файлов: {result}')
    print(f"Сумма : {sum_num.value}")