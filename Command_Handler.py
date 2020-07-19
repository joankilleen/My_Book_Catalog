import re

SEARCH_COMMAND_AUTHOR_REGEXP=re.compile(r'search_hit author=.*')
LIST_COMMAND_STATUS_REGEXP=re.compile(r'list_catalog status=.*')
ADD_HIT_COMMAND_REGEXP=re.compile(r'move_hit_catalog isbn=.*')

class Command_Handler:
    def __init__(self, command):
        self.command=command

    def search_extract_author(self):
        author=""
        search_command=SEARCH_COMMAND_AUTHOR_REGEXP.findall(self.command)
        if len(search_command) != 0:
            # Extract author
            author=self.command.partition("=")[2]
            print(f"Author: {author}")
        return author

    def list_extract_status(self):
        status=""
        list_command=LIST_COMMAND_STATUS_REGEXP.findall(self.command)
        if len(list_command) != 0:
            # Extract status
            status=self.command.partition("=")[2]
            print(f"Status: {status}")
        return status

    def add_hit_extract_isbn(self):
        add_hit_params = []
        add_hit_command=ADD_HIT_COMMAND_REGEXP.findall(self.command)
        if len(add_hit_command) != 0:
            #Extract isbn and status
            isbn =self.command.partition("=")[2]
            print(f"isbn {isbn}")            
            add_hit_params.append(isbn.strip())
            print(f"add_hit_params: {add_hit_params}")
        return add_hit_params
        


