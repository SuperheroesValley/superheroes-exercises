#Leetcode: https://leetcode.com/problems/reverse-linked-list-ii/

#
#2-pass solution
#

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if not head or not head.next:
            return head

        l = r = head

        for i in range(right-1):
            r = r.next
        for i in range(left-2):
            l = l.next

        curr = l if left == 1 else l.next
        prev = r.next
        end = r.next
        start = l

        while curr != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        if left > 1:
            start.next = prev
        if left == 1:
            return prev
        else:
            return head
            
            
            
#            
#1-pass solution
#

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        i = 0
        curr = dummy
        prev = None

        while True:

            if i == right+1:
                end_here = curr
                break

            if i == left-1:
                from_here = curr 

            if i >= left and i <= right:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            else:
                curr = curr.next
            i+=1

        from_here.next.next = end_here
        from_here.next = prev

        return dummy.next
