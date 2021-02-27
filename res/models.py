from typing import List, Optional


class Mine:
    length: int
    width: int
    map: List[List[int]]


class Backpack:
    slot1: Optional[int] = None
    slot2: Optional[int] = None
    slot3: Optional[int] = None


class Player:
    xpos: int
    ypos: int
    back: Backpack


class Item:
    id: int
    name: str
