class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ["Фантастика", "Фэнтези", "Ужасы", "Боевики", "Мистика", "Антиутопии", "Сказки", "Научная фантастика"]
        self.genre_age_rating = ["Ужасы","Боевики","Антиутопии"]

    def add_new_book(self, book_name):
        if isinstance(book_name, str):
            if book_name in self.books_genre:
                print(f"Книга с названием {book_name} уже есть в словаре.")
                return False
            else:
                self.books_genre[book_name] = ''
        else:
            print(f"Название книги может быть только строковым типом")

    def set_book_genre(self, book_name, book_genre):
        if isinstance(book_genre, str):
            if book_name in self.books_genre and book_genre in self.genre:
                self.books_genre[book_name] = book_genre
            else:
                print(f"Не найдена книга {book_name} или жанр {book_genre}")
                return False
        else:
            print(f"Жанр книги может быть только строковым типом")
        

    def get_book_genre(self, book_name):
        if isinstance(book_name, str):
            if book_name in self.books_genre:
                return self.books_genre[book_name]
            else:
                print(f"Не найдена книга {book_name}")
                return False
        else:
            print(f"Название книги может быть только строковым типом")

    def get_books_with_specific_genre(self, book_genre):
        if isinstance(book_genre, str):
            result_books = []
            if book_genre in self.genre:
                for book_name, genre in self.books_genre.items():
                    if genre == book_genre:
                        result_books.append(book_name)
                return result_books
            else:
                print(f"Не найден жанр {book_genre}")
                return False
        else:
            print(f"Жанр книги может быть только строковым типом")


    def get_books_genre(self):
        return self.books_genre


    def get_books_for_children(self):
        result_books = []
        genres_for_children = [genre for genre in self.genre if genre not in self.genre_age_rating]
        
        for book_name, book_genre in self.books_genre.items():
            if book_genre in genres_for_children:
                result_books.append(book_name)
        return result_books


    def add_book_in_favorites(self, book_name):
        if isinstance(book_name, str):
            if book_name in self.books_genre:
                if book_name not in self.favorites:
                    self.favorites.append(book_name)
                else:
                    print(f"Книга с названием {book_name} уже есть в списке любимых")
                    return False
            else:
                print(f"Книги с названием {book_name} ещё нет в словаре.")
                return False
        else:
            print(f"Название книги может быть только строковым типом")
        

    def delete_book_from_favorites(self, book_name):
        if isinstance(book_name, str):
            if book_name in self.favorites:
                self.favorites.remove(book_name)
            else:
                print(f"Книги с названием {book_name} нет в списке любимых")
                return False
        else:
            print(f"Название книги может быть только строковым типом")

    def get_list_of_favorites_books(self):
        return self.favorites