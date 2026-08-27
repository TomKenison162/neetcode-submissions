# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l1.next == None:
            return l2
        if l2.val == 0 and l2.next == None:
            return l1
            
        new = ListNode()
        c1 = l1
        c2 = l2
        head = new
        while c1 != None or c2 != None:
        
            if c1 is None:
                c1 = ListNode()
                c1.val += next
            if c2 is None:
                c2 = ListNode()
            next = 0
            val = c1.val + c2.val
            if val >=10:
                next =1
                val-=10
            new.val = val
            
            c1, c2 = c1.next, c2.next
            if c1 or next ==1:
                new.next = ListNode()
                new = new.next
                if c1:
                    c1.val += next
        if next ==1:
            new.val = next
        
        return head
            
            

        