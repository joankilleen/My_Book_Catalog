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
SEARCH_COMMAND_PROMPT = "search_hit author=<author name>"
LIST_COMMAND_PROMPT = "list_catalog status=<book status/all>"
ADD_HIT_COMMAND_PROMPT = "move_hit_catalog isbn=<isbn_13>"
COMMAND_NOT_FOUND = f"Command not found {command}"
QUIT = "quit"

while command.lower() != QUIT:

    stored_catalog=Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)

    command = input(f"Input a command:\n{SEARCH_COMMAND_PROMPT}\n{LIST_COMMAND_PROMPT}\n{ADD_HIT_COMMAND_PROMPT}\n")
    command_handler=Command_Handler(command)

    author = command_handler.search_extract_author()
    status = command_handler.list_extract_status()
    add_hit_params = command_handler.add_hit_extract_isbn()

    if len(author) != 0:
        response = Client.search_by_author(author)
        next_hits=Client.get_english_titles(response)
        google_hits.add_catalog(next_hits)
        print(google_hits)
        

    elif len(status) != 0:
       hits = stored_catalog.search_status(status)
       print(hits)

    elif len(add_hit_params) != 0:
        isbn=add_hit_params[0]
        found = google_hits.search_isbn(isbn)
        if len(found.books) == 0:
            HIT_NOT_FOUND = f"Hit not found in google hits {isbn}"
            print(HIT_NOT_FOUND) 
        else:
           print(found)
           stored_catalog.add_catalog(found)
           stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)

    elif command.lower() == QUIT:
        pass
    else:
       print(COMMAND_NOT_FOUND)






#decoded_data.list_status(Book_State.WANT_TO_READ)

#Save work before finishing 
stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)