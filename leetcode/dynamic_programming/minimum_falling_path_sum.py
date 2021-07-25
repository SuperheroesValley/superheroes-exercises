'''
Soluzione 1: in questo caso partiamo dalla prima della matrice e poi consideriamo la seconda sommando ad ogni elemento della seconda
l'elemento della prima riga che possiamo sommare. Andiamo avanti di riga in riga calcolando la somma e prendendo il minimo
per ogni posizione che abbiamo nella lista.
Alla fine arriviamo a creare l'ultima riga e restituiamo il minimo dell'ultima riga
'''
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        index = 0
        while index < n-1:
            temp_row = [float("inf")]*n
            current_row = matrix[index]
            for i, item in enumerate(current_row):
                value = matrix[index+1][i] + item
                temp_row[i] = value if value < temp_row[i] else temp_row[i]
                if i > 0:
                    value = matrix[index+1][i-1] + item
                    temp_row[i-1] = value if value < temp_row[i-1] else temp_row[i-1]
                if i < n-1:
                    value = matrix[index+1][i+1] + item
                    temp_row[i+1] = alue if value < temp_row[i+1] else temp_row[i+1]
            matrix[index+1] = temp_row[:]
            index += 1
                    
        return min(matrix[-1])
