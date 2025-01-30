import pytest
from BooksCollectorClass import BooksCollector

#Название и жанр книги для подставление в тесты
new_book_name = "Новая книга"
new_book_genre = "Ужасы"


def test_add_new_book_passed():
    '''
        Тест проверяет метод add_new_book на успешное добавление названия книги в словарь \n
        В словаре должно находится данное название книги с пустым жанром {new_book_name : ''}
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    assert collector.get_books_genre() == {new_book_name : ''}


def test_add_new_book_add_same_book():
    '''
        Тест проверяет метод add_new_book на добавление в словарь двух одинаковых книг \n
        Словарь не должен содержать копии, {new_book_name:''}
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.add_new_book(new_book_name)
    assert collector.get_books_genre() == {new_book_name:''}

@pytest.mark.parametrize('book_name', [
    (11),
    (False)
])
def test_add_new_book_invalid_name_type(book_name):
    '''
        Тест проверяет метод add_new_book на проверку типа введенного имени книги \n
        Название книги может быть только строковым(str), словарь должен быть пустым
    '''
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert collector.get_books_genre() == {}


def test_set_book_genre_passed():
    '''
        Тест проверяет метод set_book_genre на успешное добавление жанра книги \n
        Метод должен присвоить правильный жанр данной книги
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    assert collector.get_book_genre(new_book_name) == new_book_genre


@pytest.mark.parametrize('book_name, book_genre', [
    (new_book_name, "Invalid"),
    ("Invalid", "Ужасы")
])
def test_set_book_genre_invalid_genre_or_name(book_name, book_genre):
    '''
        Тест проверяет метод set_book_genre на проверку того, что данное название книги есть в словаре,
        а жанр в списке допутимых жанров. \n
        В словаре должно находится данное название книги с пустым жанром {new_book_name : ''}
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(book_name,book_genre)
    assert collector.get_books_genre() == {new_book_name: ''}


@pytest.mark.parametrize('book_genre', [
    (11),
    (False)
])
def test_set_book_genre_invalid_genre_type(book_genre):
    '''
        Тест проверяет метод set_book_genre на защиту от ввода значений отличных от строкового(str)\n
        Жанр книги может быть только строковым(str) \n
        В словаре должно находится данное название книги с пустым жанром {new_book_name : ''}
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,book_genre)
    assert collector.get_books_genre() == {new_book_name: ''}


def test_get_book_genre_passed():
    '''
        Тест проверяет метод get_book_genre на успешное извлечение жанра книги \n
        Метод должен возвращать правильный жанр данной книги new_book_genre
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    assert collector.get_book_genre(new_book_name) == new_book_genre

def test_get_book_genre_no_book():
    '''
        Тест проверяет поведение метода get_book_genre в случае запроса книги, которой нет в словаре\n
        Метод должен вернуть False
    '''
    collector = BooksCollector()
    assert collector.get_book_genre(new_book_name) == False

@pytest.mark.parametrize('invalid_book_name', [
    (11),
    (False)
])
def test_get_book_genre_invalid_name_type(invalid_book_name):
    '''
        Тест проверяет поведение метода get_book_genre в случае запроса книги с названием не строчного типа(str)\n
        Метод не должен ничего вернуть
    '''
    collector = BooksCollector()
    assert collector.get_book_genre(invalid_book_name) == None


def test_get_books_with_specific_genre_passed():
    '''
        Тест проверяет метод get_books_with_specific_genre на правильный подбор книг определенного жанра\n
        Метод должен вернуть список названия книг данного жанра new_book_genre
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_new_book("Другая книга")
    collector.set_book_genre("Другая книга",new_book_genre)
    collector.add_new_book("Ещё книга")
    collector.set_book_genre("Ещё книга","Сказки")
    assert collector.get_books_with_specific_genre(new_book_genre) == [new_book_name, "Другая книга"]


def test_get_books_with_specific_genre_invalid_genre():
    '''
        Тест проверяет метод get_books_with_specific_genre на проверку того,
        что данный жанр находится в списке допустимых \n
        Метод должен вернуть False
    '''
    collector = BooksCollector()
    assert collector.get_books_with_specific_genre("Invalid") == False

@pytest.mark.parametrize('book_genre', [
    (11),
    (False)
])
def test_get_books_with_specific_genre_invalid_genre_type(book_genre):
    '''
        Тест проверяет метод get_books_with_specific_genre на защиту от обработки жанров не строчного типа\n
        Метод не должен ничего возвращать в этом случае
    '''
    collector = BooksCollector()
    assert collector.get_books_with_specific_genre(book_genre) == None

def test_get_books_genre_passed():
    '''
        Тест проверяет метод get_books_genre на успешное возрвращение словаря с книгами и их жанрами\n
        Метод сначала должен вернуть пустой словарь, а потом заполненный {new_book_name:new_book_genre}
    '''
    collector = BooksCollector()
    assert collector.get_books_genre() == {}
    expected_book_genre = {new_book_name:new_book_genre}
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    assert collector.get_books_genre() == expected_book_genre


@pytest.mark.parametrize('book_genre, expected_book_genre', [
    ("Сказки", [new_book_name]),
    ("Ужасы", [])
])
def test_get_books_for_children_passed(book_genre, expected_book_genre):
    '''
        Тест проверяет метод get_books_for_children на успешное возрвращение списка книг, которые подходят детям\n
        Метод должен возвращать список со всеми книгами подходящими для детей
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,book_genre)
    assert collector.get_books_for_children() == expected_book_genre

def test_add_book_in_favorites_passed():
    '''
        Тест проверяет метод add_book_in_favorites на успешное добавление книги в список избранных\n
        Метод должен добавить данное название книги new_book_name в список избранных
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_book_in_favorites(new_book_name)
    assert collector.get_list_of_favorites_books() == [new_book_name]

def test_add_book_in_favorites_add_same_book():
    '''
        Тест проверяет поведение метода add_book_in_favorites в случае повторного добавления книги в список избранных \n
        В списке избранных не должно быть дубликатов, [new_book_name]
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_book_in_favorites(new_book_name)
    collector.add_book_in_favorites(new_book_name)
    assert collector.get_list_of_favorites_books() == [new_book_name]

def test_add_book_in_favorites_invalid_name():
    '''
        Тест проверяет поведение метода add_book_in_favorites в случае попытки 
        добавления несуществующей книги в список избранных\n
        Список избранных должен быть пустым
    '''
    collector = BooksCollector()
    collector.add_book_in_favorites(new_book_name)
    assert collector.get_list_of_favorites_books() == []

@pytest.mark.parametrize('invalid_book_name', [
    (11),
    (False)
])
def test_add_book_in_favorites_invalid_name_type(invalid_book_name):
    '''
        Тест проверяет поведение метода add_book_in_favorites, когда тип данного названия книги не является строчным\n
        Список избранных должен быть пустым
    '''
    collector = BooksCollector()
    collector.add_book_in_favorites(invalid_book_name)
    assert collector.get_list_of_favorites_books() == []

def test_delete_book_from_favorites_passed():
    '''
        Тест проверяет метод delete_book_from_favorites на успешное удаление книги из списка избранных\n
        Список избранных должен быть пустым
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_book_in_favorites(new_book_name)
    collector.delete_book_from_favorites(new_book_name)
    assert collector.get_list_of_favorites_books() == []

def test_delete_book_from_favorites_invalid_name():
    '''
        Тест проверяет метод delete_book_from_favorites на попытку удаления книги, которой нет в списке избранных\n
        Список избранных не должен измениться
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_book_in_favorites(new_book_name)
    collector.delete_book_from_favorites("Не та книга")
    assert collector.get_list_of_favorites_books() == [new_book_name]    

@pytest.mark.parametrize('invalid_book_name', [
    (11),
    (False)
])
def test_delete_book_from_favorites_invalid_name_type(invalid_book_name):
    '''
        Тест проверяет метод delete_book_from_favorites на попытку удаления названия книги не строчного типа\n
        Список избранных не должен измениться
    '''
    collector = BooksCollector()
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_book_in_favorites(new_book_name)
    collector.delete_book_from_favorites(invalid_book_name)
    assert collector.get_list_of_favorites_books() == [new_book_name]


def test_get_list_of_favorites_books():
    '''
        Тест проверяет метод get_list_of_favorites на успешное возвращение списка избранных книг\n
        Метод сначала должен вернуть пустой список, а потом заполненный [new_book_name]
    '''
    collector = BooksCollector()
    assert collector.get_list_of_favorites_books() == []
    collector.add_new_book(new_book_name)
    collector.set_book_genre(new_book_name,new_book_genre)
    collector.add_book_in_favorites(new_book_name)
    assert collector.get_list_of_favorites_books() == [new_book_name]




