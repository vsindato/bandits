from numpy.random import beta as beta_distribution


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


class ThompsonSampling(Strategy):
    # super_initialize
    def __init__(self, bandit, prior_distribution="beta"):
        super().__init__()
        # assign priors to each of the arms
        # can you directly access the variables declared via super_init in init?
        self.priors = [[1, 1]] * len(bandit)
        self.posteriors = self.priors[:]

    def step(self):
        samples = [beta_distribution(alpha, beta)
                   for alpha, beta in self.priors]
        samples_max, samples_max_index = max(
            samples), samples.index(max(samples))
        reward = bandit.arms[samples_max_index].pull()
        alpha, beta = self.posteriors[samples_max_index]
        self.posteriors[samples_max_index] = [
            alpha + reward, beta + 1 - reward]
