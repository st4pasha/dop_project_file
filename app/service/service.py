from app.models.cat_class import Cat

def write_to_file(cat: Cat):
    file = open("app/repositories/file.txt", "w")
    file.write(cat_to_string(cat))
    file.close()

def read_from_file():
    file = open("app/repositories/file.txt", "r")
    cat_str = file.read()
    return cat_str


def parse_row(data: str):
    list_str = data.split("|")
    return list_str


def cat_to_string(cat: Cat) -> str:
    string = ""
    for v in (cat.__dict__).values():
        string += str(v) + "|"
    string = string[0:-1]
    return string

def list_to_class(lst: list):
    cat = Cat(*lst)
    return cat



