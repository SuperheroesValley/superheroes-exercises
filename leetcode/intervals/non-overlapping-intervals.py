'''
Soluzione 1: l'idea è di ordinare la lista di intervalli e poi calcolare l'intersezione tra ogni coppia di 
intervalli. Portiamo avanti l'intersezione e vediamo se si interseca con l'intervallo successivo.
Quando troviamo un intervallo che non si sovrappone allora possiamo fermarci e sappiamo che da li ricominciamo
la ricerca di una nuova sovrapposizione. Quando abbiamo trovato una sovrapposizione tra 3 intervalli, sappiamo 
che per non avere più sovrapposizione dovremo rimuovere 2 intervalli.
'''

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        to_be_removed = 0
        intersection = intervals[0]
        len_intersection = 1
        for interval_start, interval_end in intervals[1:]:
            if interval_start >= intersection[1]:
                to_be_removed += len_intersection - 1
                intersection = [interval_start, interval_end]
                len_intersection = 1
            else:
                intersection = [max(intersection[0], interval_start), min(intersection[1], interval_end)]
                len_intersection += 1
        to_be_removed += len_intersection - 1
        return to_be_removed

    
'''
Soluzione 2
'''

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = 0
				
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] > intervals[i][0]:
                ans += 1

                #Remove elem with bigger end
                idx = i-1 if intervals[i-1][1] == max(intervals[i-1][1], intervals[i][1]) else i  
                del intervals[idx]
            else:
            	i += 1
            

        return ans
