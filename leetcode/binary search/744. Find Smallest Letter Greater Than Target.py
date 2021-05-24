class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        sol = letters[0] # Case limit when there is no element in letters that is bigger than target
        
        while l <= r:
            m = (l+r)//2
            if letters[m] <= target:
                l = m+1
            else:
                sol = letters[m]
                r = m - 1
        
        return sol
