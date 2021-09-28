class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        
        def is_pal(sx, dx):
            nonlocal ans
            while sx >= 0 and dx < len(s) and s[sx] == s[dx]:
                ans += 1
                sx -= 1
                dx += 1
                
        for index in range(len(s)):
            is_pal(index, index+1)
            is_pal(index-1, index+1)
            
        return ans
