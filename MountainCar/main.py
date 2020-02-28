# -*- coding: utf-8 -*-
"""
@author: Keran Sivalingam
"""

import gym



# GLOBAL Parameter
MAX_NUM_EPISODES = 50000
STEPS_PER_EPISODES = 200
max_num_Steps = MAX_NUM_EPISODES * STEPS_PER_EPISODES
EPSILON_MIN = 0.005
EPSILON_DECAY = 500 * EPSILON_MIN/max_num_Steps
ALPHA = 0.95
GAMMA = 0.98
NUM_DISCRETE_BINS = 30


class Q_Learner(object):
    def __init__(self, env):
        self.obs_shape = env.observation_space.shape
        self.obs_high = env.observation_space.high
        self.obs_low = env.observation_space.los
        self.obs_bins = NUM_DISCRETE_BINS
        self.bin_width = (self.obs_high - self.obs_low)/self.obs_bins
        self.action_shape = env.action_space.n
        self.Q = np.zeros((self.obs_bins + 1, self.obs_bins + 1, self.action_shape))
















env = gym.make("MountainCar-v0")
MAX_NUM_EPISODES = 500

for episode in range(MAX_NUM_EPISODES):
    done = False
    obs = env.reset() #Initial Environment
    total_reward = 0.0
    step = 0
    
    while not done:
        env.render()
        action = env.action_space.sample()
        next_state, reward, done, info = env.step(action)
        
        total_reward += reward
        step += 1
        obs = next_state
        
    print("\n Episode #{} ended in {} steps. total_reward = {}".format(episode, step+1, total_reward))
env.close()