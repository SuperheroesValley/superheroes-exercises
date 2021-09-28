class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        palindrome = s[0]
        length = 1
        
        def is_palindrome(mid, sx, dx):
            nonlocal palindrome, length
            while sx >= 0 and dx < len(s) and s[sx] == s[dx]:
                if dx - sx + 1 > length:
                    length = dx - sx + 1
                    palindrome = s[sx:dx+1]
                dx += 1
                sx -= 1
        
        for index in range(len(s)):
            is_palindrome(index, index-1, index+1)
            is_palindrome(index, index, index+1)
            
        return palindrome
