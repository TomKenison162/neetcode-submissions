import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue =[[x[1][0],x[1][1], x[0]]  for x in enumerate(tasks)]
        heapq.heapify(queue)
        
        i = min([ x[0] for x in tasks])
        current = []
        heapq.heapify(current)
        res= []
        
       
        while len(res) < len(tasks) :
           
            
            while queue:
               
                item = heapq.heappop(queue)
        
                if item[0] <= i:
                    heapq.heappush(current, [item[1], item[2]])
                else:
                    heapq.heappush(queue, item)
                    break
     
            if current: 
                task = heapq.heappop(current)
                i += task[0]
                res.append(task[1])
            else:
                item = heapq.heappop(queue)
                i = item[0]
                i += item[1]
                res.append(item[2])
               
        return res

            

        
        

        
        