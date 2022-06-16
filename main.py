import gym
from CAenv.CAenv.envs.CAworld import CAEnv
from stable_baselines3 import A2C

env =CAEnv(3)

model=A2C('MultiInputPolicy', env, verbose=1)
model.learn(100000)

observation= env.reset()

for _ in range(1000):
    action, _state = model.predict(observation, deterministic=True)
    observation, reward, done, info = env.step(action)
    env.render()
    if done:
        observation = env.reset()

env.close()