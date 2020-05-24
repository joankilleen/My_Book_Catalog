from Book import Book
from Book import Book_Catalog
from typing import List
import requests


url_template = "https://www.googleapis.com/books/v1/volumes?q=inauthor:{}"
class Client:

	@staticmethod
	def search_by_author(author_name):
		url = url_template.format(author_name)
		print(url)
		r = requests.get(url)
		print(f"Status Code {r.status_code} for url: {url}")
		return r

	@staticmethod
	def get_english_titles(response):
		num_hits = response.json()["totalItems"]
		book_list = response.json()["items"]
		book_hits = []
		for item in book_list:
			volume=item["volumeInfo"]
			language = volume["language"]
			isbn_13 = ""
			if language=="en":
				 title=volume["title"]
				 author=volume["authors"]
				 identifiers=volume["industryIdentifiers"]
				 for identifier in identifiers:
					 type=identifier["type"]
					 if type=="ISBN_13": 
						  isbn_13=identifier["identifier"]
						  next_book=Book(title=title,author=author,isbn_13=isbn_13)			 
				 book_hits.append(next_book)
				 #print(next_book)
		books_to_return=Book_Catalog(books=book_hits)
		print(len(books_to_return.books))
		return books_to_return
		
		 
		 
		 


