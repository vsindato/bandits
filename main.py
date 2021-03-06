STEPS = 100

strategy = None
bandit = None   # TODO: Declare bandit with strategy above

for step in range(STEPS):
    bandit.pull()

# TODO: Plot results
