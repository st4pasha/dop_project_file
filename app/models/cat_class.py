from dataclasses import dataclass

@dataclass
class Cat:
    name: str
    age: int
    weight: float
    vaccinated: bool
    colors: list[str]

