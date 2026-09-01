from random import choice


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False

        self.positions[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False

        index = self.positions[val]
        last_value = self.values[-1]

        self.values[index] = last_value
        self.positions[last_value] = index

        self.values.pop()
        del self.positions[val]

        return True

    def getRandom(self) -> int:
        return choice(self.values)