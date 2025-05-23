from BooksCollectorClass import BooksCollector

#Пример использования класса 
collector = BooksCollector()

#Добавление книг 
collector.add_new_book('Властелин колец')
collector.add_new_book('Гарри Поттер')
collector.add_new_book('Матрица')
collector.add_new_book('Звонок')

#Установка жанров 
collector.set_book_genre('Властелин колец','Фантастика')
collector.set_book_genre('Гарри Поттер','Фэнтези')
collector.set_book_genre('Матрица','Научная фантастика')
collector.set_book_genre('Звонок','Ужасы')

#Получение жанров 
print(collector.get_book_genre('Властелин колец'))#Фантастика
print(collector.get_book_genre('Гарри Поттер'))#Фэнтези
print(collector.get_book_genre('Матрица'))#Научная фантастика

#Получение книг определенного жанра
fantasy_books=collector.get_books_with_specific_genre('Фантастика')
print(f'Книги в жанре Фантастики:{fantasy_books}')

#Получение всех книг жанра 
all_books=collector.get_books_genre()
print('Все книги и их жанры:',all_books)

#Получение книг для детей
children_books=collector.get_books_for_children()
print('Книги для детей:',children_books)

#Добавление в избранное
collector.add_book_in_favorites('Властелин колец')
collector.add_book_in_favorites('Гарри Поттер')

#Удаление из избранного
collector.delete_book_from_favorites('Гарри Поттер')

#Получение списка избранных 
favorites_list=collector.get_list_of_favorites_books()
print('Список избранных книг:',favorites_list)