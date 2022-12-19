from book import Book
import unittest
from bookshelf import BookShelf

book_shelf = BookShelf()
book_shelf.append_book(Book("Isaac Asimov", "I, Robot"))
book_shelf.append_book(Book("Ray Bradbury", "Fahrenheit 451"))
book_shelf.append_book(Book("Ted Chiang", "Stories of Your Life and Others"))
book_shelf.append_book(
    Book("Philip Kindred Dick", "Do Androids Dream of Electric Sheep?"))

for book in book_shelf:
    book.print_title()


class BookShelfTest(unittest.TestCase):
    _book_shelf: BookShelf

    def setUp(self) -> None:
        self._book_shelf = BookShelf()
        self._book_shelf.append_book(Book("Isaac Asimov", "I, Robot"))
        self._book_shelf.append_book(Book("Ray Bradbury", "Fahrenheit 451"))
        self._book_shelf.append_book(
            Book("Ted Chiang", "Stories of Your Life and Others"))

    def test_len(self):
        self.assertEqual(len(self._book_shelf), 3)

    def test_remove_at(self):
        self._book_shelf.remove_at(1)
        self.assertEqual(len(self._book_shelf), 2)
        self.assertEqual(self._book_shelf.book_at(0).print_title(), "I, Robot")

    def test_iterator(self):
        self.setUp()
        it = self._book_shelf.__iter__()

        self.assertEqual(it.__next__().print_title(), "I, Robot")
