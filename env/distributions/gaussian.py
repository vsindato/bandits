import numpy as np
from math import sqrt


class Gaussian:
    """Gaussian distribution type

    TODO #1: define gaussian
         #2: explain the methods
    """

    def __init__(self, mean: float, variance: float) -> None:
        """Constructor method

        Parameters
        ----------
        mean:
        variance: 
        """

        self.mean = mean
        self.variance = variance
        self.standard_deviation = sqrt(variance)

    def sample(self):
        """summary

        """

        return np.random.normal(self.mean, self.standard_deviation)
