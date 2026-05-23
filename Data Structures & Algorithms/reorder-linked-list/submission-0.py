# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head #Handling empty case
        prev = None
        curr = head
        while curr:
            nextNode= curr.next 
            curr.next = prev 
            prev = curr
            curr = nextNode
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        #We got the mid
        
        #Get the second half
        sec_half = self.reverseList(mid.next)
        mid.next = None
        first = head
        while sec_half:
            t1, t2 = first.next, sec_half.next 
            first.next = sec_half
            sec_half.next = t1
            first, sec_half = t1, t2
