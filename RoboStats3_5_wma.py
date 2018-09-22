# Robot Stats Assignment 1

# Implementing the Weighted Majority Algorithm (15 Points)


# For importing the classes
import RoboStats3_2
import matplotlib.pyplot as plt
import time
import random

# ------------------- Main Code ------------------


# Will take in as arguements: nat, eta, T where T = number of trials and eta is the penalty parameter
def WMA(nat, eta, T):


    # Initialize the following:
    # - Weight vector with 1 (all weights = 1 before learning starts)
    # - Initialize learner loss vector with 0s (losses by the learner from weighted consideration of experts)
    # - Initialize expert loss vector with 0s (losses for all experts = 0 before learning starts)
    weights = [1,1,1,1]
    losses_learner = [0] * T  
    losses_expert = [[0,0,0,0] for i in range(0, T, 1)] 
    v = 0   # This is used for deterministic outputs, refer to the Deterministic class in 3_2


    # Initialize the cumulative sum of loss for learner and each individual expert
    sum_learner = 0
    sum_expert = [0,0,0,0]

    
    # 4. for t = 1,...,T do:
    for t in range(T):

        # 5. Receive expert advice (x(t) -> {-1,1}^N where N is the number of experts)
        # expert 1 is a die-hard fan for Tartan's sports team and always says win;
        # expert 2 is pessimistic and always says lose; 
        # expert 3 predicts Tartan will lose for odd-number matches and will win for even-number matches.
        expert_3 = 0
        if (t % 2 == 0):    expert_3 = 1
        else:               expert_3 = -1
        weather = random.choice(['sunny','rainy'])
        if (weather == 'sunny'):    expert_4 = 1
        else:                       expert_4 = -1
        x = [1,-1, expert_3, expert_4]
        if (t % 3 == 0):    v = 0
        else:               v = 1
        print (v)

        # 6. estimate output = sign(sum(N,n=1(xn(t)*()wn(t-1))))
        # obtain the sign of this sum (is it positive, or negative? that is the output)
        Sum = 0
        y_ = 0       
        for n in range(0, 4, 1):        # for all experts (there are 4)
            Sum +=  x[n] * weights[n]
        if (Sum < 0):   y_ = -1
        if (Sum > 0):   y_ = 1


        # 7. Receive y(t)
        y_style = 0
        if nat is 's':  y_style = RoboStats3_2.Stochastic()
        if nat is 'd':  y_style = RoboStats3_2.Deterministic(v, t)
        if nat is 'a':  y_style = RoboStats3_2.Adverserial(weights,x)
        y = y_style.output
            

        # 8. wn^(t+1)=wn^(t) * (1-eta*(y^t != xn^(t) )) for all n
        # Calculate the cumulative loss of expert and learner
        for n in range(0, 4, 1):
            val, powder = 0, 0
            if (y != x[n]):     val = 1
            if (y == x[n]):     val = 0
            weights[n] = weights[n] * ( 1 - eta*(val) )
            sum_expert[n] +=  1*val
            losses_expert[t][n] = sum_expert[n]
        if (y_ != y):     powder = 1
        if (y_ == y):     powder = 0
        sum_learner += 1 * powder 
        losses_learner[t] = sum_learner


    # Plot all of these
    #plt.ion()
    plt.figure(1)
    title = ' '
    if (nat == 's'):    title = 'Stochastic'
    if (nat == 'd'):    title = 'Deterministic'
    if (nat == 'a'):    title = 'Adverserial'
    plt.title(title)
    plt.xlabel('Timestep')
    plt.ylabel('Losses')
    loss_exp = losses_expert[0:T]
    exp1 = [j[0] for j in loss_exp]
    exp2 = [j[1] for j in loss_exp]
    exp3 = [j[2] for j in loss_exp]
    exp4 = [j[3] for j in loss_exp]
    plt.plot(  exp1,'b',  label = 'expert1')
    plt.plot(  exp2,'g',  label = 'expert2')
    plt.plot(  exp3,'r',  label = 'expert3')
    plt.plot(  exp4,'m',  label = 'expert4')
    plt.plot(  losses_learner,'y', label = 'loss of learner' )
    plt.legend(loc = 'upper left')
    plt.pause(4)
    
    plt.figure(2)
    title = ' '
    if (nat == 's'):    title = 'Stochastic'
    if (nat == 'd'):    title = 'Deterministic'
    if (nat == 'a'):    title = 'Adverserial'
    plt.title(title)
    plt.xlabel('Timestep')
    plt.ylabel('Regret')
    regret = [0] * T
    # Find who the biggest expert is (smallest loss)
    most_expert = [min(loss) for loss in losses_expert]
    #print (losses_expert)
    for t in range(0,T,1):
        #print (T)
        #print (len(losses_expert))
        #print (losses_expert[t])
        #print (most_expert[t])
        # average regret
        regret[t] = (float(losses_learner[t] - most_expert[t])/(t+1) )

    plt.plot(regret,'r')
    plt.pause(4)


#wma = WMA('a', 0.1, 100)
wma = WMA('d', 0.1, 100)
#wma = WMA('s', 0.1, 100)
