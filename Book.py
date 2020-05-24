from typing import List
import json

class Book:
     def __init__(self,title, author, isbn_13):
         self.title = title
         self.author = author
         self.isbn_13 = isbn_13
         self.state = 'want_to_read'

class Book_Catalog(object):
    def __init__(self, books: List[Book]):
        self.books = books