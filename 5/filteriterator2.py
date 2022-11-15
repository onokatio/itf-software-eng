from typing import Final, Iterator
from enum import Enum
from other import Other
from afterspace import AfterSpace
from state import Context, State


class FilterIterator2(Iterator[str], Context):
    _original: Iterator[str]

    def __init__(self, original: Iterator[str]) -> None:
        super().__init__()
        self._original = original

    AFTER_SPACE: Final[int] = 1
    OTHER: Final[int] = 2

    _state: int = AFTER_SPACE

    def set_state(self, new_state: int):
        self._state = new_state

    def __next__(self) -> str:
        # ここで original から1文字取得して， ch に代入する
        ch = self._original.__next__()
        if self._state == FilterIterator2.AFTER_SPACE:
            print(self._state)
            return AfterSpace.get_instance().process_char(self, ch)
        elif self._state == FilterIterator2.OTHER:
            print(self._state)
            return Other.get_instance().process_char(self, ch)
        else:
            return ch


if __name__ == "__main__":
    for ch in FilterIterator2(iter("The quick brown fox jumps over a lazy dull dog.\n")):
        print(ch, end="")
