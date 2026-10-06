from dataclasses import dataclass
from app.service.service import read_from_file

@dataclass
class Cat:
    name: str
    age: int
    weight: float
    vaccinated: bool
    colors: list[str]

def parse_row(data: str):
    list_str = data.split("|")
    return list_str

def cat_to_string(cat: Cat) -> str:
    string = ""
    for v in cat.__dict__.values():
        string += str(v) + "|"
    string = string[:-1]
    return string

def list_to_class(lst: list):
    cat = Cat(*lst)
    return cat


def search_cat(name: str, cats: list[str]):
    for cat in cats:
        cat_list = parse_row(cat)
        cat_class = list_to_class(cat_list)
        if cat_class.name == name:
            return cat_class
    return "Cat not found."