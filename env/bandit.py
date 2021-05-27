from typing import List
from numpy.random import binomial, normal


class Arm:
    """Class for a single bandit arm.

    """

    def __init__(self) -> None:
        """ Constructor method
        """
        self.pull_count = 0

    def pull(self) -> float:
        pass


class Bernoulli(Arm):
    def __init__(self, param: float):
        super().__init__()
        self.param = param

    def pull(self) -> float:
        return binomial(1, self.param)


class Normal(Arm):
    def __init__(self, mean, std_dev):
        super().__init__()
        self.mean = mean
        self.std_dev = std_dev

    def pull(self) -> float:
        return normal(self.mean, self.std_dev)


class Bandit:
    def __init__(self, arms: List):
        """Constructor method

        Parameters
        ----------
        arms: A collection of arms to pull/sample from
        strategy: Sampling strategy

        """
        self.arms = arms

    # to avoid direct modification of self.arms variable
    def get_arms(self):
        return self.arms

    def __len__(self):
        return len(self.arms)
