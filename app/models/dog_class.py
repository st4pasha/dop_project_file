from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    weight: float
    vaccinated: bool
    colors: list[str]

def parse_row(data: str):
    list_str = data.split("|")
    return list_str

def dog_to_string(dog: Dog) -> str:
    string = ""
    for v in dog.__dict__.values():
        string += str(v) + "|"
    string = string[:-1]
    return string

def list_to_class(lst: list):
    dog = Dog(*lst)
    return dog


def search_dog(name: str, cats: list[str]):
    for dog in cats:
        dog_list = parse_row(dog)
        dog_class = list_to_class(dog_list)
        if dog_class.name == name:
            return dog_class
    return "Cat not found."