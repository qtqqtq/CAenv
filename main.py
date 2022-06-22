import gym
from CAworld import CAEnv
from stable_baselines3 import A2C

env =CAEnv(4)

model=A2C('MlpPolicy', env, verbose=1)
model.learn(100000)

observation= env.reset()

for _ in range(10):
    action, _state = model.predict(observation, deterministic=True)
    print(action)
    env.render()
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()

env.close()