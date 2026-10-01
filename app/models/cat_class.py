from dataclasses import dataclass
from datetime import date


@dataclass
class Cat:
    name: str
    age: int
    weight: float
    vaccinated: bool
    colors: list[str]