from typing import List
from enum import Enum

import json

INIT='init'
WANT_TO_READ='want_to_read'
READ='read'
FAVOURITE='favourite'


        

class Book:
     def __init__(self, title, author, isbn_13, state=INIT):
         self.title = title
         self.author = author
         self.isbn_13 = isbn_13
         self.state = state

     @classmethod
     def from_json(cls, data: dict):
        return cls(**data)
     
     def __str__(self):
        return "{self.isbn_13} {self.title} {self.author} {self.state}".format(self=self)


#List of books which can be serialized and deserialized as Json and written to file
class Book_Catalog(object):
    
    def __init__(self, books: List[Book]):
        self.books = books  
        
   

    #Seach books of a certain status
    def search_status(self, book_state='all'): 
        data = []
        if book_state == 'all':
            return Book_Catalog(self.books)
        for book in self.books:
            if book.state==book_state:
                data.append(book)
        return Book_Catalog(data)

    #Seach book catalog for an isbn
    def search_isbn(self, isbn): 
        data = []      
        for book in self.books:
            if book.isbn_13==isbn:
                data.append(book)
        return Book_Catalog(data)

    #Merge two catalogues
    def add_catalog(self, catalog_to_add):
        for book in catalog_to_add.books:
            self.add_if_not_duplicate(book)
        return self

    #Add a book if not a duplicate
    def add_if_not_duplicate(self, new_book: Book):
        is_duplicate = bool(False)
        for book in self.books:
            if new_book.isbn_13 == book.isbn_13:
                is_duplicate = bool(True)
                break
        if is_duplicate == bool(False):
            self.books.append(new_book)

    #Delete a book from the catalog
    def delete(self, delete_book: Book):
        for book in list(self.books):
            if book.isbn_13==delete_book.isbn_13:
                self.books.remove(book)
        return self

    def update_book(self, update:Book):
        for book in self.books:
            if book.isbn_13==update.isbn_13:
                self.books.remove(book)
                self.books.append(update)
                print(f"Updating with book update {update}")
                print(f"new status {update}")
        return Book_Catalog(self.books)
        




    # Serialize as Json and persist to file
    def serialize_to_file(self, filepath):
        json_object = json.dumps(self, default=lambda o: o.__dict__) 
        with open(filepath, "w") as outfile: 
            json.dump(json_object, outfile) 
        return self

    @classmethod
    def from_json(cls, data: dict):
        list_books = list(map(Book.from_json, data["books"]))
        return cls(books) 

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
                state=item["state"]
                next_book=Book(title=title,author=author,isbn_13=isbn_13,state=state)	
                book_data.append(next_book)   
            return Book_Catalog(books=book_data)

    def __str__(self):
        str = ""
        for book in self.books:
            str += book.__str__() + "\n"
        return str


