class Book:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def create_book_list():
        return [
            Book("Python 101"),
            Book("AI Basics"),
            Book("Data Science")
        ]

books = Book.create_book_list()

for b in books:
    print("Book title:", b.title)
