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

value = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
visitedtotal = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
visitednow = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
curreward = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

start = 12
current = start
reward = 0
#newmean = oldmean + (oldmean-newvalue)/visited

def step():
    global current
    global start
    global visitednow
    global reward
    global visitedtotal
    global value
    global curreward
    
    if current == 0 or current == 15:
        #print("epoch")
        #current = random.randint(1,15)
        current = start
        visitedtotal += visitednow
        for i in range(len(value)):
            if visitedtotal[i] > 0:
                value[i] += ((reward-curreward[i]) - value[i])/visitedtotal[i]
        curreward = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        visitednow = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        reward = 0
    else:
        reward -= 1
        if visitednow[current] == 0:
            visitednow[current] += 1
            curreward[current] += reward
        nexts = random.randint(0,len(trans[current])-1)
        current = trans[current][nexts]

def doer(n):
    for i in range(n):
        step()
