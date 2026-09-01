from random import choice

class RandomizedSet:

    def __init__(self):
        self.ranset ={}
        

    def insert(self, val: int) -> bool:
        
        if val not in self.ranset:
            self.ranset[val] = 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
       
        if val not in self.ranset:
            return False
        else:
            del self.ranset[val]
            return True
        

    def getRandom(self) -> int:
        return choice(list(self.ranset.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()