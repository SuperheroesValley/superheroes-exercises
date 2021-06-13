#Leetcode: https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        solution = []
 
        while i < len(firstList) and j < len(secondList):
            startA, startB = firstList[i][0], secondList[j][0]
            endA, endB     = firstList[i][1], secondList[j][1]
 
            #intersection check
            l = max(startA, startB)
 
            if (startA <= startB and endA >= startB) or (startB <= startA and endB >= startA):
                r = min(endA, endB)
                solution.append([l, r])
 
            # go on
            if endA <= endB:
                i += 1
            if endB <= endA:
                j += 1
 
        return solution
