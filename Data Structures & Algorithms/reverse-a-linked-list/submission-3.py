# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == [] or head == None:
            return head
        currentNode = ListNode(head.val)
        current = head
        while current.next != None:
            current = current.next
            currentNode = ListNode(current.val, currentNode)
            
        return currentNode
             
        