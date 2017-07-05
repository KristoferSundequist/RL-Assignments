import numpy as np

asd = np.matrix([
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    ])

trans = np.array([
    [],[0,2,5],[1,3,6],[2,7],
    [5,8],[4,6,9],[2,5,7,10],[3,6,11],
    [4,9,12],[5,8,10,13],[6,9,11,14],[7,10,15],
    [8,13],[9,12,14],[10,13,15],[11,14]])

v = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def do():
    global v
    for i in range(len(v)):
        if len(trans[i]) == 0:
            continue
        curmax = -99999
        for a in trans[i]:
            curmax = max([curmax,v[a]-1])
        v[i] = curmax
    print(v)
        
