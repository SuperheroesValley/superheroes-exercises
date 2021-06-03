# First solution
# The idea is to scan the string (with the pointer i) until a letter (R/L) is found and then solve it by cases:
#  - if a L is found then backpropagate the L on the left until a stop is reached and restart from i+1
#  - if a R is found then scan the string (with the pointer j) starting from i+1 until a letter (R/L) is found and solve it by cases:
#    - if a R is found then backpropagate the R from j to i, then set i = j and start again this inner loop (the scan for j)
#    - if a L is found we are in this situation: R . . (...) . . L
#      we have to propagate step-by-step both R and L, when they reach the same index then stop and restart the outermost loopp from i+1
# Morevoer we have to consider these two edge cases:
#  - the string starts with an arbitrary number of dots (even zero) and then there is a L. Something like ^. . . . (...) L
#  - the string ends with a R and then an arbitrary number of dots (even zero). Something like R (...) . . . .$
#
# Should have a linear time complexity, O(1) memory
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Necessario perche' le stringhe sono immutables
        dominoes = list(dominoes)
        
        i = 0
        j = 0
        
        while i < len(dominoes):
            # Search the next non-dot element
            while i < len(dominoes) and dominoes[i] == '.':
                i += 1
            
            # Stop condition
            if i == len(dominoes):
                break
            
            # Case when i is L
            if dominoes[i] == 'L':
                # Backpropagate L
                j = i - 1
                while j >= 0 and dominoes[j] == '.':
                    dominoes[j] = 'L'
                    j -= 1
                i += 1
            
            # Case when i is R
            else:
                
                # Find the next non dot element
                j = i + 1
                while j < len(dominoes) and dominoes[j] == '.':
                    j += 1
                
                # Edge case, there are ony dots element until the end of the string
                if j == len(dominoes):
                    while i < len(dominoes):
                        dominoes[i] = 'R'
                        i += 1
                    break # No need to proceed
                
                # Case R .... R
                #      i      j
                if dominoes[j] == 'R':
                    # Propagate R and then set i = j so that at next iteration dominoes[i] = R
                    while i < j:
                        dominoes[i] = 'R'
                        i += 1
                
                # Case R .... L
                #      i      j
                else:
                    # Propagate both step-by-step
                    oldJ = j
                    while i < j:
                        dominoes[i] = 'R'
                        dominoes[j] = 'L'
                        i += 1
                        j -= 1
                    i = oldJ + 1
        
        # convert back to a string
        return ''.join(dominoes)



# Alternative solution
# Time complexity is linear, O(n) memory
# The algorithm scan the string from left to right propagating all the R then does the same thing from right to left for the L
# While doing these proagations it saves also the distance from a "source" (the original R or L)
# Then it does the merge of the propagations.
# If there is both a left and a right propagation for an index i then it chooses the one that is closer to the source, in case they are equal it leaves the dot.
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Necessario perche' le stringhe sono immutables
        dominoes = list(dominoes)
        
        # Remember the distance to the source
        rightPropagation = [0]*len(dominoes)
        leftPropagation = [0]*len(dominoes)
        
        # Propagate from left to right
        i = 0
        while i < len(dominoes):
            if dominoes[i] == 'R':
                j = i + 1
                while j < len(dominoes) and dominoes[j] == '.':
                    rightPropagation[j] = rightPropagation[j-1] + 1
                    j += 1
                i = j
            else:
                i += 1
        
        # Propagate from right to left
        i = len(dominoes)-1
        while i >= 0:
            if dominoes[i] == 'L':
                j = i - 1
                while j >= 0 and dominoes[j] == '.':
                    leftPropagation[j] = leftPropagation[j+1] + 1
                    j -= 1
                i = j
            else:
                i -= 1
        
        # Merge the propagations
        for i in range(len(dominoes)):
            if rightPropagation[i] > 0:
                if leftPropagation[i] > 0: # both propagations, must choose one
                    if rightPropagation[i] < leftPropagation[i]:
                        dominoes[i] = 'R'
                    elif rightPropagation[i] > leftPropagation[i]:
                        dominoes[i] = 'L'
                else: # Only right propagation
                    dominoes[i] = 'R'
            elif leftPropagation[i] > 0: # Only left propagation
                dominoes[i] = 'L'
        
        # convert back to a string
        return ''.join(dominoes)
