from heapq import heapify, heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], x[1]))
        # Creating empty heap
        heap = []
        heapify(heap)
        max_len = 0
            
        for interval in intervals:
            if len(heap)>0:
                while len(heap)>0 and heap[0]<=interval[0]:
                    heappop(heap)
                    
            heappush(heap, interval[1])  
            if len(heap)>max_len:
                max_len = len(heap)
                
        return max_len
