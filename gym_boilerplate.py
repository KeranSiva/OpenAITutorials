# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:41:05 2020

@author: Keran Sivalingam
"""

import gym

env = gym.make("Qbert-v0")
MAX_NUM_EPISODES = 10
MAX_STEPS_PER_EPISODE = 500

for episode in range(MAX_NUM_EPISODES):
    
    obs = env.reset() #Initial Environment
    
    for step in range(MAX_STEPS_PER_EPISODE):
        env.render()
        action = env.action_space.sample()
        next_state, reward, done, info = env.step(action)
        obs = next_state
        
        if done is True:
            
            print("\n Episode #{} ended in {} steps.".format(episode,step+1))
            break