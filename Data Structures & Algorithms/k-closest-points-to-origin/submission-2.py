import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(x**2 + y**2) for [x,y] in points]
        freq = defaultdict(list)
        for d, p in zip(dist, points):
            freq[d].append(p)
        print(points, dist, freq)
        heapq.heapify(dist)
        res =[]
        for i in range(k):
            val = heapq.heappop(dist)
            res.append(freq[val].pop())   
        return res

        

        