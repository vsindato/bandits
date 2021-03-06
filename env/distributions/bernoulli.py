import numpy as np


class Bernoulli:
    """Bernoulli distribution

    TODO #1: explain the methods
    A bernoulli distribution, X ~ Bernoulli(p), is a distribution with 
    2 possible outcomes; a 0 ("failure") and 1("success").The parameter p
    represents the probability of "success".

    Methods
    -------
    #TODO: Explain the methods

    """

    def __init__(self, p: float) -> None:
        """Constructor method

        Parameters
        ----------
        p: probability of "success" i.e. outcome = 1
        """

        self.p = p

    def sample(self) -> int:
        """Sampling method

        Output
        ------
        A value of 0/1

        """

        return np.random.binomial(1, self.p)
