import math

class Complex:
    #Когда флаг=True функция принимает данные алгебраическом виде
    #флаг=False она переводит данные из полярного вида в алгебраический
    #принимаются радианы, а не градусы
    def __init__(self, real, imag, flag):
        if isinstance(flag,bool) and (type(real) in [int, float]) and (type(imag) in [int, float]):
            if (flag):
                self._real = real
                self._imag = imag
            else:
                self._real = real * math.cos(imag)
                self._imag = real * math.sin(imag)
        else:
            raise ValueError("Конструктор Complex(real, imag, flag) принимает только численные значения для real & imag, булевое для flag")

    #Проверяется тип другого обьекта для выбора формулы 
    def __add__(self, other):
        if isinstance(other,Complex):
            return Complex(self.real + other.real, self.imag + other.imag, True)
        elif type(other) in [int, float]:
            return Complex(self.real + other, self.imag, True)
        else:
            raise ValueError(f"Комплексные числа не складываются с {str(type(other))}")

    def __sub__(self, other):
        if isinstance(other,Complex):
            return Complex(self.real - other.real, self.imag - other.imag, True)
        elif type(other) in [int, float]:
            return Complex(self.real - other, self.imag, True)
        else:
            raise ValueError(f"Не существует разности комплексного числа и {str(type(other))}")

    def __mul__(self, other):
        if isinstance(other,Complex):
            return Complex(self.real * other.real - self.imag * other.imag,self.imag * other.real + self.real *other.imag , True)
        elif type(other) in [int, float]:
            return Complex(self.real * other, self.imag * other, True)
        else:
            raise ValueError(f"Комплексные числа не перемножаются с {str(type(other))}")


    def __truediv__(self, other):
        if isinstance(other,Complex):
            return Complex((self.real * other.real + self.imag * other.imag )/( other.real**2 + other.imag**2), (self.imag * other.real - self.real *other.imag) / ( other.real**2 + other.imag**2), True)
        elif type(other) in [int, float]:
            return Complex(self.real/other,self.imag/other,True)
        else:
            raise ValueError(f"Комплексные числа не делятся на {str(type(other))}")


    def __str__(self):
        if self.imag < 0:
            return f"{round(self.real,3)}{round(self.imag,3)}i"
        else:
            return f"{round(self.real,3)}+{round(self.imag,3)}i"
    
    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def polar(self):
        return (abs(self), math.atan2(self.imag,self.real))

    def rect(modulus, phase):
        if type(modulus) in [int, float] and type(phase) in [int, float]:
            return Complex(modulus * math.cos(phase),modulus * math.sin(phase), True)
        raise ValueError(f"Комплексные числа не создаются из пары типа ({str(type(modulus))},{str(type(phase))})")

    #Вазращает строку - данный комплексный обьект в полярной записи
    def printPolar(self):
        r, a = self.polar()
        #Преобразование для того, чтобы углы находились в диапазоне от 0 до 360 градусов(0 - 6,28 рад)
        while a < 0:
            a += 6.28
        while a >= 6.28:
            a -= 6.28
        return f"{round(r,3)}*(cos({round(a,3)})+i*sin({round(a,3)})))"

    @property
    def real(self):
        return self._real
    
    @property
    def imag(self):
        return self._imag
    

def main():
    try:
        a = Complex(1,2, True)
        print(a)
        b = Complex(3,5, False)
        print(b)
        print(a+b)
        print(a-b)
        print(a*b)
        print(a/b)
        print(abs(a))
        c,d = a.polar()
        print(Complex.rect(c,d))
        print(b.printPolar())
        print(a + 2)
        print(a-2)
        print(a*2)
        print(a/2)
        print(b.printPolar())
        a = Complex("11",88,True)
        print(a+"len")
        print(a-True)
        print(a*"1")
        print(a/"1")
        Complex.rect("qq", True)
    except ValueError as er:
        print(er)

if __name__ == "__main__":
    main()