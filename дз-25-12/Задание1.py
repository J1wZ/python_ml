# Задача 1 Права администратора

import functools

user_role = ""

def role_required(role:str):
    """
    Функция проверяет есть ли у роли доступ
    """
    def check_role(func):
        @functools.wraps(func)
        def wrapper():
            if role == user_role:
                return func()
            else:
                return f"Permission denied"
        return wrapper
    return check_role
            
@role_required("admin")
def secret_resource():
    #Какой-то код
    return f"Permission accepted"

user_role = input("Введите роль:")
print(f"user_role = {user_role}")
print(secret_resource())

users = ["manager", "anon", "admin", "someone"]
for u in users:
    user_role = u
    print(secret_resource())

