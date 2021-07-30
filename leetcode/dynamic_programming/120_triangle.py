'''
Soluzione 1: ricorsiva. Consideriamo tutte le possibili vie dal nodo 
root dell'albero fino all'ultima riga e scegliamo la strada che costa 
di meno. Notare che si usa @lru_cache per fare in modo che la funzione
mantenga in cache i risultati in modo tale che se viene chiamata più di una
volta con lo stesso input, sa cosa rispondere.
'''

from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        @lru_cache
        def dp(row, idx):
            if row >= len(triangle):
                return 0
            if idx > len(triangle[row]):
                return float("inf")
            return triangle[row][idx] + min(dp(rw+1, idx+1), dp(row+1, idx))
            
        return triangle[0][0] + min(dp(1, 0), dp(1, 1))


'''
Soluzione 2: questa è iterativa, partiamo dalla penultima riga e vediamo 
di riga in riga quale è il percorso migliore fino a quel punto.
Poi ad ogni iterazione aggiungiamo una riga e prendiamo il percorso 
di costo minore considerando anche la riga che hai aggiunto.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path_costs = triangle[-1]
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                path_costs[j] = triangle[i][j] + min(path_costs[j], path_costs[j+1])
        return path_costs[0]
