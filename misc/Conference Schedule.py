#Twitter Online Assessment

def conf_schedule(start: List[int], end: List[int])->int:
    tuples = [(start[i], end[i]) for i in range(len(start))]
    tuples.sort(key=lambda t: t[1])
    start = -1
    end = -1
    
    max_conf = 0
    for conf in tuples:
        if end<=conf[0]:
            max_conf+=1
            start, end = conf
    return max_conf

"""
print(conf_schedule([1, 1, 2], [3, 2, 4]))
"""
