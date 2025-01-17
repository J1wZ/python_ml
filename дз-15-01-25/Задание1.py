# Задание 1
# Напишите метакласс PythonAttrLoggingMeta, 
# который регистрирует каждый доступ к атрибуту или его изменение. 
# В метаклассе должен быть переопределен метод __new__. 
# В AttrLoggingMeta добавить методы по логированию доступа 
# log_access(name,value), чтению log_read(name,value,instance) 
# и записи log_write(name,value,instance) атрибута класса.
# 
# Определите класс LoggedClass, используя AttrLoggingMeta в 
# качестве его метакласса. Проверьте правильность реализации методов.

class PythonAttrLoggingMeta(type):
    """
    В Метаклассе PythonAttrLoggingMeta есть методы по логированию доступа log_access(name,value),
    чтению log_read(name,value,instance) и записи log_write(name,value,instance)
    атрибута класса.
    """
    
    def __new__(mcs, name, bases, attrs, **extra_kwargs):
        for attr_key, attr_value in attrs.items():
            #Чтобы логировались только ни приватные ни специальные атрибуты и методы
            if not attr_key.startswith('__'):
                attrs[attr_key] = mcs.log_access(attr_key, attr_value)
        return super().__new__(mcs, name, bases, attrs)  

    def __init__(cls, name, bases, attrs, **extra_kwargs):  
        super().__init__(cls)  

    @classmethod  
    def __prepare__(mcs, cls, bases, **extra_kwargs):  
        return super().__prepare__(mcs, cls, bases, **extra_kwargs)  

    def __call__(cls, *args, **kwargs):  
        return super().__call__(*args, **kwargs)
    
    @staticmethod
    def log_access(name, value):
        """
        Метод по логированию доступа к методам и атрибутам
        """

        if callable(value):
            return PythonAttrLoggingMeta.log_method(name, value)
        else:
            #Определяется геттер и сеттер для атрибута
            return property(
                fget=lambda self: PythonAttrLoggingMeta.log_read(name, value, self),
                fset=lambda self, new_value: PythonAttrLoggingMeta.log_write(name, new_value, self)
            )
    
    @staticmethod
    def log_method(name, value):
        def wrapper(*args, **kwargs):
                print(f"Calling method {name}")
                return value(*args, **kwargs)
        return wrapper


    @staticmethod
    def log_read(name, value, instance):
        print(f"Reading attribute {name}")
        return value
    
    @staticmethod
    def log_write(name, value, instance):
        print(f"Writing attribute {name} with value {value}")
        instance.__dict__[name] = value

class LoggedClass(metaclass=PythonAttrLoggingMeta):
    """
    Класс LoggedClass основан на метаклассе PythonAttrLoggingMeta. \n
    Он добавляет атрибут custom_method и метод other_custom_method.
    """

    custom_method = 42

    def other_custom_method(self):
        pass

def main():
    instance = LoggedClass()
    print(instance.custom_method)  
    instance.custom_method = 78    
    instance.other_custom_method()

if __name__ == "__main__":
    main()
