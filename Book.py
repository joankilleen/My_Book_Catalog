from typing import List
from enum import Enum

import json


class Book:
     def __init__(self,title, author, isbn_13):
         self.title = title
         self.author = author
         self.isbn_13 = isbn_13
         self.state = Book_State.INIT

     @classmethod
     def from_json(cls, data: dict):
        return cls(**data)
     
     def __str__(self):
        return "{self.isbn_13} {self.title} {self.author} {self.state}".format(self=self)


#List of books which can be serialized and deserializes as Json and written to file
class Book_Catalog(object):
    def __init__(self, books: List[Book]):
        self.books = books

    @classmethod
    def from_json(cls, data: dict):
        list_books = list(map(Book.from_json, data["books"]))
        return cls(books)

    # Serialize as Json and persist to file
    def serialize_to_file(self, filepath):
        json_object = json.dumps(self, default=lambda o: o.__dict__) 
        with open(filepath, "w") as outfile: 
            json.dump(json_object, outfile) 

    # Read book catalog from file
    @staticmethod
    def serialize_from_file(filepath):
        with open(filepath, "r") as infile:
            json_object = json.load(infile)
            book_catalog = Book_Catalog(**json.loads(json_object))
            return book_catalog

    def __str__(self):
        str = ""
        for book in self.books:
            str += book.__str__() + "\n"
        return str

class Book_State(str, Enum):
    INIT='init'
    WANT_TO_READ='want_to_read'
    READ='read'
    FAVOURITE='favourite'
