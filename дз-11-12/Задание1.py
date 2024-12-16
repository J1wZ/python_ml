import time
from concurrent.futures import ThreadPoolExecutor, as_completed


'''
 Функция process_number возвращеет переданное ей число number умноженное на 2, 
 с имитацией задержки 0.2 сек на каждой операции
'''
def process_number(number):
    time.sleep(0.2)
    return number * 2


'''
Функция list_processing принимает список списков data и максимальное количество 
рабочих потоков num_threads

Она возвращает сумму обработанных чисел списка который 
был обработан быстрее остальных и время его обработки
'''
def list_processing(data, num_threads=10):
    min_process_time = float('inf')
    first_list_sum = 0
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        start = time.time()
        for data_list in data:
            futures = [executor.submit(process_number, elm) for elm in data_list] 
            
        if (time.time() - start) < min_process_time:
            min_process_time = time.time() - start
            first_list_sum = sum(future.result() for future in as_completed(futures))
                
    return {'min_process_time' : min_process_time, 'first_list_sum' : first_list_sum}

if __name__ == "__main__":
    with open("test_list_numbers.txt", "r") as file:
        test_list_numbers = eval("".join([line.strip() for line in file.readlines()]))

    results = list_processing(test_list_numbers)
    print(f"Results: {results}")
    print(f"Сумма чисел в первом обработанном списке: {results['first_list_sum']}")