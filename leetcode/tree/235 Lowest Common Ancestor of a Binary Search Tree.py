# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
            
        while True:
            if root.val >= p.val and root.val <= q.val:
                return root
            elif p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right

                
#A more "defensive" solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val == p.val:
            return q
        
        #Ip: p.val < q.val
        if p.val > q.val:
            p,q = q,p #swap

        while root is not None:
            if p.val <= root.val <= q.val:
                return root
            elif q.val <= root.val:
                root = root.left
            else:
                root = root.right
        
        return None
