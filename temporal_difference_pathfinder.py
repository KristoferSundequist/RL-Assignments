import numpy as np
import random as random

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

value = np.array([0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

start = 12
current = start

def step():
    global current
    global start
    global value
    
    if current == 0:
        current = random.randint(0,len(value)-1)
    else:
        nexts = random.randint(0,len(trans[current])-1)
        nexts = trans[current][nexts]
        value[current] += 1*(-1 + 0.9*value[nexts]-value[current])
        current = nexts

def doer(n):
    for i in range(n):
        step()
