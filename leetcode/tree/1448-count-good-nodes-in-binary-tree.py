# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesCounter(root, root.val)
        
    def goodNodesCounter(self, root: TreeNode, max_value:int) -> int:
        
        if root==None:
            return 0
        
        left_counter = self.goodNodesCounter(root.left, max(max_value, root.val))
        right_counter = self.goodNodesCounter(root.right, max(max_value, root.val))
        
        if root.val>=max_value:
            return 1 + left_counter + right_counter
        
        return left_counter + right_counter
