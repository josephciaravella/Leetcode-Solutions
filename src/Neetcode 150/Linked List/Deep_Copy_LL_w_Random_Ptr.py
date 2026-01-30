# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # no head
        if not head:
            return None
        
        new = Node(head.val)

        # hashmap connecting original -> new nodes
        nodes = {}
        nodes[head] = new

        # hold position of head
        dummy = head

        head = head.next
        # pass once to create nodes first
        while head:
            new = Node(head.val)
            nodes[head] = new
        
            head = head.next

        # pass again to take care of the pointers
        head = dummy
        dummy = nodes[head]
        curr = nodes[head]
        while head:
            curr.next = nodes[head.next] if head.next else None
            curr.random = nodes[head.random] if head.random else None
        
            head = head.next
            curr = curr.next

        return dummy


