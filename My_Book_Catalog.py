from typing import List
from Book import Book
from Book import Book_Catalog
from Book import Book_State
from Google_Client import Client
import json

BOOK_CATALOG_FILEPATH="resources/book_catalog.json"

author="Colum McCann"
response = Client.search_by_author(author)
book_catalog=Client.get_english_titles(response)

book_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)

decoded_book_catalog = Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)

print(decoded_book_catalog)
print(decoded_book_catalog.books)