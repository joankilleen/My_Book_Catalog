import re

SEARCH_COMMAND_AUTHOR_REGEXP=re.compile(r'search author=.*')
LIST_COMMAND_STATUS_REGEXP=re.compile(r'list status=.*')

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


