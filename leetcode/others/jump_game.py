'''
Soluzione 1: in questa soluzione si itera la lista nums e per ogni elemento della lista calcoliamo
il punto della lista dove riusciamo a saltare considerando sia se il salto viene fatto usando l'elemento
corrente della lista sia se il salto viene fatto considerando il precedente. Se vediamo che il salto dall'elemento 
dove mi trovo è uguale alla posizione su cui mi trovo allora mi fermo perchè vuol dire che non posso andare avanti.
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        index = 0
        if nums[index] == 0:
            return False
        
        for jump in nums[1:]:
            index += 1
            nums[index] = max((index+jump), nums[index-1])
            if nums[index] == index:
                return False
            if nums[index] >= len(nums) - 1:
                return True
        return False


'''
Soluzione 2: soluzione greedy. In questo caso indichiamo il nostro obiettivo che è raggiungere la posizione n-1.
Poi partendo da quella posizione vediamo se considerando la posizione e il salto che si può fare superiamo il goal 
o meno. A mano a mano che si va indietro e che troviamo sempre possibilità di superare il goal, lo diminuiamo.
Se alla fine il goal è 0, ovvero se siamo arrivati alla posizione 0 della lista e da li riusciamo a raggiungere il goal
allora possiamo restituire True.
'''

class Solution:
    def canJump(self, nums):
        n = len(nums)
        goal = n-1

        for i in range(n-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        return goal==0
