# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None: return l2
        elif l2 == None: return l1
        elif l1 == None and l2 == None: return None
        head = ListNode()
        new = head
        while l1 and l2:
            if l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        new.next = l1 if l1 else l2
        return head.next