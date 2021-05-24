import Reward from reward
from typing import List

# TODO: Define the Reward type to be enforced in Arm constructor


class Arm:
    """Class for a single bandit arm.

    """

    def __init__(self, reward_distribution: Reward) -> None:
        """ Constructor method

        Args:
          reward: Reward distribution
        """

        self.reward_distribution = reward_distribution
        self.pull_count = 0

    def pull(self) -> float:
        reward = self.reward_distribution.sample()
        return reward


class Bandit:
    def __init__(self, arms: List,):
        """Constructor method

        Parameters
        ----------
        arms: A collection of arms to pull/sample from
        strategy: Sampling strategy

        """
        self.arms = arms

    # TODO: Implement cases for different strategies
    def pick_and_pull(self) -> float:
        """Select and pull an arm based on strategy

        """
        # TODO: Implement this class as an interface / abstract class.
        #       interface=bandit; greedy_bandit: class greedy(bandit), randomized: class randomized(bandit)
        pass

    def __len__(self):
        return len(self.arms)


class Strategy:
    def __init__(self, bandit: Bandit):

    def step(self):
        pass
