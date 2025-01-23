import numpy as np
from empiricaldist import Pmf, Cdf
from scipy.stats import binom
import matplotlib.pyplot as plt
import pandas as pd

def update_binomial(pmf, data):
    k, n = data
    xs = pmf.qs
    likelihood = binom.pmf(k, n, xs)
    pmf *= likelihood
    pmf.normalize()

def make_die(sides):
    outcomes = np.arange(1, sides+1)
    die = Pmf(1/sides, outcomes)
    return die

def add_dist_seq(seq):
    total = seq[0]
    for other in seq[1:]:
        total = total.add_dist(other)
    return total


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


# # 6면체 주사위 3개에 대한 PMF 계산
# die = make_die(6)
# dice = [die] * 3
# pmf_3d6 = add_dist_seq(dice)
#
# n = 100000
# a = np.random.randint(1, 7, size=(n, 4))
# a.sort(axis=1)
# t = a[:, 1:].sum(axis=1)
# pmf_best3 = Pmf.from_seq(t)
# cdf_best3 = pmf_best3.make_cdf()
# cdf_max6 = Cdf(cdf_best3 ** 6)
#
# prob_gt = 1 - cdf_best3
# prob_gt6 = prob_gt**6
#
# prob_le6 = 1 - prob_gt6
# cdf_min6 = Cdf(prob_le6)
# cdf_min_dist6 =


# d4 = make_die(4)
# d6 = make_die(6)
# mix1 = (d4 + d6) / 2
# mix2 = (d4 + 2*d6) / 3
# total_damage = Pmf.add_dist(mix1, mix2)
#
# print(total_damage)
hypos = [4, 6, 8]
counts = [1, 2, 3]
pmf_dice = Pmf(counts, hypos)
pmf_dice.normalize()
dice = [make_die(sides) for sides in hypos]
df = pd.DataFrame(dice).fillna(0).transpose()
df *= pmf_dice.ps
print(df)
