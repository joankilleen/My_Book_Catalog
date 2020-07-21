from typing import List
from Book import Book
from Book import Book_Catalog
from Command_Handler import Command_Handler
from Google_Client import Client
import json

command=""
google_hits = Book_Catalog(books=[])

BOOK_CATALOG_FILEPATH="resources/book_catalog.json"
SEARCH_COMMAND_PROMPT = "search_hit author=<author name>"
LIST_COMMAND_PROMPT = "list_catalog status=<book status/all>"
MOVE_HIT_COMMAND_PROMPT = "move_hit_catalog isbn=<isbn_13>"
DELETE_CATALOG_COMMAND_PROMPT = "delete_catalog isbn=<isbn_13>"
SET_STATUS_CATALOG_COMMAND_PROMPT = "set_catalog isbn=<isbn_19> status=<book status>"
COMMAND_NOT_FOUND = f"Command not found {command}"
QUIT = "quit"

while command.lower() != QUIT:

    stored_catalog=Book_Catalog.serialize_from_file(BOOK_CATALOG_FILEPATH)

    command = input(f"Input a command:\n{SEARCH_COMMAND_PROMPT}\n{MOVE_HIT_COMMAND_PROMPT}\n{LIST_COMMAND_PROMPT}\n{DELETE_CATALOG_COMMAND_PROMPT}\n{SET_STATUS_CATALOG_COMMAND_PROMPT}\n\n")
    command_handler=Command_Handler(command)

    author = command_handler.search_extract_author()
    status = command_handler.list_extract_status()
    add_hit_params = command_handler.add_hit_extract_isbn()
    delete_isbn = command_handler.delete_extract_isbn()
    set_status_params = command_handler.set_catalog_params()

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
           stored_catalog.add_catalog(found)
           stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)

    elif len(delete_isbn) != 0:
        found = stored_catalog.search_isbn(delete_isbn)
        if len(found.books) == 0:
            HIT_NOT_FOUND = f"Hit not found in stored catalog {delete_isbn}"
            print(HIT_NOT_FOUND) 
        else:
            stored_catalog = stored_catalog.delete(found.books[0])
            stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)
            print(stored_catalog)

    elif len(set_status_params) != 0:
        isbn=set_status_params[0]
        status=set_status_params[1]
        found = stored_catalog.search_isbn(isbn)
        if len(found.books) == 0:
            HIT_NOT_FOUND = f"Hit not found in stored catalog {isbn}"
            print(HIT_NOT_FOUND) 
        else:
            update = found.books[0]
            print(f"Book found: {update}")
            setattr(update, 'state', status)
            print(f"Before update: {update}")
            stored_catalog = stored_catalog.update_book(update)
            print(stored_catalog)
            stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)
            print(stored_catalog)

    elif command.lower() == QUIT:
        pass
    else:
       print(COMMAND_NOT_FOUND)


#Save work before finishing 
stored_catalog.serialize_to_file(BOOK_CATALOG_FILEPATH)