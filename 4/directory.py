from typing import List
from entry import Entry
from subject import Subject


class Directory(Subject[Entry]):
    _children: List[Entry]
    _obs: List[Subject]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children = []

    def get_children(self) -> List[Entry]:
        return self._children

    def add(self, e: Entry) -> None:
        self._children.append(e)
        self.notify_observers()

    def add_observer(self, obs: Subject) -> None:
        self._obs.append(obs)

    def notify_observers(self) -> None:
        for obs in self._obs:
            obs.update(self)
