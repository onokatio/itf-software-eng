from observe import Observer


class IndentObserver(Observer):
    def __init__(self):
        self.indent: int = 0

    def update(self, e) -> None:
        print(" " * self.indent + e.get_name())
        if e.is_directory():
            self.indent += 2
            for child in e.get_children():
                child.accept(self)
            self.indent -= 2
