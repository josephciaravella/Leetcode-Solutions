# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        c1, next1 = list1, list1.next if list1.val < list2.val else list2, list2.next
        next2 = list2 if c1 == list1 else list1
        while True:
            if next1.val < next2.val:
                next1 = next1.next
                c1.next = next1