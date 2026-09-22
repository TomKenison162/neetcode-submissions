class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        random_ref = {}
        current = head
        newhead = Node(head.val)
        random_ref[head] = newhead
        last = newhead

        while current.next is not None:
            current = current.next
            new = Node(current.val)
            random_ref[current] = new
            last.next = new
            last = new

        current = head
        final = newhead

        while current is not None:
            final.random = random_ref.get(current.random)
            current = current.next
            final = final.next

        return newhead