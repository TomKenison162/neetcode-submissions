# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        newNode = ListNode(None)
        start = ListNode(0, newNode)
        while list1 and list2:
            if list2 == None or list1.val <= list2.val:
                if list1:
                    newNode.next = ListNode(list1.val)
                    newNode = newNode.next
                    list1 = list1.next
                else:
                    newNode.next = None
                    list1 = list1.next
            else:
                if list2:
                    newNode.next = ListNode(list2.val)
                    newNode = newNode.next
                    list2 = list2.next
                else:
                    newNode.next = None
                    list2 = list2.next
        if list1:
            newNode.next = list1
            newNode = newNode.next
        if list2:
            newNode.next = list2
        return start.next.next
            
            

               
        