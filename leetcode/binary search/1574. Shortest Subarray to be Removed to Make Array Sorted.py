class Solution:
    def bin_search_from(self, arr, start, target):
        """ binary search the index of the first element of `arr` from `start` that is at least `target` """
        
        l = start
        r = len(arr)-1
        sol = r + 1
        
        while l <= r:
            m = (l+r)//2
            if arr[m] < target:
                l = m + 1
            else:
                sol = m
                r = m - 1
        
        return sol
    
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        begin = [arr[0]]
        for e in arr[1:]:
            if begin[-1] <= e:
                begin.append(e)
            else:
                break
        end = [arr[-1]]
        for e in arr[-2::-1]:
            if end[-1] >= e:
                end.append(e)
            else:
                break
        
        end.reverse()
        
        # Simple case
        if len(begin) == len(arr):
            return 0
        
        # arr is in the form
        # [begin] :: [to remove] :: [end]
        
        # we want to find the minimum number of elements to remove from begin and end
        # in order to make the array [begin] :: [end] non decreasing
        
        j = 0
        sol = max(len(begin), len(end)) # base solution, just take either begin or end
        
        for i in range(1, len(begin)+1):
            # Binary search approach O(len(begin) * log(len(end)))
            # ~ j = self.bin_search_from(end, j, begin[i-1])
            
            # Iterative approach O(len(begin) + len(end))
            while j < len(end) and end[j] < begin[i-1]:
                j += 1
            
            # take begin[:i] and end[j:]
            sol = max(sol, i + len(end)-j)
            
            # We can't find any better solution
            if j == len(end):
                break
        
        return len(arr) - sol
