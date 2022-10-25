class FibSequence:
    _num: int

    def __init__(self, num: int):
        self._num = num
        self._i = 0
        self._j = 1

    def __iter__(self):
        if self._num <= 0:
            raise StopIteration

        yield 1
        self._num -= 1

        while self._num > 0:
            val = self._i + self._j
            self._i = self._j
            self._j = val
            self._num -= 1
            yield val
        return StopIteration



if __name__ == "__main__":
    for v in FibSequence(10):
        print(v)