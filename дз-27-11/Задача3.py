# Задайте функцию-генератор,которая на основе символов строки chars:
# from string import ascii_lowercase, ascii_uppercase
# chars=ascii_lowercase+ascii_uppercase+"0123456789!?@#$*"
# формирует и выдает случайно сгенерированные пароли длиной 12 символов.
# Количество выдаваемых паролей функцией должно быть неограниченным. 
# Случайный выбор символа из последовательности chars 
# можно реализовать с помощью функции choice модуля random. 
# Выведите первые пять сгенерированных паролей на экран

from string import ascii_lowercase, ascii_uppercase
from random import choice

chars=ascii_lowercase+ascii_uppercase+"0123456789!?@#$*"

def generatePass(chars):
    password = ''.join(choice(chars) for _ in range(12))
    yield password

i = 0
while i < 5:
    print(next(generatePass(chars)))
    i+=1