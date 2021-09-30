#Problem 1
from collections import defaultdict
def max_span_users(logs, max_span):

    users = defaultdict(lambda: [[],[]])
    
    for log in logs:
        splitted = log.split()
        if splitted[2] == "sign-in":
            users[splitted[0]][0].append(int(splitted[1]))
        else:
            users[splitted[0]][1].append(int(splitted[1]))
    ids = []
    for key in users:
        users[key][0].sort()
        users[key][1].sort()
        range_value = min(len(users[key][0]), len(users[key][1]))
        for i in range(range_value):
            if users[key][1][i] - users[key][0][i] <= max_span:
                ids.append(key)
                break
        
    return ids
  
  print(max_span_users(["30 99 sign-in","30 105 sign-out","12 100 sign-in","20 80 sign-in","12 120 sign-out","20 101 sign-out", "21 101 sign-in"], 20))
