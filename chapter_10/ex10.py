from empiricaldist import Pmf
from collections import Counter
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def update(pmf, data):
    pmf *= likelihood[data]
    pmf.normalize()

def choose(beliefs):
    ps = [b.choice() for b in beliefs]
    return np.argmax(ps)




def play(i, actual_probs):

    counter[i] += 1
    p = actual_probs[i]
    if np.random.random() < p:
        return 'W'
    else:
        return 'L'

def choose_play_update(beliefs):
    machine = choose(beliefs)
    outcome = play(machine, [0.1, 0.2, 0.3, 0.4])
    update(beliefs[machine], outcome)


def plot(distributions):

    plt.figure(figsize=(10, 5))
    plt.plot(distributions.index, distributions.values, color='black')
    plt.xlabel('x')
    plt.ylabel('probability')
    plt.legend()
    plt.grid(True)
    plt.show()


# xs = np.linspace(0, 1, 101)
# uniform = Pmf(1, xs)
#
# k,n = 140, 250
# likelihood = binom.pmf(k, n, xs)
#
# posterior = uniform * likelihood
# posterior.normalize()
# print(posterior.mean(), posterior.credible_interval(0.9))
# plt.figure(figsize=(10, 5))
# plt.plot(posterior.index, posterior.values, color='black')
# plt.xlabel('x')
# plt.ylabel('probability')
# plt.legend()
# plt.show()

# xs = np.linspace(0 ,1, 101)
# prior = Pmf(1, xs)
# prior.normalize()
# beliefs = [prior.copy() for i in range(4)]
# counter = Counter()
# #
# likelihood = {
#     'W': xs,
#     'L': 1 - xs
# }
#
# bandit = prior.copy()
#
# for outcome in 'WLLLLLLL':
#     update(bandit, outcome)
#
# plot(bandit)
#
# samples = np.array([b.choice(1000)] for b in beliefs)
# indices = np.argmax(samples, axis=0)
# pmf = Pmf.from_seq(indices)
# print(choose(beliefs))

# num_plays = 100
#
# for i in range(num_plays):
#     choose_play_update(beliefs)

