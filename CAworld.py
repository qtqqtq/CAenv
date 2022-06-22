import gym
from gym import spaces
import pygame
import numpy as np
import CAmodel


class CAEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, size=5):
        self.size = size  # The size of the square grid
        self.CA=CAmodel.CAmodel(size)
        self.observation_space = spaces.Box(0,1,shape=(size,size),dtype=int)
        self.action_space = spaces.MultiDiscrete([size,size])



    def reset(self, seed=None, return_info=False, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)
        return self.CA.matrix

    def step(self, action):
        info = {}
        self.CA.matrix[action[0]][action[1]]=1
        self.CA.next_state()
        observation=self.CA.matrix
        reward=self.CA.matrix.count(1)
        if reward>=self.size*self.size:
            done=True
        else:done=False
        return observation, reward, done ,info

    def render(self, mode="human"):
        self.CA.print_list()


