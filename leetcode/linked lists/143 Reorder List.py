#Leetcode: https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        length = 1
        lst = head
        
        # Count the number of nodes in the list
        while lst.next:
            lst = lst.next
            length += 1
        length = length // 2
        
        # reach the middle of the list
        middle = head
        for _ in range(length):
            middle = middle.next
    
        prev = None
        node = middle
        
        # change the pointers in the list
        # Ex: 1->2->3->4->5
        # If we are on node 4, the next nod of 4 will be 3
        while node.next:
            tmp = node.next
            node.next=prev
            prev = node 
            node = tmp
        node.next=prev
        
        lst = head
        
        # reorder the list
        for _ in range(length):
            tmp_lst = lst.next
            tmp_node = node.next
            lst.next, node.next = node, lst.next
            lst = tmp_lst
            node = tmp_node 
        lst.next = None


# Another Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """      
        def reverse(head):
            if head is None or head.next is None:
                return head
            curr = head.next
            head.next = None
            while curr != None:
                tmp = curr.next
                curr.next = head
                head = curr
                curr = tmp
            
            return head
        
        #Find list half point
        curr = head
        n = 0
        while curr != None:
            curr = curr.next
            n = n + 1
        
        m = n // 2
        
        midpoint = head
        cnt = 0
        while cnt < m:
            midpoint = midpoint.next
            cnt = cnt + 1
        
        #Divide in two sub-lists
        r_head = midpoint.next
        midpoint.next = None
        
        #Reverse second sub-lists
        r_head = reverse(r_head)
        
        #Alternate-insert second sub-list in first sub-list
        curr = head
        r_curr = r_head
        
        while curr != None and r_curr != None:
            tmp = curr.next
            r_tmp = r_curr.next
            
            curr.next = r_curr
            curr.next.next = tmp
            
            r_curr = r_tmp
            curr = tmp
        
