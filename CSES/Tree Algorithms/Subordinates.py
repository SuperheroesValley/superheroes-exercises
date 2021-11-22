import sys
old = sys.getrecursionlimit() # perhaps 1000 is typical
sys.setrecursionlimit(1000000) # change to allow 1 million nested calls
def solve(n,boss):
  subordinates=[0]*(n+1)
  
  ht=[[] for _ in range(n+1)]#person--->[person1, person2,...]
  for sub,person in enumerate(boss):
    sub+=2  #first element in person number 2 not number 0
    ht[person].append(sub)
  
  def post(person: int):
    nonlocal subordinates, ht
    
    #visit children
    below_me=0
    for child in ht[person]:
      below_me+=post(child)
    
    #visit father
    subordinates[person]=below_me
    
    return below_me+1  #my subordinates + myself
    
  post(1)
  
  return subordinates[1:]
  
  
#read the input
n=int(input())
boss=list(map(int,input().split(" ")))
answer=solve(n,boss)
print(" ".join(map(str,answer)))