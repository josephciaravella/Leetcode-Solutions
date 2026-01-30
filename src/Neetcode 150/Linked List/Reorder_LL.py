# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and not head.next:
            return
        
        # split list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse second half of list
        def reverse(head):
            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev
        
        l2 = reverse(l2)

        # merge the two lists one at a time
        while l2:
            tmp1, tmp2 = l1.next, l2.next
        
            l1.next = l2
            l2.next = tmp1
            
            l1, l2 = tmp1, tmp2
            
        return