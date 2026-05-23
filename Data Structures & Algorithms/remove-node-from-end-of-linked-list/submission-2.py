# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt = head
        N = 1
        while pt.next:
            pt = pt.next
            N+=1
        if N-n-1 <0:
            return head.next
        f = head
        for i in range(N-n-1):
            f= f.next
        f.next = f.next.next
        return head
        