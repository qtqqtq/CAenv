import gym
from CAworld import CAEnv
from stable_baselines3 import PPO

env=CAEnv(4)

model=PPO('MlpPolicy', env, verbose=1)
model.learn(10000)

observation= env.reset()

for _ in range(10):
    action, _state = model.predict(observation, deterministic=True)
    print(action)
    env.render()
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()

env.close()