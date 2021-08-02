'''
Soluzione 1: con ricorsione. In questo caso quello che facciamo è considerare la cifra
amount che abbiamo e poi ad ogni chiamata ricorsiva consideriamo la lista coins. Per ogni
elemento della lista coins richiamiamo la funzione sottraendo ad amount l'elemento della lista 
coins. Facciamo quindi una chiamata per ogni elemento della lista coins e poi calcoliamo
il minimo. Ad ogni iterazione il minimo che otteniamo lo memorizziamo nella lista 
memo che utilizziamo per la memoization
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [-1]*(amount + 1)
        memo[0] = 0
        
        def dp(current_amount):
            if current_amount < 0:
                return float("inf")
            
            if memo[current_amount] >= 0:
                return memo[current_amount]
            
            memo[current_amount] = min(dp(current_amount - coin) for coin in coins) + 1
            return memo[current_amount]
        ans = dp(amount) 
        return ans if ans != float("inf") else -1

'''
Soluzione 2: iterativa. Questa soluzione è bottom up.
In questo caso partiamo dal valore più basso di coins e cerchiamo iterativamente
di modificare l'array memo andando a contare per ogni elemento dell'array (elementi
che vanno dal minimo della lista coins fino ad amount) quante monete sono 
necessarie per formare quell'elemento.
Esempio con
[1,2,5], amount = 11
la lista memo è la seguente:
[0,1,1,2,2,1,2,2,3,3,2,3]
quindi 3 che è in posizione amount è la soluzione.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [float("inf")] * (amount+1)
        memo[0] = 0
        min_coins = min(coins)
        for current_value in range(min_coins, amount + 1):
            memo[current_value] = min([memo[current_value-coin] for coin in coins if current_value-coin >= 0]) + 1
        return memo[-1] if memo[-1] != float("inf") else -1
