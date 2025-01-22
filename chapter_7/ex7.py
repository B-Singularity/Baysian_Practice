import numpy as np
from empiricaldist import Pmf
from scipy.stats import binom
import matplotlib.pyplot as plt

def update_binomial(pmf, data):
    k, n = data
    xs = pmf.qs
    likelihood = binom.pmf(k, n, xs)
    pmf *= likelihood
    pmf.normalize()

# hypos = np.linspace(0, 1, 101)
# pmf = Pmf(1, hypos)
# data = 140, 250
# update_binomial(pmf, data)
# cumulative = pmf.cumsum()
#
# plt.figure(figsize=(8, 5))
# plt.plot(hypos, cumulative, label='Cumulative Distribution', color='blue')
# plt.title('Cumulative Distribution Function (CDF)')
# plt.xlabel('Probability (θ)')
# plt.ylabel('Cumulative Probability')
# plt.grid(True)
# plt.legend()
# plt.show()
