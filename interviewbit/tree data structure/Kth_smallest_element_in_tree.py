'''
Soluzione 1: ricorsiva con contatore c 
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    c = 0

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        if A:  
            res = self.kthsmallest(A.left, B)   
            if res:
                return res
            self.c = self.c + 1
            if B == self.c:
                return A.val
                
            return self.kthsmallest(A.right, B)

'''
Soluzione 2: utilizziamo una lista di un solo elemento per decrementare la K invece di 
incrementare la c come abbiamo fatto nella soluzione 1.
'''
class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    
	def kthsmallest(self, root, k):
        def wrapper(root, list_k):        
          if root:  
              res = wrapper(root.left, list_k)
              if res:
                  return res

              list_k[0] -= 1
              if list_k[0] == 0:
                  return root.val

              return wrapper(root.right, list_k)
            
        return wrapper(root, [k])
      
 
'''
Soluzione 3: utilizzando una lista per salvare la visita dell'albero e poi prendiamo l'elemento B-1
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    
    def in_order_visit(self, A, B, l):
        if len(l) == B:
            return
        if A:
            self.in_order_visit(A.left, B, l)
            l.append(A.val)
            self.in_order_visit(A.right, B, l)
    
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        l = []
        self.in_order_visit(A, B, l)
        return l[B-1]
        
