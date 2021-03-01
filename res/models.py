from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Mine:
    map: List[List[int]]
    length: int
    width: int


@dataclass
class Backpack:
    slot1: Optional[int] = None
    slot2: Optional[int] = None
    slot3: Optional[int] = None


@dataclass
class Player:
    x_pos: int = 0
    y_pos: int = 0
    backpack: Backpack = field(default_factory=Backpack)


@dataclass
class Item:
    id: int
    name: str
    hide: bool = True
