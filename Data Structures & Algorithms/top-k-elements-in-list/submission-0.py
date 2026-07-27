class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        numsCounts = {}

        for i in range(len(nums)):
            current = numsCounts.get(nums[i], -1)
            if current == -1:
                numsCounts[nums[i]] =[1,i]
            else:
                 numsCounts[nums[i]][0] +=1




        unsorted_array = list(numsCounts.values())
        heapq.heapify_max(unsorted_array)
        
        final= []
        for i in range(k):

            final.append(nums[heapq.heappop(unsorted_array)[1]])
            heapq.heapify_max(unsorted_array)


        return final
        