class Solution(object):
    def findMinArrowShots(self, intervals):
        if not intervals:
            return []

        intervals.sort(key = lambda x: x[0])

        i = 1
        intersection = intervals[0]
        res = []
        while i < len(intervals):
            new_intersection = [max(intervals[i][0], intersection[0]), min(intervals[i][1], intersection[1])]
            if new_intersection[1] < new_intersection[0]:
                res.append(intersection[0])
                intersection = intervals[i]
            else:
                intersection = new_intersection
            i+=1

        if intersection[0] <= intersection[1]:
            res.append(intersection[0])

        return len(res)
