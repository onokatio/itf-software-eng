from typing import List
from entry import Entry


class Directory(Entry):
    _children: List[Entry]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children = []

    def get_children(self) -> List[Entry]:
        return self._children

    def add(self, e: Entry) -> None:
        self._children.append(e)
