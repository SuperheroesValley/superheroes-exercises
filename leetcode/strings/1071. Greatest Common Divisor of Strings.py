import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N = len(str1)
        M = len(str2)
        
        g = math.gcd(N, M)
        
        # Proviamo con dim 1
        if str1 == str1[0]*N and str2 == str2[0]*M and str1[0] == str2[0]:
            # abbiamo una soluzione
            return str1[:g]
        
        if g == 1:
            return ""
        
        d = g
        candidate = str1[d]
        if str1 == candidate*(N//d) and str2 == candidate*(M//d):
            num = math.gcd(N//d, M//d)
            return str1[:num*d]
        
        return ""


# Super easy solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N = len(str1)
        M = len(str2)
        
        if str1+str2 == str2+str1:
            # Spiegazione: la stringa s = str1[:g] e' la massima soluzione possibile, infatti
            # se esistesse una soluzione piu' lunga vorrebbe dire che esisterebbe un numero piu' grande di g
            # che divide sia N che M, ma e' impossibile
            #
            # se esiste una soluzione di lunghezza l con l < g allora esisterebbe anche la soluzione lunga g,
            # infatti l deve dividere sia N che M e quindi l deve dividere anche g, quindi concatenando g/l volte la stringa
            # ne otteniamo una di dimensione g che e' la soluzione
            g = math.gcd(N, M)
            return str1[:g]
        else:
            return ""
