# # Задача 2 Динамическое создание класса 
# Напишите функцию Python create_class_with_methods, 
# которая принимает имя класса, словарь атрибутов и словарь методов и 
# возвращает динамически созданный класс с этими атрибутами и методами. 
# Для создания класса использовать метод type.

def create_class_with_methods(class_name : str, attr_dict : dict, method_dict : dict):
    """
    Функция create_class_with_methods создает динамически созданный класс с 
    данными атрибутами и методами. \n
    class_name - имя класса \n
    attr_dict - словарь атрибутов \n
    method_dict - словарь методов
    """

    return type(class_name, (object,), attr_dict | method_dict)


def main():
    attributes= {'species':'Human','age':25}
    methods={'greet':lambda self:f"Hello, I am a {self.species} and I am {self.age} years old."}
    DynamicClass=create_class_with_methods('DynamicClass',attributes,methods)
    instance=DynamicClass()
    print(instance.greet())

if __name__ == "__main__":
    main()
