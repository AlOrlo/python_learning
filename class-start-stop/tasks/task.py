class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start == self.stop:
            return print("Maximal value is reached")
        else:
            self.start += 1
            return self.start

    def get(self):
        return self.start