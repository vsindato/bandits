import numpy as np
import matplotlib.pyplot as plt

class Reward:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def sample(self):
        return np.random.normal(self.mean, self.std)


class Handle:
    def __init__(self, reward):
        self.reward = reward
        self.value = 0
        self.pull_count = 0

    def pull(self):
        reward = self.reward.sample()
        self.update_value(reward)
        return reward

    def update_value(self, reward):
        if self.pull_count > 0:
            self.value += self.value + (1/self.pull_count) * (reward - self.value)
        else:
            self.value = reward

class SlotMachine:
    def __init__(self, num_of_handles):
        self.handles = [Handle(Reward(np.random.randint(-2,3), 1)) for i in range(num_of_handles)]
        self.num_of_handles = num_of_handles

    def pull(self, epsilon=None):
        if np.random.randint(1,11) <= 1:
            handle = self.handles[np.random.randint(0,self.num_of_handles)]
        else:
            handle = self.get_handle_with_max()
        return handle.pull()

    def get_handle_with_max(self):
        handles = sorted(self.handles, key = lambda handle: handle.value, reverse=True)
        return handles[0]

    def explore(self):
        pass

if __name__ == '__main__':
    machine = SlotMachine(10)
    epsilon = None
    x, y = [],[]
    num_steps = 1000
    total_rewards = 0

    for step in range(1,num_steps):
        total_rewards += machine.pull()
        if step%10 == 0:
            x.append(step)
            y.append(total_rewards/step)

    plt.plot(np.array(x),np.array(y))
    plt.show()
