import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) >1:
            print(stones)
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            res = stone2-stone1
            if res !=0:
                heapq.heappush(stones, -res)
        if stones:
            return -stones[0]
        return 0

        