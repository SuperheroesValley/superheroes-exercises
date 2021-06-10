# First solution. time complexity is O(n)
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Calculate the size of the list
        size = 0
        curr = head
        while curr is not None:
            size += 1
            curr = curr.next
        
        # Insert a dummy element so that we will always have an element before the one that has to be removed
        dummy = ListNode(next=head)
        
        # The n-th node from the end is equal to the (size-n)th element from the top
        curr = dummy
        for k in range(size-n): # We want to stop to the previous
            curr = curr.next
        
        curr.next = curr.next.next
        
        # Skip the dummy element
        return dummy.next


# Second solution. time complexity is O(n) and we do only one pass of the list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Insert a dummy element so that we will always have an element before the one that has to be removed
        dummy = ListNode(next=head)
        
        # Create two pointers separated by n nodes
        i = j = head
        prev = dummy # The node that is immediatly before i
        for k in range(n):
            j = j.next
        
        # Loop through the list until j reaches the end. At this point i is the node to be removed
        while j != None:
            prev = i
            j = j.next
            i = i.next
        
        prev.next = i.next
        
        # Skip the dummy element
        return dummy.next
