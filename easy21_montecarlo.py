import random as random
import numpy as np

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



player = random.randint(1,10)
comp = random.randint(1,10)

def init_game():
    global player
    global comp
    player = random.randint(1,10)
    comp = random.randint(1,10)
    
print("computer: " , comp , ", player: " , player)

def play(a):
    global player
    global comp
    
    a,b,reward,terminal = step(comp, player, a)
    comp = a
    player = b
    print("computer: " , comp , ", player: " , player , ", reward: " , reward , ", terminal: " , terminal)
    
############# MC
w,h = 22, 11;
action_values = [[[0,0] for x in range(w)] for y in range(h)]
states_actions_count = [[[0,0] for x in range(w)] for y in range(h)]
state_visited_count = [[0 for x in range(w)] for y in range(h)]


#returns: hit: 0 or stick:1 (0 or 1)
def pi(comp,player):
    Nzero = 100
    eps = Nzero/(Nzero + state_visited_count[comp][player])
    #get max
    maxa = 1
    if action_values[comp][player][0] > action_values[comp][player][1]:
        maxa = 0
    if action_values[comp][player][0] == action_values[comp][player][1]:
        maxa = random.randint(0,1)

    r = random.uniform(0,1)
    if r > eps/2:
        return maxa
    else:
        if maxa == 0:
            return 1
        else:
            return 0
        
def pi2(a,b):
    return random.randint(0,1)

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

def upgrade(episode):
    global action_values
    global states_actions_count
    global states_visited_count
    
    state_actions, reward = episode
    for sa in state_actions:
        state_visited_count[sa[0]][sa[1]] += 1
        states_actions_count[sa[0]][sa[1]][sa[2]] += 1
        action_values[sa[0]][sa[1]][sa[2]] += (1/states_actions_count[sa[0]][sa[1]][sa[2]])*(reward - action_values[sa[0]][sa[1]][sa[2]])
    
def learn(n_eps):
    for i in range(n_eps):
        e = episode(pi)
        upgrade(e)

def eval(n_eps, pi):
    total_reward = 0
    for i in range(n_eps):
        _, reward = episode(pi)
        total_reward += reward
    return total_reward/n_eps

    


