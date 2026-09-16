class Foo:
    def __init__(self):
        pass
        self.seq = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.seq = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.seq < 1: continue
        printSecond()
        self.seq = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.seq < 2: continue
        printThird()