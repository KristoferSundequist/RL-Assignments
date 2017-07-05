import random as random
import numpy as np

###############
# ENVIRONMENT #
###############

def draw():
    card = random.randint(1,10)
    color = random.randint(1,3)
    if color == 1:
        return card*(-1)
    return card

def bust(n):
    if n > 21 or n < 1:
        return True
    return False

#returns (dealer, player, reward, bool: terminal)
#action 1 == stick ( 0 == hit)
def step(dealer, player_sum, action):
    if action == 1:
        while dealer < 17 and dealer > 0:
            dealer += draw()
        if bust(dealer):
            return dealer, player_sum, 1, True
        elif dealer > player_sum:
            return dealer, player_sum, -1, True
        elif dealer < player_sum:
            return dealer, player_sum, 1, True
        else:
            return dealer, player_sum, 0, True
            
        
    else:
        player_sum += draw()
        if bust(player_sum):
            return dealer, player_sum, -1, True
        else:
            return dealer, player_sum, 0, False

#########
# SARSA #
#########


weights = np.random.randn(36)

#map state to feature vector
def mapping(comp, player, action):
    c = []
    features = []
    
    #comp
    if 1 <= comp <= 4:
        c.append(0)

    if 4 <= comp <= 7:
        c.append(1)

    if 7 <= comp <= 10:
        c.append(2)

    for cs in c:
        player_intervals = []
        if 1 <= player <= 6:
            player_intervals.append(0)
            
        if 4 <= player <= 9:
            player_intervals.append(1)

        if 7 <= player <= 12:
            player_intervals.append(2)

        if 10 <= player <= 15:
            player_intervals.append(3)

        if 13 <= player <= 18:
            player_intervals.append(4)

        if 16 <= player <= 21:
            player_intervals.append(5)

        for ps in player_intervals:
            #on_comp #ps #action
            comp_offset = (cs*12)
            p_offset = (ps*2)
            features.append(comp_offset + p_offset + action)


    v = np.zeros(36)
    for f in features:
        v[f] = 1
    return v
    
#epsilon-greedy pi
#returns: hit: 0 or stick:1 (0 or 1)
def pi(comp,player):
    global weights
    eps = 0.05
    maxa = 1
    azero = np.dot(mapping(comp,player,0),weights)
    aone = np.dot(mapping(comp,player,1),weights)
    if azero > aone:
        maxa = 0
    if azero == aone:
        maxa = random.randint(0,1)

    r = random.uniform(0,1)
    if r > eps:
        return maxa
    else:
        if maxa == 0:
            return 1
        else:
            return 0
        
#returns an episode using pi
def episode(pi):
    #state
    comp = random.randint(1,10)
    player = random.randint(1,10)
    episode_log = []
    terminal = False
    reward = 0
    
    #do actions
    while terminal == False:
        a = pi(comp, player)
        newcomp,newplayer,reward,terminal = step(comp, player, a)
        episode_log.append([comp,player,a])
        comp = newcomp
        player = newplayer
        #print("computer: " , comp , ", player: " , player , ", reward: " , reward , ", terminal: " , terminal)

    return episode_log, reward

#upgrade pi on episode with sarsa(lambda)
def upgrade(episode,lambda_sarsa):
    global weights
    E = np.zeros(36)
    alpha = 0.01
    state_actions, reward = episode
    for i in range(len(state_actions)):
        sa = state_actions[i]
        sav = mapping(sa[0],sa[1],sa[2])
        
        delta = 0
        if i == len(state_actions)-1:
            delta = reward - np.dot(sav,weights)
        else:
            next_sa = state_actions[i+1]
            delta = np.dot(mapping(next_sa[0],next_sa[1],next_sa[2]),weights) - np.dot(sav,weights)

        delta *= sav
        
        E = lambda_sarsa*E + sav
        weights += alpha*delta*E

#learn pi on n_eps episodes with sarsa(lambda)      
def learn(n_eps,lambda_sarsa):
    for i in range(n_eps):
        e = episode(pi)
        upgrade(e,lambda_sarsa)

#random stategy
def pi2(a,b):
    return random.randint(0,1)

#eval a strategy on n_eps episodes
def eval(n_eps, pi):
    total_reward = 0
    for i in range(n_eps):
        _, reward = episode(pi)
        total_reward += reward
    return total_reward/n_eps

    


