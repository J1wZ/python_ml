# Написать класс CyclicIterator. 
# Итератор должен итерировать по итерируемому объекту 
# (например, по range, list, tuple, set и т.д.),
# и когда достигнет последнего элемента, начинать с начала. 
# Проверить работу итератора

class CyclicIterator():

    def __init__(self, list=[]):
        self._list = list


    @property
    def list(self):
        return self._list


    def cycle(self):
        list = self.list
        saved = []
        for element in list:
            yield element
            saved.append(element)

        while saved:
            for element in saved:
                yield element

def main():
    my_list = [1, 2, 3 , 4]
    iter = CyclicIterator(my_list).cycle()
    i = 0
    while i < len(my_list)+5:
        print(next(iter))
        i +=1

if __name__ == "__main__":
    main()
    

