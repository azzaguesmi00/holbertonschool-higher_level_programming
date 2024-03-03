#!/usr/bin/python3
"""containing the append_after function"""

def append_after(filename="", search_string="", new_string=""):
    """appends new-string after a line containing
    search_string in filename """
    with open (filename, 'r', encoding='utf-8') as f:
        link_list = []
        while True:
            line= f.readline()
            if line == "":
                break
            link_list.append(line)
            if search_string in line:
                link_list.append(new_string)
    with open(filename, 'w', encoding='uft-8') as f:
        f.writelines(link_list)
