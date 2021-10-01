#Twitter Online Assessment

def getMinDeletions(s):
    letters = set()
    dels = 0
    for char in s:
        if char in letters:
            dels = dels + 1
        else:
            letters.add(char)
    
    return dels

#1-line alternative
def getMinDeletions(s):
    return sum([v-1 for v in Counter(s).values()])

"""
print(getMinDeletions("abab"))
"""
