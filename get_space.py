# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:06:00 2020

@author: Keran Sivalingam
"""

import gym
from gym.spaces import *
import sys


def print_spaces(space):
    print(space)
    if isinstance(space, Box): 
        
        print("\n space.low: ", space.low)
        print("\n space.high: ", space.high)
        
if __name__ == "__main__":
    env = gym.make(sys.argv[1])
    print("Observation Space:")
    print_spaces(env.observation_space)
    
    print("Action Space:")
    print_spaces(env.action_space)
    
    try:
        print("Action descriptiion/meaning:",env.unwrapped.get_action_meanings())
    except AttributeError:
        pass