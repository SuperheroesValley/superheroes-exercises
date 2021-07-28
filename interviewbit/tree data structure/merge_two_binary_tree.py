'''
Soluzione 1: iterativa
'''

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        qA = [A]
        qB = [B]
      
        while qA and qB:
            elemA = qA.pop()
            elemB = qB.pop()
        
            if elemA.left and elemB.left:
                qA.append(elemA.left)
                qB.append(elemB.left)
            elif elemB.left and not elemA.left:
                elemA.left = elemB.left 

            if elemA.right and elemB.right:
                qA.append(elemA.right)
                qB.append(elemB.right)
            elif elemB.right and not elemA.right:
                elemA.right = elemB.right
            
            elemA.val += elemB.val
      
        return A
    
    
    
    

'''
Soluzione 2: ricorsiva
'''
class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        
        def merge(A, B):
            if A.left and B.left:
                merge(A.left, B.left)
            elif B.left and not A.left:
                A.left = B.left 

            if A.right and B.right:
                merge(A.right, B.right)
            elif B.right and not A.right:
                A.right = B.right
            
            A.val += B.val
        
        merge(A, B)
        return A
