# Создать класс Movie. 
# У Movie есть название и расписание, 
# по каким дням он идёт в кинотеатрах. 
# Название Movie - это текст. Расписание хранится периодами дат.
# Например, прокат фильма проходит с 1 по 7 января, 
# а потом показ возобновляется с 15 января по 7 февраля:

# [(datetime(2024,11,1),datetime(2024,11,7)),
# (datetime(2024,12,15),datetime(2024,12,31))]

# Реализуйте у класса Movie метод schedule. 
# Он будет генерировать дни, в которые показывают фильм. 
# Проверить работу генератора.

from datetime import date, timedelta, datetime
import random

class Movie():

    #num_days определяет максимальное количество дней после которых начнется показ фильма
    def __init__(self, name='', num_days = 20):
        self._name = str(name)
        if isinstance(num_days, int):
            self._schedule = self.chooseRandomDates(num_days)
        else:
            raise TypeError(f"Канструктор Movie не принимает в num_days обьекты {type(num_days)}")

    #chooseRandomDates возвращает лист из двух рандомных начал и концов показа фильма
    #date_range определяет максимальное количество дней после которых начнется показ фильма
    def chooseRandomDates(self, date_range):
        start = date.today()
        res = []
        #rand_day - кол-во дней от start до начала показа фильма
        #sessions -  кол-во дней(сеансов) до конца показа 
        rand_day = 0
        sessions = 0
        for _ in range(2):
            random.seed(a=None)
            rand_day = random.randrange(rand_day+sessions,rand_day+sessions+date_range)
            sessions = random.randrange(1, date_range//2)
            t = (start + timedelta(rand_day), start + timedelta(rand_day) + timedelta(sessions))
            res.append(t)
        return res


    def schedule(self):
        dates = self._schedule
        for date in dates:
            start_date = date[0]
            end_date = date[1]
            days = int((end_date - start_date).days)
            for i in range(days):
                yield start_date + timedelta(i)

    def show_schedule(self):
        res = ''
        for el in self.schedule():
            res += f'{datetime.strftime(el,"%Y-%m-%d %H:%M:%S")}\r\n'
        return res
    

def main():
    a = Movie('Русалочка',30)
    print(a.show_schedule())
    try:
        a = Movie(23, "qqqq")
    except TypeError as er:
        print(er)

if __name__ == "__main__":
    main()