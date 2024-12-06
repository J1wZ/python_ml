# Задача 3 Перестановки строк 
# Решить следующее задание с применением библиотеки itertools. 
# Написать функцию, принимающую строку s и число n и 
# возвращающую все возможные перестановки из n символов 
# в s строке в лексикографическом порядке 
# (использовать itertools.permutations)

from itertools import permutations

def get_permutations(s : str, n : int):
    return sorted(list(permutations(s,n)))

string = 'Hello_World!'
num = 3
result = get_permutations(string, num)
for el in result:
    print(el)