class Greedy(Strategy):
    # 1. super-init (still not sure what this is)
    # 2. set name
    def run():
    """
    Args: bandit, timesteps
    Output:
    """
      # sample all actions once
      arm_values = []
       for arm in bandit.get_arms():
            arm_values.append(arm, arm.pull())

        for t in range(timesteps):
            _ = sorted(arm_values, key=lambda pair: pair[1], reverse=True)
            greedy_arm, greedy_value = _[0]
            reward = greedy_arm.pull()
            new_value = greedy_arm.get_value()
            _[0][1] = new_value

        return

        # consistently select the action with highest estimated reward
