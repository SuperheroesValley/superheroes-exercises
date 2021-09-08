# You can find the problem on lintcode
# https://www.lintcode.com/problem/779/description

class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def generateAbbreviations(self, word):
        N=len(word)  
        tot=2**N
        ans=set()
        for mask in range(tot):
            count=0
            new_word=[]
            for bit in range(N):
                #check if bit is set
                if mask&(1<<bit)!=0:
                    count+=1
                else:
                    if count: new_word.append(str(count))
                    count=0
                    new_word.append(word[bit])
            if count: new_word.append(str(count))
            ans.add("".join(new_word))
        return ans
