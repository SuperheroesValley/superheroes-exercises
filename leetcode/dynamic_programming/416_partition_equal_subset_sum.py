'''
  Soluzione 1: ricorsivamente ad ogni chiamata della funzione dp consideriamo il caso in cui non consideriamo l'elemento corrente e il caso in 
  cui lo consideriamo.
  Quando arriviamo ad una situazione in cui i due gruppi di elementi sommati sono uguali al totale / 2 allora possiamo fermarci e abbiamo trovato la soluzione.
  Tempo: 3148 ms
  Spazio: 648.3 MB
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from functools import lru_cache
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_sum = sum(nums)
        if max_sum % 2 != 0:
            return False
        half_sum = max_sum // 2
       
        @lru_cache(None)
        def dp(current_included, current_not_included, index):
            
            if current_included > max_sum // 2 or current_not_included > max_sum // 2:
                return False
            
            if current_included == half_sum or current_not_included == half_sum:
                return True
            
            included = dp(current_included + nums[index], current_not_included, index+1)
            not_included = dp(current_included, current_not_included + nums[index], index+1)
            
            return included or not_included
        
        return dp(0, 0, 0)
    
    
'''
  Soluzione 2: in questo caso ad ogni iterazione generiamo le possibili partizioni e controlliamo se una delle 
  partizioni generate è uguale alla somma dimezzata.
  Tempo: 332 ms
  Spazio: 15 MB
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        max_sum = sum(nums)
        if max_sum % 2 != 0:
            return False
        partitions = set([0])
        half_sum = max_sum // 2
        
        for num in nums:
            current_set = set()
            for partition in partitions:
                current_set.add(partition + num)
                current_set.add(partition)
            if half_sum in current_set:
                return True
            partitions = current_set
