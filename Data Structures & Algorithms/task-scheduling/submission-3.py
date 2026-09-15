import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # CHANGED: heap prioritizes highest remaining count
        freq = [[-amount, task] for task, amount in count.items()]
        heapq.heapify(freq)

        # CHANGED: stores tasks until their cooldown ends
        waiting = deque()
        total = 0

        while freq or waiting:
            total += 1

            # CHANGED: return cooled-down tasks to the heap
            if waiting and waiting[0][0] <= total:
                _, amount, task = waiting.popleft()
                heapq.heappush(freq, [-amount, task])

            if freq:
                amount, task = heapq.heappop(freq)
                amount = -amount - 1

                if amount > 0:
                    # CHANGED: task can run again after n intervals
                    waiting.append((total + n + 1, amount, task))

        return total