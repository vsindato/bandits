from env.bandit import Bernoulli, Normal, Bandit
from strategy.thompson_sampling import ThompsonSampler

number_of_arms = 5

# Setting reward distributions per arm (bernoulli)
bernoulli_params = [0.46, 0.54, 0.71, 0.32, 0.85]

# Setting reward distributions per arm (normal)
mean_reward_per_arm = [(2, 1), (3, 1), (4, 1), (6, 1), (8, 1)]

STEPS = 5000

strategy = 'TS'

arms = [Bernoulli(p) for p in bernoulli_params]
# arms = [Normal(mean, std_dev) for mean, std_dev in mean_reward_per_arm]
bandit = Bandit(arms)
sampler = ThompsonSampler(bandit)

for step in range(STEPS):
    sampler.step()
sampler.print_posteriors()
sampler.estimated_mean_reward()
