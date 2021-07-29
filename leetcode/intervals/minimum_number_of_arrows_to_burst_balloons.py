'''
Soluzione 1: si itera la lista di intervalli e per ogni coppia di intervalli si crea 
l’intersezione che è formata dal massimo tra i primi due elementi e il minimo dei secondi 
due elementi degli intervalli. Ogni volta si controlla se il primo elemento della coppia
di intersezione è minore o no del secondo elemento. Se è minore continuiamo altrimenti dobbiamo
fermarci, aggiungiamo l’intersezione corrente alla lista dei risultati e prendiamo l’intervallo 
che stavamo considerando come iterazione successiva da prendere in considerazione.
'''

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

    
  
'''
Soluzione 2: soluzione greedy, ordina la lista crescente sul secondo elemento, poi parte dal primo 
intervallo e prende l’elemento finale dell’intervallo come elemento su cui sparare. Ora in modo 
iterativo va avanti e confronta l’elemento su cui sparare anche con il primo elemento dell’intervallo 
successivo, questo perchè sappiamo che l’elemento finale dell’intervallo successivo sarà maggiore, 
se vediamo che il primo dell’intervallo successivo è minore allora sappiamo che c’è una sovrapposizione.
'''

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        arrow_count = 0
        popped_up_to = -float("inf")
        for range_start, range_end in points:
            if range_start > popped_up_to:
                popped_up_to = range_end
                arrow_count += 1
        return arrow_count

