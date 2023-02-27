class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        return f"{self.name} bird can fly"

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"

class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="fish"):
        Bird.__init__(self, name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        actions = ['walk']
        if hasattr(self, "fly"):
            actions.append('fly')
        if hasattr(self, "swim"):
            actions.append('swim')
        return f"{self.name} bird can {', '.join(actions)}"