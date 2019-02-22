# -*- coding: utf-8 -*-
import deepmind_lab
from pprint import pprint

env = deepmind_lab.Lab('nav_maze_static_01', [])
observation_spec = env.observation_spec()
action_spec = env.action_spec()
print('Observation spec:')
pprint(observation_spec)
print('Action spec:')
pprint(action_spec)