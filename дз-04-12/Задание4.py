# Задача 4 Комбинации символов 
# Решить следующее задание сприменением библиотеки itertools.
# Реализовать функцию get_combinations. 
# Должна принимать строку s и число k и возвращать 
# все возможные комбинации из символов в строке s 
# с длинами <= k (использовать itertools.combinations)

from itertools import combinations

def get_combinations(s : str, k : int):
    result = []
    for i in range(k+1):
        result += list(combinations(s, i))
    return result

string = 'Hello_World!'
#максимальное кол-во комбинаций 
max_num = 3
result = get_combinations(string, max_num)
for el in result:
    print(el)