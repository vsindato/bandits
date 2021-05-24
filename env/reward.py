# replace these with imports from numpy
from distributions import gaussian, bernoulli


class Reward:
    """Class representing reward distribution

    Methods: sample

    """

    # TODO: Think of how to specify dist. in constructor?
    # TODO: how to prompt user to select from a limited set of distributions
    # TODO: Have options for users pre-specifying the input
    def __init__(self, distribution: str = "gaussian") -> None:
        """summary line

        """
        pass

    def sample(self) -> float:
        """ Sample a value from the specified reward distribution """

        return self.distribution.sample()
