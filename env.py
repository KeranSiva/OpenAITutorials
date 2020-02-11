# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:23:59 2020

@author: Keran Sivalingam
"""

from gym import envs
env_names = sorted([spec.id for spec in envs.registry.all()])
env_name = env_names[0:100]
for name in sorted(env_name):
    print(name)