from dataclasses import dataclass
from datetime import date


@dataclass
class Grade:
    id: int
    name: str
    created: date
    active: bool = True
