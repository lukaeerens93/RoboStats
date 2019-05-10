#!/usr/bin/python
# 16-831 Spring 2018
# Project 4
# RL questions:
# Fill in the various functions in this file for Q3.2 on the project.

import numpy as np
import gridworld 

def value_iteration(env, gamma, max_iterations=int(1e3), tol=1e-3):
  """
  Q3.2.1
  This implements value iteration for learning a policy given an environment.

  Inputs:
    env: environment.DiscreteEnvironment (likely gridworld.GridWorld)
      The environment to perform value iteration on.
      Must have data members: nS, nA, and P
    gamma: float
      Discount factor, must be in range [0, 1)
    max_iterations: int
      The maximum number of iterations to run before stopping.
    tol: float
      Tolerance used for stopping criterion based on convergence.
      If the values are changing by less than tol, you should exit.

  Output:
    (numpy.ndarray, iteration)
    value_function:  Optimal value function
    iteration: number of iterations it took to converge.
  """

  ## YOUR CODE HERE ##
  #raise NotImplementedError()
  iteration = 0
  value_func_prime = np.zeros( (env.nS, 2) )
  while True:
      state_values = np.zeros( (env.nS, 2) )
      iteration += 1
      delta = 0

      for s in range(env.nS):
          placeholder_val = value_func_prime[s][0]
          rewardM = -1

          for a in range(env.nA):
              value = 0
              state_transition_prob_matrix = env.P[s][a]
              
              for prob, state_next, reward, end in state_transition_prob_matrix:
                  if end == True:
                      value += prob * reward
                  else:
                      value += prob * (reward + gamma * value_func_prime[state_next][0])

              if value > rewardM:
                  state_values[s][0] = value
                  rewardM = value
          delta_prime = abs(placeholder_val - state_values[s][0])
          delta = max(delta, delta_prime)
      value_func_prime = state_values
      if delta < tol or iteration > max_iterations:
          break
  return state_values, iteration


def policy_from_value_function(env, value_function, gamma):
  """
  Q3.2.1/Q3.2.2
  This generates a policy given a value function.
  Useful for generating a policy given an optimal value function from value
  iteration.

  Inputs:
    env: environment.DiscreteEnvironment (likely gridworld.GridWorld)
      The environment to perform value iteration on.
      Must have data members: nS, nA, and P
    value_function: numpy.ndarray
      Optimal value function array of length nS
    gamma: float
      Discount factor, must be in range [0, 1)

  Output:
    numpy.ndarray
    policy: Array of integers where each element is the optimal action to take
      from the state corresponding to that index.
  """

  ## YOUR CODE HERE ##    
  #raise NotImplementedError()
  policy = np.zeros(env.nS,dtype = 'int')
  for s in range(env.nS):
      value_max = -1
      for a in range(env.nA):
          value = 0
          state_transition_prob_matrix = env.P[s][a]
          for prob, state_next, reward, end in state_transition_prob_matrix:
              if end == True:
                  value += prob * reward
              else:
                  value += prob * (reward + gamma * value_function[state_next][0])
          if value >= value_max:
              policy[s] = a
              value_max = value
  return policy


def graph(val, key):
    fig, axis = plt.subplots()
    graph_plot = np.reshape(val, (8, 8) )
    im = axis.imshow(graph_plot)
    for i in range(len(graph_plot)):
        for j in range(len(graph_plot)):
            text = axis.text(j, i, round(graph_plot[i, j], 2), ha="center", va="center", color="w")
    if (key == 1): plt.title('val_fn')
    if (key == 2): plt.title('policy')
    if (key == 3): plt.title('val_fn_3.2.2')
    if (key == 4): plt.title('policy_3.2.2')
    if (key == 5): plt.title('TD(0)')
    plt.show()


def policy_iteration(env, gamma, max_iterations=int(1e3), tol=1e-3):
  """
  Q3.2.2: BONUS
  This implements policy iteration for learning a policy given an environment.

  You should potentially implement two functions "evaluate_policy" and 
  "improve_policy" which are called as subroutines for this.

  Inputs:
    env: environment.DiscreteEnvironment (likely gridworld.GridWorld)
      The environment to perform value iteration on.
      Must have data members: nS, nA, and P
    gamma: float
      Discount factor, must be in range [0, 1)
    max_iterations: int
      The maximum number of iterations to run before stopping.
    tol: float
      Tolerance used for stopping criterion based on convergence.
      If the values are changing by less than tol, you should exit.

  Output:
    (numpy.ndarray, iteration)
    value_function:  Optimal value function
    iteration: number of iterations it took to converge.
  """

  ## BONUS QUESTION ##
  ## YOUR CODE HERE ##
  
  v, p = 0, 0
  policy = np.zeros(env.nS, dtype='int')
  state_values = np.zeros(env.nS)

  while True:
      value_func_prime = np.zeros(env.nS)
      iteration = 0
      kk = 0
      while True:
          state_values = np.zeros(env.nS)
          iteration += 1
          deta = 0
          
          for s in range(env.nS):
              placeholder_val = value_func_prime[s]
              a = policy[s]
              value = 0
              for prob, state_next, reward, end in env.P[s][a]:
                  #print (state_next)
                  #print (value_func_prime[state_next])
                  if (end == True): value += prob * reward
                  else:             value += prob * (reward + gamma * state_values[state_next])
              state_values[s] = value
              delta_prime = abs(state_values[s] - placeholder_val)
              deta = max(deta, delta_prime)
          
          value_func_prime = state_values
          if deta < tol or iteration > max_iterations:
              break
      b = 0
      better = False
      #better_policy = policy_from_value_function(env, state_values, gamma)
      policy_ = np.zeros(env.nS,dtype = 'int')
      for s in range(env.nS):
        value_max = -1
        for a in range(env.nA):
            value = 0
            state_transition_prob_matrix = env.P[s][a]
            for prob, state_next, reward, end in state_transition_prob_matrix:
                if end == True:
                    value += prob * reward
                else:
                    value += prob * (reward + gamma * state_values[state_next])
            if value >= value_max:
                policy_[s] = a
                value_max = value

      for s in range(env.nS):
          if policy[s] != policy_[s]:
              better = True
              b += 1
              break
      if (b > max_iterations):
          kk = abs(max_iterations - b)
      p += 1
      policy = policy_
      v += iteration
      if (not better) or p > max_iterations:
          break
  print ('V iteration: ' + str(v))
  print ('P iteration: ' + str(p))
  return state_values, policy


def td_zero(env, gamma, policy, alpha):
  """
  Q3.2.2
  This implements TD(0) for calculating the value function given a policy.

  Inputs:
    env: environment.DiscreteEnvironment (likely gridworld.GridWorld)
      The environment to perform value iteration on.
      Must have data members: nS, nA, and P
    gamma: float
      Discount factor, must be in range [0, 1)
    policy: numpy.ndarray
      Array of integers where each element is the optimal action to take
      from the state corresponding to that index.
    alpha: float
      Learning rate/step size for the temporal difference update.

  Output:
    numpy.ndarray
    value_function:  Policy value function
  """

  ## YOUR CODE HERE ##
  delta=2*1e-5
  value = np.zeros( (env.nS, 1) )
  for t in range(1000):
      delta = 0
      old_value = np.zeros( (env.nS, 1) )

      for s in range(env.nS):
          a = policy[s]

          for prob, state_next, reward, end in env.P[s][a]:
              value[s] += prob * alpha*(reward + gamma * value[state_next][0] - value[s][0])
          delta_prime = np.abs(old_value[s][0] - value[s][0])
          delta = np.maximum(delta, delta_prime)

      if (delta < 1e-3):
          break    
  return value

def n_step_td(env, gamma, policy, alpha, n):
  """
  Q3.2.4: BONUS
  This implements n-step TD for calculating the value function given a policy.

  Inputs:
    env: environment.DiscreteEnvironment (likely gridworld.GridWorld)
      The environment to perform value iteration on.
      Must have data members: nS, nA, and P
    gamma: float
      Discount factor, must be in range [0, 1)
    policy: numpy.ndarray
      Array of integers where each element is the optimal action to take
      from the state corresponding to that index.
    n: int
      Number of future steps for calculating the return from a state.
    alpha: float
      Learning rate/step size for the temporal difference update.

  Output:
    numpy.ndarray
    value_function:  Policy value function
  """

  ## BONUS QUESTION ##
  ## YOUR CODE HERE ##
  raise NotImplementedError()

if __name__ == "__main__":
  env = gridworld.GridWorld(map_name='8x8')

  # Play around with these values if you want!
  gamma = 0.9
  alpha = 0.05
  n = 10
  
  # Q3.2.1
  V_vi, n_iter = value_iteration(env, gamma)
  policy = policy_from_value_function(env, V_vi, gamma)
  print (n_iter)

  from matplotlib import pyplot as plt
  graph(V_vi[:, 0], 1)
  graph(policy,     2)


  # Q3.2.2: BONUS
  V_pi, policy2 = policy_iteration(env, gamma)
  graph(V_pi,  3)
  graph(policy2,     4)

  # Q3.2.3
  V_td = td_zero(env, gamma, policy, alpha)
  graph(V_td, 5)

  # Q3.2.4: BONUS
  # V_ntd = n_step_td(env, gamma, policy, alpha, n)