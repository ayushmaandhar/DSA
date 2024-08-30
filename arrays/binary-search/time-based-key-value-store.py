from collections import defaultdict
import time


class TimeMap:

    def __init__(self):
        # we are mapping key to a list
        # that list will have elements in format [timestamp, value]
        self.data = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if len(self.data[key]):
            # using binary search
            pairs = self.data[key]
            
            l, r = 0, len(pairs)-1
            
            while l <= r:
                m = (l+r) // 2
                if pairs[m][0] == timestamp:
                    return pairs[m][1]
                elif pairs[m][0] > timestamp:
                    r = m - 1
                else:
                    l = m + 1
            return "" if l == 0 else pairs[l-1][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)