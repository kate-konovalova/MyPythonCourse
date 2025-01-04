books = [
    {
        "id": 1,
        "name": "Сборник Стихов",
        "pages": 510,
    },
    {
        "id": 2,
        "name": "Энциклопедия",
        "pages": 600,
    }
]    # для проверки кода 


class Book:

    def __init__(self, id, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):    # __str___ метод для строкового представления экземпляра класса
        return f'Книга "{self.name}"'

    def __repr__(self):    # __repr__ метод для строкого представления экземпляра класса
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:

    def __init__(self, books=None):  # пустой лист для книг
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):    # ID += 1
        if len(self.books) == 0:    # если сейчас книг нет, то у следующей будет 1
            return 1
        else:    # в ином случае добавляем +1
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id):
        for index, book in enumerate(self.books):
            if book.id == id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':

    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in books
    ]
    for book in list_books:
        print(book)  # печать-проверка метода __str__ для каждой книги

    print(list_books)  # печать-проверка метода __repr__

    empty_library = Library()  # создаем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки (=1)

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in books
    ]
    library_with_books = Library(books=list_books)  # создаем библиотеку с книгами (2 шт)
    print(library_with_books.get_next_book_id())  # проверяем следующий id для библиотеки с двумя кингами (=3)

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1