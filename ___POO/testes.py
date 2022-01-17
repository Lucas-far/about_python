

"""
Asserções comuns:

assertEqual
assertNotEqual
assertTrue
assertFalse
assertIs
assertIsNot
assertIsNone
assertIsNotNone
assertIn
assertNotIn
assertIsInstance
assertNotIsInstance
"""

from unittest import TestCase


class Book:

    def introduce_book(self):
        return f'Apresento-lhes e o livro: {self.__name}'

    def comment_about_book(self, commentary):
        return f'O livro {self.__name} {commentary}'

    def book_info(self):
        the_name = f'Nome: {self.__name}\n'
        the_author = f'Autor: {self.__author}\n'
        the_n_pages = f'Número de páginas: {self.__n_pages}\n'
        the_release = f'Data de lançamento: {self.__release}\n'
        frame = the_name + the_author + the_n_pages + the_release
        return frame

    def is_book_large(self):
        if self.__n_pages >= 400:
            return True
        return False

    def is_book_old(self):
        from datetime import datetime
        date_of_today = datetime.today().year
        book_age = date_of_today - self.__release

        if book_age >= 20:
            return True
        return None

    def __init__(self, name, author, n_pages, release):

        self.__name = name
        self.__author = author
        self.__n_pages = n_pages
        self.__release = release


class BookTest(TestCase):

    def setUp(self) -> None:
        self.book_1st = Book(name='Lookout', author='Hamsein Kaid', n_pages=287, release=2015)
        self.book_2nd = Book(name='The loop', author='Linsdra Jakuhen', n_pages=602, release=1980)

    def test_introduce_book(self):
        book_1st_method_1 = self.book_1st.introduce_book()
        content = 'Apresento-lhes e o livro: Lookout'
        # Teste: [assertEqual]
        self.assertEqual(book_1st_method_1, content)

    def test_comment_about_book(self):
        book_1st_method_2 = self.book_1st.comment_about_book(commentary='foi uma grande experiência')
        content = 'O livro Lookout foi uma grande experiência'
        # Teste: [assertEqual]
        self.assertEqual(book_1st_method_2, content)

    def test_book_info(self):
        book_1st_method_3 = self.book_1st.book_info()
        content = 'Nome: Lookout' + 'Autor: Hamsein Kaid' + 'Número de páginas: 287' + 'Data de lançamento: 1980'
        # Teste: [assertNotEqual]
        self.assertNotEqual(book_1st_method_3, content)

    def test_is_book_large(self):
        book_1st_method_4 = self.book_1st.is_book_large()
        content = False
        # Teste: [assertFalse]
        self.assertFalse(book_1st_method_4, content)

    def test_is_book_old(self):
        book_1st_method_5 = self.book_1st.is_book_old()
        content = None
        # Teste: [assertIsNone]
        self.assertIsNone(book_1st_method_5, content)

    def test2_is_book_large(self):
        book_1st_method_6 = self.book_2nd.is_book_large()
        content = True
        # Teste: [assertTrue]
        self.assertTrue(book_1st_method_6, content)

    def test2_is_book_old(self):
        book_1st_method_7 = self.book_2nd.is_book_old()
        content = True
        # Teste: [assertIsNotNone]
        self.assertIsNotNone(book_1st_method_7, content)
