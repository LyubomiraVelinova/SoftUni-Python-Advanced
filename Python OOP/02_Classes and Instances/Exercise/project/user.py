# from project.library import Library


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: "Library"):
        authors_available = [author for author in library.books_available.keys()]
        if author in library.books_available and book_name in library.books_available[author]:
            self.books.append(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}

            library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)

            library.rented_books_by_book_name[book_name] = (self.username, days_to_return)

            return f"{book_name} successfully rented for the next {days_to_return} days!"
        #     TILL HERE

        if book_name in library.rented_books_by_book_name:
            _, days_to_return = library.rented_books_by_book_name[book_name]
            return f'The book "{book_name}" is already rented and will be available in {library.rented_books[self.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, library):
        rented_books_names = [value.keys() for value in library.rented_books.values()]
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)

        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]
        #
        # if author in library.books_available.keys():
        #     library.books_available[author].append(book_name)
        # else:
        #     library.books_available[author] = [book_name]
        #     del rented_books_names[self.username][book_name]

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"

