# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = None
        curr = head 
        nxt = head.next
        head = head.next
        while nxt:
            if prev:
                prev.next = nxt
            curr.next = nxt.next
            prev = curr
            nxt.next = curr
            curr = curr.next
            if curr:
                nxt = curr.next
            else:
                nxt = None
                
        
        return head
