#From Twitter Online Assessment

from collections import defaultdict
def Problem(words, sentences):
    def get_fingerprint(word):
        return frozenset(Counter(word).items())

    dic = defaultdict(list)
    for word in words:
        wf = get_fingerprint(word)
        if word not in dic[wf]:
            dic[wf].append(word)
    
    #print({k:v for k,v in dic.items()})
    
    result = []
    for sentence in sentences:
        m = 1
        s = sentence.split()
        for w in s:
            wf = get_fingerprint(w)
            if w not in dic[wf]:
                m *= (len(dic[wf])+1)
            else:
                m *= len(dic[wf])
        result.append(m)
    
    return result

"""
# Example 1
words = ['listen', 'silent', 'it', 'is']
sentences = ['listen it is silent']
print(Problem(words, sentences))

# Example 2
words = ['listen', 'it', 'is']
sentences = ['listen listen'] 
print(Problem(words, sentences))

# Example 3
words = ['its', 'ist', 'ist']
sentences = ['its ist its']
print(Problem(words, sentences))
"""
