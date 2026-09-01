class TimeMap:

    def __init__(self):
        self.store = {}
        self.timestore = {}
    
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        time =self.store.get(key, -1)
        if time == -1:
            self.timestore = {timestamp : value}
            self.store[key] = self.timestore
        else:
            time[timestamp] = value

        

    def get(self, key: str, timestamp: int) -> str:
        time =self.store.get(key, -1)
        if time == -1:
            return ""

        val = time.get(timestamp, -1)
        if val == -1:
            keys = sorted(list(time.keys()))
            print(keys)
            for i in range(len(keys)):
                prev = keys[-i-1]
                print(prev, -i-1)
                if prev <= timestamp:
        
                    return time[prev]
            return ""
        
        else:
            return val
        
        
