def read_from_file(path: str):
    with open(path, 'r', encoding="utf-8") as file:
        file_read = file.readlines()
        return file_read

def parse_row(data: str):
    list_str = data.split("|")
    return list_str

def write_to_file(lst: list[str], path: str):
    with open(path, 'w', encoding="utf-8") as file:
        string = ""
        for l in lst:
            string += l.rstrip('\n') + '\n'
        file.write(string)

def list_to_string(lst: list[str], sep='|'):
    return sep.join(lst)

