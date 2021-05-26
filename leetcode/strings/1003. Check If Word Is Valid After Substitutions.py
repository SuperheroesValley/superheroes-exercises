class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == 'a':
                stack.append('b')
            elif stack and c == stack[-1]:
                stack.pop()
                if c == 'b':
                    stack.append('c')
            else:
                return False
        
        return not stack


# Another solution, same complexity
class Solution:
    def isValid(self, s: str) -> bool:
        ans = "abc"
        i = 0
        
        while len(ans) < len(s):
            if i < len(ans) and ans[i] == s[i]:
                i += 1
            else:
                if s[i] == 'a':
                    ans = ans[:i] + "abc" + ans[i:]
                else:
                    return False
        
        if ans == s:
            return True
        return False
