class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        already = set() # A set that contains all the characters in the current substring
        
        best = 0
        i = 0
        j = 0
        while j < N:
            # Substring is from i (included) to j (excluded)
            best = max(best, j-i)
            
            # s[j] is a duplicate, increment i
            if s[j] in already:
                already.remove(s[i])
                i += 1
            else: # s[j] is not a duplicate
                already.add(s[j])
                j += 1
        
        # Last check
        best = max(best, j-i)
        
        return best
