# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next:
            return None

        # add extra node ahead of head so we can remove head safely if need be.
        # else we just have an extra iteration when navigating to the end of the list
        dummy = ListNode(0, head)
        fast = dummy
        for _ in range(n):
            fast = fast.next

        # have n+1 gap
        slow = dummy

        # move ptrs until fast at the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # head at end, slow.next = nth from end
        slow.next = slow.next.next

        return dummy.next

