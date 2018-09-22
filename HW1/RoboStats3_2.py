# Robo Stats Assignment 1

# Programing Nature (10 Points)

import numpy as np
import math
import random


# ---------------------------------------------  Classes  --------------------------------------------------
class Stochastic(object):
    '''
    This class generates a stochastic output (random output)
    In this assignment it is random binary output...

    Better to have binary 1, -1 scores rather than 0,1 because you
    have to multiply these predictions with weights, and multiplying 0 by
    anything is curry powder
    '''

    def __init__(self):
        # -1 = False,  1 = Win
        vals = [-1,1]
        self.output = random.choice(vals)



class Deterministic(object):
    '''
    This class generates a deterministic output

    The idea is to alternate between 1's and 0's each 2 iterations

    The method that I have decided to deploy generates output as follows:
    '''
    
    def __init__(self, index_of_val, timestep):
        # Every 2 cycles
        vals = [-1,1]
        #print (index_of_val)

        self.output = vals[index_of_val]
        #print (self.output)
        





class Adverserial(object):

    '''
    Here the nature gets to see the weight vector and prediction for each expert 
    '''
    def __init__(self, weight_vec, prediction_vec):
        self.weight = weight_vec
        self.pred = prediction_vec
        # The output of the adverserial example is one that goes
        # directly against (1 is -1 or -1 is 1) the most trusted expert
        # (ie: the expert with the highest weight designation in the weight vector
        max_weight = max(self.weight)
        index_max_weight = self.weight.index(max_weight)
        self.output = -1*self.pred[ index_max_weight ]
        




# ----------------------------------------  Running these  -------------------------------------------


    
# In order to run Stochastic
'''
x = Stochastic()
print (x.output)
'''

# In order to run deterministic
# -----------------------------------------------------------------------------
# Vector Index (v_index), element of vector index (e_index)
'''
v_index, e_index = 0, 0
while (True):
    x = Deterministic(v_index, e_index)
    print (x.output)
    v_index, e_index = x.increment(v_index, e_index)
'''

# In order to run Adverserial
'''
x = Adverserial( [3,5,2], [1,1,-1] )
print (x.output)
'''
