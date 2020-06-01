from typing import List
from enum import Enum

import json

class Book_State(str, Enum):
    INIT='init'
    WANT_TO_READ='want_to_read'
    READ='read'
    FAVOURITE='favourite'

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

    #Print books of a certain status
    def list_status(self, book_state: Book_State): 
        data = []
        for book in self.books:
            if book.state==book_state:
                data.append(book)
        print(Book_Catalog(data))



    # Read book catalog from file
    @staticmethod
    def serialize_from_file(filepath):
        with open(filepath, "r") as infile:
            json_object = json.load(infile)
           
            catalog = Book_Catalog(**json.loads(json_object))
            books=catalog.books
            book_data=[]
             # This is still not really a catalog but a half way house json format. I don't know why!
             # Convert to Book_Catalog
            for item in books:
                title= item["title"]
                author=item["author"]
                isbn_13=item["isbn_13"]
                next_book=Book(title=title,author=author,isbn_13=isbn_13)	
                book_data.append(next_book)   
            return Book_Catalog(books=book_data)

    def __str__(self):
        str = ""
        for book in self.books:
            str += book.__str__() + "\n"
        return str


