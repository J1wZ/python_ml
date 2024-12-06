# Задача 5 Функция с частичными аргументами 
# Решить следующее задание с применением библиотеки functools.
# Напишите функцию _sort_users_by_age, которая принимает список 
# пользователей (словарей) и порядок сортировки 
# (возрастание или убывание). Используя partial, 
# создайте две новые функции: одну для сортировки 
# по возрастанию возраста и другую — по убыванию.

from functools import partial

def _sort_users_by_age(users : dict, sort_order : str = 'ascending'):
    if sort_order == 'ascending':
        return dict(sorted(users.items(), key = lambda kv: kv[1]))
    elif sort_order == 'descending':
        return dict(sorted(users.items(), key = lambda kv: kv[1],reverse=True))
    else:
        raise ValueError(f'Функция не принимает sort_order = {sort_order}')
    
#Функция для сортировки по возрастанию возраста
_sort_users_by_age_ascending = partial(_sort_users_by_age, sort_order = 'ascending')

#Функция для сортировки по убыванию возраста
_sort_users_by_age_descending = partial(_sort_users_by_age, sort_order = 'descending')

users = {'Максим': 12, 'Маша': 5, 'Андрей': 54, 'Анастасия': 25}

try:
    users_ascending = _sort_users_by_age_ascending(users)

    users_descending = _sort_users_by_age_descending(users)


    print(f'Сортировка по возрастанию возраста:\n{users_ascending}\n')

    print(f'Сортировка по убыванию возраста:\n{users_descending}')
except ValueError as err:
    print(err)

try:
    users_sort = _sort_users_by_age(users, 5)
except ValueError as err:
    print(err)