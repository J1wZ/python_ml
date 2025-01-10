# # Задание 2
# 
# В этом задании вам придётся реализовать декоратор, который будет принимать несколько аргументов. Так, нужно написать декоратор cache( db : str ),который принимает в качестве параметра db-название базы данных, где будет кэшироваться информация. Затем подумайте, как можно передать второй параметр- expiration, количество раз, когда данные будут браться из кэша, а затем будут стёрты.
# 
# Исходные условия:
# 
#     ●Определена функция get_info(thing:str)->str, которая возвращает информацию о предмете thing.
# 
# Порядок выполнения:
# 
#     ●Напишите декоратор, который будет принимать название базы данных и количество раз, когда данные будут браться из кэша. После того, как количество станет равным нулю кэш необходимо обновить актуальными данными (см.примеры)

import functools

def cache(bd : str, expiration = 5):
    """
    Кэширует данные из func в базе данный bd. 
    expiration - кол-во раз, когда можно брать данные из кэша,
    после чего они будут стерты 
    """
    def decorator_cache(func):
        @functools.wraps(func)
        def wrapper_cache(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache.cache:
                wrapper_cache.cache[cache_key] = [func(*args, **kwargs), expiration]
                print(f"Info about: {args[0]} from {bd}, now cached with expire = {expiration}")
                return wrapper_cache.cache[cache_key][0]
            wrapper_cache.cache[cache_key][1] -=1
            print(f"Info about: {args[0]} cached in {bd}, expire = {wrapper_cache.cache[cache_key][1]}")
            if wrapper_cache.cache[cache_key][1] == 0:
                final_cache = wrapper_cache.cache[cache_key][0]
                del wrapper_cache.cache[cache_key]
                return final_cache
            return wrapper_cache.cache[cache_key][0]  
        # в wrapper_cache.cache будет храниться наш кэш
        wrapper_cache.cache = dict()
        return wrapper_cache
    return decorator_cache

def get_info(thing):
    return f"{thing} Info: {type(thing)}, {len(thing)}"


for i in range(2):
    print(get_info("Fish"))

@cache("PostgreSql")
def info1(thing):
    return get_info(thing)

@cache("MySQL", 2)
def info2(thing):
    return get_info(thing)

for i in range(3):
    print(info1("Bike"))

for i in range(2):
    info1("Toys")
for i in range(3):
    info1("Chairs")
for i in range(4):
    info2("user")

# для user уже есть кэш с прошлого range, поэтому expire = 1
for i in range(5):
    info2("user")

for i in range(7):
    info2("new user")