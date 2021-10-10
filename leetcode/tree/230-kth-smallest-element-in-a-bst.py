# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

	'''
	Logic: a symmetric visit on a BST visits the nodes
	       in non-descending order, so we first reach the
	       minimum value, and from that we count up to k.
	'''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        step = 0
        
        def search(node):
            if not node:
                return -1
                
            nonlocal step
            
            left_res = search(node.left)
            if left_res != -1:
                return left_res
            
            step += 1
            if step == k:
                return node.val
            
            return search(node.right)
        
        return search(root)
