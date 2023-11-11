class MyRange:
    def __init__(self, start, end, step = 1):
        self.start = start
        self.end = end
        self.step = step

        self.current = start

    # This itself is the iterator
    def __iter__(self):
        return self

    # The next generates the next i
    def __next__(self):
        if self.current < self.end:
            temp = self.current
            self.current += self.step
            return temp
        raise StopIteration("Index out of range")