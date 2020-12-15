import numpy as np
import matplotlib.pyplot as plt

class Reward:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def sample(self):
        return np.random.normal(self.mean, self.std)


class Arm:
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

class Bandit:
    def __init__(self, num_of_arms, strategy):
        self.arms = [Arm(Reward(np.random.randint(-2,3), 1)) for i in range(num_of_arms)]
        self.num_of_arms = num_of_arms
        self.strategy = strategy

    ### CHECKPOINTTTT
    def pull(self):
        if self.strategy.name == 'epsilon_greedy':
            pass

        if np.random.randint(1,11) <= 1:
            handle = self.arms[np.random.randint(0,self.num_of_arms)]
        else:
            handle = self.get_handle_with_max()
        return handle.pull()

    def get_handle_with_max(self):
        arms = sorted(self.arms, key = lambda handle: handle.value, reverse=True)
        return arms[0]

    def explore(self):
        pass

class Strategy:
    def __init__(self):
        self.name = None

    def plot_results(self, x, y):
        plt.plot(np.array(x),np.array(y))
        plt.show()
        return

class Greedy(Strategy):
    # super-init (still not sure what this is)
    def greedy(self):
        self.name = 'greedy'

    def optimistic_initial_values(self):
        self.name = 'optimistic'

class Randomized(Strategy):
    # super-init (still not sure what this is)
    def epsilon_greedy(self, bandit, epsilon, num_of_pulls):
        self.name = 'epsilon_greedy'
        self.epsilon = epsilon
        x, y = [],[]
        total_rewards = 0
        for step in range(1,num_of_pulls):
            total_rewards += bandit.pull()
            if step%10 == 0:
                x.append(step)
                y.append(total_rewards/step)

        self.plot_results(x, y)
        return

    def bernoulli_exploration(self, temperature):
        self.name = 'bernoulli_exploration'
        self.temperature = temperature



if __name__ == '__main__':
    # Initialize bandit
    # Initialize strategy
