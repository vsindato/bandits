class Arm:
    def __init__(self, reward) -> None:
        self.reward = reward
        self.value = 0
        self.pull_count = 0

    def pull(self) -> float:
        reward = self.reward.sample()
        self.update_value(reward)
        return reward

    def update_value(self, reward: float) -> None:
        if self.pull_count > 0:
            self.value += self.value + \
                (1/self.pull_count) * (reward - self.value)
        else:
            self.value = reward

    def get_value(self) -> float:
        return self.value


class Bandit:
    def __init__(self, num_of_arms: int, strategy: str):
        self.arms = [Arm(Reward(np.random.randint(-2, 3), 1))
                     for i in range(num_of_arms)]
        self.num_of_arms = num_of_arms
        self.strategy = strategy

    # CHECKPOINT
    # TODO: Implement cases for different strategies
    def pull(self) -> float:
        if self.strategy.name == 'epsilon_greedy':
            pass
        # TODO: epsilon-greedy, boltzmann exploration, ucb, bayesian

        if np.random.randint(1, 11) <= 1:
            arm = self.arms[np.random.randint(0, self.num_of_arms)]
        else:
            arm = self.get_handle_with_max()
        return arm.pull()

    def get_handle_with_max(self):
        arms = sorted(self.arms, key=lambda handle: handle.value, reverse=True)
        return arms[0]

    def explore(self):
        pass
