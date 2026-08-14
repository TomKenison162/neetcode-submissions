class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        middle = head
        fast = head
        start = head

        # Find the middle
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        # Reverse the second half
        current = middle.next
        middle.next = None

        currentNode = None

        while current:
            temp = current.next
            current.next = currentNode
            currentNode = current
            current = temp

        # Merge the two halves
        first = start
        second = currentNode

        while second:
            temps = first.next
            tempm = second.next

            first.next = second
            second.next = temps

            first = temps
            second = tempm

        return