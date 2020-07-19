import re

SEARCH_COMMAND_AUTHOR_REGEXP=re.compile(r'search_hit author=.*')
LIST_COMMAND_STATUS_REGEXP=re.compile(r'list_catalog status=.*')
ADD_HIT_COMMAND_REGEXP=re.compile(r'move_hit_catalog isbn=.*')
DELETE_CATALOG_REGEXP=re.compile(r'delete_catalog isbn=.*')
SET_CATALOG_REGEXP=re.compile(r'set_catalog isbn=.* status=(init|want_to_read|read|favourite)')

class Command_Handler:
    def __init__(self, command):
        self.command=command

    def search_extract_author(self):
        author=""
        search_command=SEARCH_COMMAND_AUTHOR_REGEXP.findall(self.command)
        if len(search_command) != 0:
            # Extract author
            author=self.command.partition("=")[2]
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
            #Extract isbn
            isbn =self.command.partition("=")[2]
            print(f"isbn {isbn}")            
            add_hit_params.append(isbn.strip())
            print(f"add_hit_params: {add_hit_params}")
        return add_hit_params

    def delete_extract_isbn(self):
        delete_isbn=DELETE_CATALOG_REGEXP.findall(self.command)
        isbn=''
        if len(delete_isbn) != 0:
            #Extract isbn 
            isbn =self.command.partition("=")[2]      
        return isbn

    def set_catalog_params(self):
        set_catalog_params = []
        find_params=SET_CATALOG_REGEXP.findall(self.command)
        if len(find_params) != 0:
            #Extract isbn and status
            status =self.command.partition("status=")[2]
            print(f"status {status}")
            temp2 =self.command.partition("isbn=")[2]
            print(f"temp2 {temp2}")
            isbn=temp2.partition(" status=")[0]
            set_catalog_params.append(isbn.strip())
            set_catalog_params.append(status.strip())
        print(f"set_catalog_params: {set_catalog_params}")
        return set_catalog_params
        


