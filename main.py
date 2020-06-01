from typing import List
from Book import Book
from Book import Book_Catalog
from Book import Book_State
from Command_Handler import Command_Handler
from Google_Client import Client
import json

command=""
google_hits = []

BOOK_CATALOG_FILEPATH="resources/book_catalog.json"
SEARCH_COMMAND_PROMPT = "search author=<author name>"
COMMAND_NOT_FOUND = f"Command not found {command}"
QUIT = "QUIT"

while command.upper() != QUIT:

    command = input(f"Input a command:\n{SEARCH_COMMAND_PROMPT}\n")
    command_handler=Command_Handler(command)

    author=command_handler.search_extract_author()

    if len(author) != 0:
        response = Client.search_by_author(author)
        google_hits=Client.get_english_titles(response)
        print(google_hits)
    else:
       print(COMMAND_NOT_FOUND)


#decoded_data = Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)



#decoded_data.list_status(Book_State.WANT_TO_READ)

#Save work before finishing 
#book_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)