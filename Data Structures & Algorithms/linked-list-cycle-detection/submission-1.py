# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict1 = {}
        current = head
        while current != None:
            if dict1.get(current, -1) == -1:
                dict1[current] =1
                current = current.next
            else:
                return True
        return False
            
