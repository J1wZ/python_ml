# # Задание 3
# 
# Реализуйте контекстный менеджер safe_write, который принимает один аргумент : filename — имя файла 
# 
# Контекстный менеджер должен позволять записывать информацию в файл с именем filename. Причем если вовремя записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:
# 
#     Вовремя записи в файл было возбуждено исключение <тип исключения> 
# 
# Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.


class safe_write:
    """
    Контекстный менеджер safe_write позволяет записывать информацию в файл с именем filename.\n
    Причеме если во время записи в файл было возбуждено какое-либо исключение,
    контекстный менеджер поглотит его, отменит все выполненные ранее записи в файл, 
    если они были,вернет файл в исходное состояние.
    """
    def __init__(self, filename):
        self.path = filename
        with open(self.path, mode='r') as file:
            self.initial_text = file.read()

    def __enter__(self):
        self.file = open(self.path, mode='w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            if exc_type is not None:
                print(f"Во время записи в файл было возбуждено исключение {exc_type.__name__}")
                with open(self.path, mode='w') as file:
                    file.write(self.initial_text)
                return True
            self.file.close()
            
#обычная запись
with safe_write('undertale.txt') as file:
    file.write('Я знаю,что ничего не знаю, но другие не знают и этого.')

with open('undertale.txt') as file:
    print(file.read())

#вызов исключения
with safe_write('under_tale.txt') as file:
    file.write('Я знаю,что ничего не знаю, но другие не знают и этого.\n')

with safe_write('under_tale.txt') as file:
    print('Если ты будешь любознательным, то будешь многознающим.',file=file,flush=True)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())