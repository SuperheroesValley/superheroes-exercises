'''
Soluzione 1: ordiniamo in modo separato i primi elementi della lista di punti e i secondi elementi della lista ovvero inizio delle conferenze
e fine delle conferenze. Mettiamo un puntatore sull'inizio delle conferenze e uno sulla fine.
Muoviamo in avanti il puntatore dell'inizio fino a che non troviamo che una conferenza è finita, ovvero fino a quando il valore che troviamo
nella lista dell'inizio non è maggiore del valore che puntiamo nella lista di fine.
A questo punto una conferenza è finita e noi possiamo diminuire il numero di stanze disponibili. Sia se la stanza è libera sia se è occupata aumentiamo
comunque il conteggio delle stanze utilizzate perchè se una stanza si è liberata comunque abbiamo un'altra conferenza da allocare quindi non ci sballa 
il calcolo, altrimenti se ne abbiamo una nuova e non abbiamo una stanza vuota incrementiamo.
Costo: =(nLogn)
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
      
'''
Soluzione 2: in questo caso utilizziamo un min heap. Nello heap aggiungiamo il primo intervallo di tempo e poi controlliamo gli intervalli successivi.
Se il primo valore dell'intervallo di tempo successivo è maggiore del minimo dello heap allora vuol dire che l'evento è finito e per il nuovo posso 
usare la stessa stanza quindi tolgo il minimo dallo heap e metto il nuovo. In ogni caso ogni volta metto il nuovo evento nello heap perchè comunque o lo tolgo
uno oppure se non ci sono stanze libere comunque devo creare una nuova stanza.
'''      
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)     
      
'''
Soluzione 3: utilizzando la ricerca binaria
'''
      
import bisect

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()

        rooms = 0
        until = 0

        while intervals:
          print("--")
          print(intervals)
          # incremento il numero di stanze che mi servono e cerco il primo intervallo che 
          # non si sovrappone. Togliamo il primo intervallo della lista dalla lista
          rooms += 1
          until = intervals[0][1]
          intervals.pop(0)
          index = bisect.bisect_right(intervals, [until, 0])
          print(index)

          # Ora consideriamo index e facciamo la stessa cosa cercando il primo intervallo che non si
          # sovrappone. Poi lo togliamo dalla lista e facciamo di nuovo la stessa cosa 
          while index < len(intervals):
            print(intervals[index])
            until = intervals[index][1]
            intervals.pop(index)
            index = bisect.bisect_right(intervals, [until, 0])
        
        return rooms

print(Solution().minMeetingRooms([[0, 10], [2, 8],[4, 6],[12, 18]]))

'''
--
[[0, 10], [2, 8], [4, 6], [12, 18]]
index: 2
[12, 18]
Il primo che non si sovrappone è 12,18 e quindi lo togliamo e vediamo rispetto a questo quale sarà
il primo che non si sovrappone (while interno)
--
Questi due rimangono e quindi vuol dire che si sovrappongono con il primo [0,10] che abbiamo rimosso in precedenza.
[[2, 8], [4, 6]]
index: 1
--
È rimasto questo e quindi vuol dire che si sovrappone con [4, 6]
[[4, 6]]
index: 0
result: 3
'''
