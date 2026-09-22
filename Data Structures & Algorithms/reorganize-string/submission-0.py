import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        sets = "".join(list(set(s)))
        heap = [[-count[k], k] for k in count.keys()]
        heapq.heapify(heap)
        print(heap)
        final = []
       
        last =""
        while len(final) != len(s):
            print(final, heap, last)
            num, curr = heapq.heappop(heap)
            if curr == last:
                if not heap:
                    return ""
                num2, sec = heapq.heappop(heap)
                heapq.heappush(heap, [num, curr])
                final.append(sec)
                last = sec
                if num2 != -1:
                    heapq.heappush(heap, [num2+1, sec])
            else:
                final.append(curr)
                if num != -1:
                    heapq.heappush(heap, [num+1, curr])
                last = curr

            
           
        return "".join(final)

            


        