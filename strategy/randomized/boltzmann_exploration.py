def boltzmann_exploration(self, bandit, temperature):
    self.name = 'boltzmann_exploration'
    self.T = temperature

    # initialize payoff estimates per arm
    payoff_estimates_per_arm = {arm: 0 for arm in bandit.arms}
    normalizer = sum([pow(math.e, p/self.T)
                      for p in payoff_estimates_per_arm.values()])
    # calculate probabilities
    # select action based on probabilities
    choices([], [])
