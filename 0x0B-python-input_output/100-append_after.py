#!/usr/bin/python3
"""Adds a line after a line where a given search string is found"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a new sentence after a sentence that contains 'search_string'

    The file content is modified in the process.
    Args:
        filename (str): path to the file
        search_string (str): string to search
        new_string (str): string to insert
    """

    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if search_string in line:
                lines.insert(count + 1, new_string)
            count += 1

    with open(filename, 'w', encoding='utf-8') as g:
        lines = "".join(lines)
        g.write(lines)
