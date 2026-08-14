# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return head.next
            

        slow = ListNode(None, head)
        fast = head
        s = ListNode
        s.next = slow

        while fast != None:
            if n > 0:
                n-=1
            
            else:   
                slow = slow.next
            fast = fast.next
        print(slow.val)
        slow.next = slow.next.next
        return s.next.next
