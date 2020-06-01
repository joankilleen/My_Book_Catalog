from typing import List
from Book import Book
from Book import Book_Catalog
from Book import Book_State
from Google_Client import Client
import json
import re

BOOK_CATALOG_FILEPATH="resources/book_catalog.json"
SEARCH_COMMAND_REGEXP=re.compile(r'search author=.*')
SEARCH_COMMAND_PROMPT = "search author=<author name>"

command = input(f"Input a command:\n{SEARCH_COMMAND_PROMPT}\n")

search_command=SEARCH_COMMAND_REGEXP.findall(command)
if len(search_command) != 0:
    # Extract author
    author=command.partition("=")
    print(author[2])


#response = Client.search_by_author(author)
#google_hits=Client.get_english_titles(response)
#print(google_hits)


#decoded_data = Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)



#decoded_data.list_status(Book_State.WANT_TO_READ)

#Save work before finishing 
#book_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)