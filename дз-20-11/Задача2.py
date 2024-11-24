import math
class Vector:
    #Конструктор Vector принимает только: 0 переменных, массив или одно число
    #Если контруктору не было передана переменная он возращает пустой список
    def __init__(self,items = []):
        if (isinstance(items,list) and Vector.CheckVectorItems(items)):
            self._items = items
        elif type(items) in [int, float]:
            self._items = [items]
        else:
            raise ValueError(f"Для инициализации вектора не принимаются {str(type(items))}")

    #Функция проверяет, что все элементы в списке только типа int или float
    def CheckVectorItems(items):
        if items != []:
            for el in items:
                if type(el) not in [int,float]:
                    raise ValueError(f"Вектор может состоять только из чисел. Он не должен содержать {str(type(el))}")
        return True
        
    
    def __add__(self, other):
        if isinstance(other,Vector):
            if self.size != other.size:
                raise ValueError("Векторы разной размерности не складываются")
            return Vector([self.items[i]+other.items[i] for i in range(self.size)])
        raise ValueError(f"Только вектора складываются с друг другом")


    def __sub__(self, other):
        if isinstance(other,Vector):
            if self.size != other.size:
                raise ValueError("Нет разности векторов разной размерности")
            return Vector([self.items[i]-other.items[i] for i in range(self.size)])
        raise ValueError("Только вектора вычитаются из друг друга")

    #Возвращает скалярное умножение векторов или результат умножения вектора на число
    def __mul__(self, other):
        if isinstance(other,Vector):
            return sum([self.items[i]*other.items[i] for i in range(self.size)])
        elif not (type(other) in [int, float]):
            raise ValueError(f"Векторы не могут перемножатся с {str(type(other))}")
        return Vector([self.items[i]*other for i in range(self.size)])

    def cos(self, other):
        if isinstance(other,Vector):
            return (self * other)/(abs(self)*abs(other))
        raise ValueError(f"Косинус не может считаться между вектором и {str(type(other))}")


    def __str__(self):
        return str(self.items)
    
    #Возвращает Евклидову норму
    def __abs__(self):
        return math.sqrt(sum([self.items[i]**2 for i in range(self.size)]))

    #Добавляет к вектору новые элементы из списка или другого вектора
    #Составлен на основе extend списка
    def extend(self, items):
        if (isinstance(items,list) and Vector.CheckVectorItems(items)):
            self._items.extend(items)
        elif isinstance(items, Vector):
            self._items.extend(items._items)
        else:
            raise ValueError(f"Вектор не может быть увеличен(extend) обьектом {str(type(items))}")
    
    #Добавляет к вектору новую координату
    #Составлен на основе append списка
    def append(self,item):
        if type(item) in [int, float]:
            self._items.append(item)
        else:
            raise ValueError(f"К вектору не может быть добавлен {str(type(item))}")
        
    # Возращает длину списка(размерность вектора)
    def __len__(self):
        return self.size

    @property
    def items(self):
        return self._items
    
    @property
    def size(self):
        return len(self.items)
    

def main():
    try:
        a = Vector()
        print(a)
        b = Vector([3,5])
        print(b)
        c = Vector(1)
        print(c)
        a.extend([3,4,5])
        b.append(8)
        print(a)
        print(b)
        print("---------")
        print(a+b)
        print(a-b)
        print(a*b)
        print(a*2)
        print(abs(a))
        print(Vector.cos(a,b))
        print(a*"s")
        print(a-2)
        d = Vector([1,2,"q",1])
        print(a-2)
        a.append("qq")
        a.extend("qq")
    except ValueError as er:
        print(er)

if __name__ == "__main__":
    main()