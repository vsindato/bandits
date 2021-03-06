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

        self.reward = reward
        self.value = 0
        self.pull_count = 0

    def pull(self) -> float:
        reward = self.reward.sample()
        self.update_value(reward)
        return reward

    def update_value(self, reward: float) -> None:
        """Update current value estimate of arm instance

        # TODO: Expl. of incremental updates

        Parameters
        ----------
        reward: observed reward.


        """
        step_size = 1/self.pull_count if self.pull_count else 1
        self.value += self.value + step_size * (reward - self.value)

    def get_value(self) -> float:
        return self.value


class Bandit:
    def __init__(self, arms: List, strategy: str):
        """Constructor method

        Parameters
        ----------
        arms: A collection of arms to pull/sample from
        strategy: Sampling strategy

        """
        self.arms = arms
        self.strategy = strategy

    # TODO: Implement cases for different strategies
    def pick_and_pull(self) -> float:
        """Select and pull an arm based on strategy

        """
        # TODO: Implement this class as an interface / abstract class.
        #       interface=bandit; greedy_bandit: class greedy(bandit), randomized: class randomized(bandit)
        pass

    def get_max_arm(self):
        """Return arm with highest estimated value

        """

    def explore(self):
        pass
