# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        start = dummy
        # compile numbers
        while l1 or l2:
            total = 0
            if l1 and l2:
                total = l1.val + l2.val + carry
                carry = 0
                if total >= 10:
                    carry = 1
                    total -= 10
                
                dummy.next = ListNode(total)
                dummy = dummy.next
                
                l1 = l1.next
                l2 = l2.next

            elif l1 and not l2:
                total = l1.val + carry
                carry = 0
                if total >= 10:
                    carry = 1
                    total -= 10
                
                dummy.next = ListNode(total)
                dummy = dummy.next
                
                l1 = l1.next

            elif not l1 and l2:
                total = l2.val + carry
                carry = 0
                if total >= 10:
                    carry = 1
                    total -= 10
                
                dummy.next = ListNode(total)
                dummy = dummy.next
                
                l2 = l2.next

        dummy.next = ListNode(carry) if carry else None

        return start.next