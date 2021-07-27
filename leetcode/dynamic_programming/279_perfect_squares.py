'''
Soluzione 1: parte dal numero e per ogni elemento di squares
in modo ricorsivo richiama l'algoritmo fino a che non si arriva ad avere 1 nella chiamata.
A quel punto sappiamo che siamo arrivati ad avere una somma dei quadrati.
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        squares = [i**2 for i in range(1, int(math.floor(math.sqrt(n))) + 1)]

        memo = [-1]*n
        
        def dp(num):
            if num < 0:
                return float("inf")
            if num == 0:
                return 0
            if num == 1:
                return 1
            
            total = float("inf")
            for square in squares:
                
                if memo[num-1] != -1:
                    return memo[num-1]
                else:
                    total = min(total, 1+dp(num-square))

            memo[num-1] = total 
            return total
    
        return dp(n)

'''
Soluzione 2: soluzione iterativa. Si considera il range di numeri compresi tra 1 e n e poi
per ognuno di questi numeri si considerano i quadrati dell'array squares.
Ad ogni iterazione si aggiorna l'array di memoization andando a mettere nella posizione
corrente il minimo tra la posizione corrente e 1+memo[i-square]. Questa parte serve per fare in 
modo che in posizione i ci sia il miglior costo considerando i vari valori di square.
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        squares = [i**2 for i in range(1, int(math.floor(math.sqrt(n))) + 1)]

        memo = [float("inf")]*(n+1)
        memo[0] = 0
        
        for i in range(1, n+1):
            for square in squares:
                if i < square:
                    break
                memo[i] = min(memo[i], 1+memo[i-square])
        return memo[-1]

