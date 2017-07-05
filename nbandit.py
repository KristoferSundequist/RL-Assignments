import random
import numpy as np



rewards = [0]*10;
for i in range(len(rewards)):
    rewards[i] = np.random.normal(0,1)

#[(sum,count)]
values = [(0,0)]*len(rewards)
v = [0]*len(rewards)
choices = [0]*len(rewards)

#for i in range(len(v)):
 #   v[i] = random.uniform(min(rewards), max(rewards))


correct = 0


def do_action(n):
    global correct
    r = rewards[n] + np.random.normal(0,1)
    values[n] = (values[n][0]+r, values[n][1]+1)
    #v[n] = values[n][0]/values[n][1]
    #v[n] = v[n] + (1/values[n][1])*(r - v[n])
    v[n] = v[n] + 0.1*(r - v[n])
    choices[n] += 1
    if n == rewards.index(max(rewards)):
        correct += 1
    for i in range(len(rewards)):
        rewards[i] += np.random.normal(0,0.1)
        
def choose_action(eps):
    dice = random.uniform(0,1)
    n = 0
    if dice > eps:
        n = v.index(max(v))
    else:
        n = int(round(random.uniform(0,len(v)-1)))
        
    do_action(n)

def do_n(n,eps):
    for i in range(n):
        choose_action(eps)

def get_total_reward():
    s = 0
    for i in range(len(rewards)):
        s += choices[i]*rewards[i]

    return s/sum(choices)
    
    

