from Book import Book
from Book import Book_Catalog
from typing import List

import json

BOOK_CATALOG_FILEPATH="resources/book_catalog.json"
books=[]
key1="1234-17"
key2="1235-17"
book1 = Book(title="Test1",author="Colum McCann",isbn_13=key1) 
book2 = Book(title="Test2",author="Colum McCann",isbn_13=key2) 
books = Book_Catalog(books=[book1, book2])

books.serialize_to_file(BOOK_CATALOG_FILEPATH)

decoded_book_catalog = Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)

print(decoded_book_catalog)
print(decoded_book_catalog.books)