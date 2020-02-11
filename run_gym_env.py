# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:16:14 2020

@author: Keran Sivalingam
"""

import gym
import sys

def run_gym_env():
    env = gym.make('Alien-ram-v0')

    env.reset()
    for _ in range(2000):
        env.render()
        env.step(env.action_space.sample())
        
    env.close()
    


if __name__ == "__main__":
        run_gym_env()