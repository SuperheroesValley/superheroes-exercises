class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
	    #Two Pointers
        p1 = 0
        p2 = 0
        
        while p1<len(A) and p2<len(B):
            if A[p1] < B[p2]: #traverse A until you find a spot for B[p2]
                p1 += 1
            elif A[p1] >= B[p2]: #spot found
                A.insert(p1,B[p2])
                p1 += 1
                p2 += 1
            
        if p1>=len(A) and p2<len(B): #A is exhausted but B has yet to be fully traversed
            for el in B[p2:]:
                A.append(el)
