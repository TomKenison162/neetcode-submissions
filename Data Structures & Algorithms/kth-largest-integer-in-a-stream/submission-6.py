from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k =k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heappop(self.minheap)

        

    def add(self, val: int) -> int:
        heappush( self.minheap, val)
        if len(self.minheap) > self.k:
            heappop(self.minheap)
        return self.minheap[0]

        
