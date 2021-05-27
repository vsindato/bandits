class Randomized(Strategy):
    # super-init (still not sure what this is)
    def epsilon_greedy(self, bandit, epsilon, horizon):
        self.name = 'epsilon_greedy'
        self.epsilon = epsilon
        x, y = [], []
        total_rewards = 0
        for step in range(1, horizon):
            total_rewards += bandit.pull()
            if step % 10 == 0:
                x.append(step)
                y.append(total_rewards/step)

        self.plot_results(x, y)
        return
