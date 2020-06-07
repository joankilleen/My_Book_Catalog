from typing import List
from Book import Book
from Book import Book_Catalog
from Book import Book_State
from Command_Handler import Command_Handler
from Google_Client import Client
import json

command=""
google_hits = Book_Catalog(books=[])

BOOK_CATALOG_FILEPATH="resources/book_catalog.json"
SEARCH_COMMAND_PROMPT = "search author=<author name>"
LIST_COMMAND_PROMPT = "list_cat status=<book status/all>"
ADD_HIT_COMMAND_PROMPT = "add_hit isbn=<isbn_13> status=<book_status>"
COMMAND_NOT_FOUND = f"Command not found {command}"
QUIT = "quit"

while command.lower() != QUIT:

    stored_catalog=Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)

    command = input(f"Input a command:\n{SEARCH_COMMAND_PROMPT}\n{LIST_COMMAND_PROMPT}\n{ADD_HIT_COMMAND_PROMPT}\n")
    command_handler=Command_Handler(command)

    author = command_handler.search_extract_author()
    status = command_handler.list_extract_status()
    add_hit_params = command_handler.add_hit_extract_params()

    if len(author) != 0:
        response = Client.search_by_author(author)
        next_hits=Client.get_english_titles(response)
        google_hits.add_catalog(next_hits)
        print(google_hits)

    elif len(status) != 0:
       hits = stored_catalog.search_status(status)
       print(hits)

    elif len(add_hit_params) != 0:
        print("")

    else:
       print(COMMAND_NOT_FOUND)






#decoded_data.list_status(Book_State.WANT_TO_READ)

#Save work before finishing 
stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)