# Time complexity: O(n)
# Sliding window with fixed size
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pattern = {}
        ans = []
        l = 0
        r = 9

        while r < len(s):
            pattern.setdefault(s[l:r+1],0)
            pattern[s[l:r+1]] += 1

            if pattern[s[l:r+1]] == 2:
                ans.append(s[l:r+1])

            l += 1
            r += 1

        return ans
