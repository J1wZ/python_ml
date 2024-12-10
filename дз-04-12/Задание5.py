# Задача 5 Функция с частичными аргументами 
# Решить следующее задание с применением библиотеки functools.
# Напишите функцию _sort_users_by_age, которая принимает список 
# пользователей (словарей) и порядок сортировки 
# (возрастание или убывание). Используя partial, 
# создайте две новые функции: одну для сортировки 
# по возрастанию возраста и другую — по убыванию.

from functools import partial

'''
Функция _sort_users_by_age принимает список пользователей и sort_order - порядок сортировки
sort_order == False - сортирует по возрастанию, True - по убыванию
'''
def _sort_users_by_age(users, sort_order : bool = False):
    if isinstance(sort_order, bool):
        return sorted(users, key = lambda user: user['age'],reverse=sort_order)
    else:
        raise ValueError(f'Функция не принимает sort_order типа {type(sort_order)}')
    
#Функция для сортировки по возрастанию возраста
_sort_users_by_age_ascending = partial(_sort_users_by_age)

#Функция для сортировки по убыванию возраста
_sort_users_by_age_descending = partial(_sort_users_by_age, sort_order = True)

users = [
    {'name':'Максим','age': 12},
    { 'name':'Маша','age': 5},
    {'name':'Андрей','age': 54}, 
      ]

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