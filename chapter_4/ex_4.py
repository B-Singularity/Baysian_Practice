import numpy as np
import pandas as pd
from scipy.stats import beta
import matplotlib.pyplot as plt

# Step 1: Define the range of possible p values
hypos = np.linspace(0, 1, 101)

# Step 2: Define the prior (uniform distribution)
prior = pd.Series(1, index=hypos)

# Step 3: Define the likelihood function
def likelihood(p, heads, tails):
    return (0.5 + 0.5 * p)**heads * (0.5 - 0.5 * p)**tails

# Step 4: Update with data
heads = 80
tails = 20
likelihoods = [likelihood(p, heads, tails) for p in hypos]

# Step 5: Compute posterior
posterior = prior * likelihoods
posterior /= posterior.sum()

# Step 6: Plot the posterior distribution
posterior.plot(label='Posterior')
plt.xlabel('Proportion of people who cheat on taxes')
plt.ylabel('Probability')
plt.legend()
plt.show()

# Step 7: Find the MAP (Most Likely Value)
map_estimate = posterior.idxmax()
print(f"The most likely proportion of cheaters: {map_estimate:.2f}")