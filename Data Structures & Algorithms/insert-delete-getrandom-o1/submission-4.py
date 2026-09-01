from random import randint

class RandomizedSet:

    def __init__(self):
        self.ranset ={}
        

    def insert(self, val: int) -> bool:
        print(self.ranset)
        v = self.ranset.get(val, -1)
        if v == -1:
            self.ranset[val] = 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        print(self.ranset)
        v = self.ranset.get(val, -1)
        if v == -1:
            return False
        else:
            del self.ranset[val]
            return True
        

    def getRandom(self) -> int:
        print(self.ranset)
        lists = list(self.ranset.keys())
        i = randint(0, len(lists)-1)
        return lists[i]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()