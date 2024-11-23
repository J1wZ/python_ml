import math

class Complex:
    #Когда флаг=True функция принимает данные алгебраическом виде
    #флаг=False она переводит данные из полярного вида в алгебраический
    #принимаются радианы, а не градусы
    def __init__(self, real, imag, flag):
        if (flag):
            self._real = real
            self._imag = imag
        else:
            self._real = real * math.cos(imag)
            self._imag = real * math.sin(imag)

    #Проверяется тип другого обьекта для выбора формулы 
    def __add__(self, other):
        if isinstance(other,Complex):
            return Complex(self._real + other._real, self._imag + other._imag, True)
        else:
            return Complex(self._real + other, self._imag, True)

    def __sub__(self, other):
        if isinstance(other,Complex):
            return Complex(self._real - other._real, self._imag - other._imag, True)
        else:
            return Complex(self._real - other, self._imag, True)

    def __mul__(self, other):
        if isinstance(other,Complex):
            return Complex(self._real * other._real - self._imag * other._imag,self._imag * other._real + self._real *other._imag , True)
        else:
            return Complex(self._real * other, self._imag * other, True) 

    def __truediv__(self, other):
        if isinstance(other,Complex):
            return Complex((self._real * other._real + self._imag * other._imag )/( other._real**2 + other._imag**2), (self._imag * other._real - self._real *other._imag) / ( other._real**2 + other._imag**2), True)
        else:
            return Complex(self._real/other,self._imag/other,True)

    def __str__(self):
        if self.imag < 0:
            return f"{round(self.real,3)}{round(self.imag,3)}i"
        else:
            return f"{round(self.real,3)}+{round(self.imag,3)}i"
    
    def __abs__(self):
        return math.sqrt(self._real**2 + self._imag**2)

    def polar(self):
        return (abs(self), math.atan2(self.imag,self.real))

    def rect(modulus, phase):
        return Complex(modulus * math.cos(phase),modulus * math.sin(phase), True)

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

if __name__ == "__main__":
    main()