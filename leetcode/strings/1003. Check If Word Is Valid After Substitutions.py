class Solution:
    def isValid(self, s: str) -> bool:
        # La cima dello stack indica quale deve essere il prossimo carattere
        stack = []
        
        # Scorriamo la sequenza e se il carattere corrente e' uguale alla cima dello stack allora lo rimuoviamo dallo stack
        # e aggiungiamo in cima allo stack il successivo elemento ('a' -> 'b', 'b' ->, 'c' -> niente)
        # NOTA: in qualsiasi momento possiamo trovare una 'a', infatti in qualsiasi punto possiamo
        # inserire un nuovo 'abc'
        for c in s:
            if c == 'a':
                stack.append('b') # Il prossimo elemento nella sequenza che ci aspettiamo e' una 'b'
            elif stack and c == stack[-1]:
                stack.pop()
                if c == 'b':
                    stack.append('c') # Il prossimo elemento nella sequenza che ci aspettiamo e' una 'b'
            else:
                return False # c'e' un mismatch, la sequenza non va bene
        
        return not stack # se lo stack e' vuoto ritorna True


# Another solution, same complexity
class Solution:
    def isValid(self, s: str) -> bool:
        ans = "abc"
        i = 0
        
        # Generiamo progressivamente la soluzione scorrendo di una posizione alla volta la sequenza
        while len(ans) < len(s):
            if i < len(ans) and ans[i] == s[i]:
                i += 1 # la sequenza matcha la nostra sequenza generata finora
            else:
                if s[i] == 'a': # Se abbiamo un mismatch e nella sequenza c'e' una 'a', allora inseriamo un 'abc' nel punto indicato
                    ans = ans[:i] + "abc" + ans[i:]
                else:
                    return False
        
        if ans == s:
            return True
        return False
