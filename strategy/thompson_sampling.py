from numpy.random import beta as beta_distribution
from strategy.base import Strategy

"""
Thompson sampling (Bernoulli bandit):
(K: number of actions, 
 theta_k: probability of +1 reward after pulling kth action
)
- Agent starts with independent prior beliefs over each theta_k 
- Assume priors are beta-distributed with parameters alpha and beta for each k
"""

# implementation
# how'll it fit with the rest of the module?
# structure
# strategy subclass

# pseudocode
# consider each arm's prior distribution of its mean reward (let it be beta)
# sample from each arm's distribution
# pull arm with largest sample value
# update the parameters of the distribution of the pulled arm (in the case of beta
# distribution, update alpha and beta)

# Thompson sampling on bernoulli bandits


class ThompsonSampler(Strategy):
    # super_initialize
    def __init__(self, bandit, prior_distribution="beta"):
        super().__init__(bandit)
        # assign priors to each of the arm
        self.bandit = bandit
        self.priors = [[1, 1]] * len(bandit)
        self.posteriors = self.priors[:]

    def reset(self):
        self.posteriors = self.priors[:]

    def step(self):
        samples = [beta_distribution(alpha, beta)
                   for alpha, beta in self.posteriors]
        samples_max = max(samples)
        samples_max_index = samples.index(samples_max)
        reward = self.bandit.get_arms()[samples_max_index].pull()
        alpha, beta = self.posteriors[samples_max_index]
        self.posteriors[samples_max_index] = [
            alpha + reward, beta + 1 - reward]

    def print_posteriors(self):
        print("Current posteriors: ", self.posteriors)

    def estimated_mean_reward(self):
        print([(a-1)/(a+b-2) for a, b in self.posteriors])
