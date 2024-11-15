# Задача1.
# Создать матрицу размером 8х8 элементов,
# состоящую из нулей. Заполнить эту матрицу значениями,
# расположенными в шахматном порядке.
# Задачу решить через срезы массива NumPy

import numpy as np
import matplotlib.pyplot as plt

check = np.zeros((8, 8), dtype=int)
check[::2, 1::2] = 1  
check[1::2,::2] = 1 
print(check)
plt.imsave('check.png', check, cmap='gray')


