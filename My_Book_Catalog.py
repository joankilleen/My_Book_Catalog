from Book import Book
from Book import Book_Catalog
from typing import List
import json
books=[]

key1="1234-17"
key2="1235-17"
book1 = Book(title="Test1",author="Colum McCann",isbn_13=key1) 
book2 = Book(title="Test2",author="Colum McCann",isbn_13=key2) 
books = Book_Catalog(books=[book1, book2])

 # Serializing json  
json_object = json.dumps(books, default=lambda o: o.__dict__, indent=4) 

print(json_object)