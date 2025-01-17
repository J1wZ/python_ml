# # Задача 3 Генерация кода
# Напишите функцию Python generate_complex_function, 
# которая принимает имя функции, список имён параметров и 
# тело функции в виде строк и возвращает динамически сгенерированную функцию.
import types

def generate_complex_function(function_name, parameters_list, body):
    """
    Функция generate_complex_function принимает имя функции function_name, 
    список имён параметров parameters_list 
    и тело функции в виде строк body
    и возвращает динамически сгенерированную функцию.
    """
    parameters = ', '.join(parameters_list)
    function_body = body.replace('\n', '\n    ')
    function_code = f"def {function_name}({parameters}):\n    {function_body}"
    namespace = {}
    exec(function_code, namespace)
    dynamic_function = types.FunctionType(namespace[function_name].__code__, locals())
    return dynamic_function

def main():
    function_name = 'complex_function'
    parameters = ['x', 'y']
    function_body = """
    if x > y:
        return x - y
    else:
        return y - x
    """

    complex_func = generate_complex_function(function_name, parameters, function_body)

    print(complex_func(10, 5)) 
    print(complex_func(5, 10)) 

if __name__ == "__main__":
    main()

# Я видела примеры где использовалось return locals()[function_name], но у меня она по какой-то причине не работала

# def generate_complex_function(function_name, parameters_list, body):
#     """
#     Функция generate_complex_function принимает имя функции function_name, 
#     список имён параметров parameters_list 
#     и тело функции в виде строк body
#     и возвращает динамически сгенерированную функцию.
#     """
#     parameters = ', '.join(parameters_list)
#     function_body = body.replace('\n', '\n    ')
#     function_code = f"def {function_name}({parameters}):\n    {function_body}"
#     exec(function_code)
#     return locals()[function_name]

