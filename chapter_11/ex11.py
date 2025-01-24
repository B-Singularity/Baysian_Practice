from scipy.stats import norm
from empiricaldist import Pmf
import numpy as np
import pandas as pd
import sys
sys.path.append(r"C:\Users\SSAFY\Downloads\sung\Baysian_Practice")
from utils.plot import plot


def make_joint(pmf1, pmf2):
    X, Y = np.meshgrid(pmf1, pmf2)
    return pd.DataFrame(X * Y, columns=pmf1.qs, index=pmf2.qs)

def normalize(joint):
    prob_data = joint.to_numpy().sum()
    joint /= prob_data
    return prob_data

def marginal(joint, axis):
    return Pmf(joint.sum(axis=axis))

# def plot_joint(joint, cmap='Blues'):
#     vmax = joint.to_numpy().max() * 1.1
#     plt.pcolormesh(joint.columns, joint.index, joint,
#                    cmap=cmap,
#                    vmax=vmax,
#                    shading='nearest')
#     plt.colorbar()




# x, y = [1, 3, 5], [2, 4]
# X, Y = np.meshgrid(x, y)
# df = pd.DataFrame(X * Y, columns=x, index=y)
# print(X > Y)

mean = 178
qs = np.arange(mean-24, mean+24, 0.5)
std = 7.7
ps = norm(mean, std).pdf(qs)
prior = Pmf(ps, qs)
prior.normalize()
# plot(prior)

joint = make_joint(prior, prior)
x = joint.columns
y = joint.index

X, Y = np.meshgrid(x, y)
A_taller = (X > Y)
a = np.where(A_taller, 1, 0)
likelihood = pd.DataFrame(a, index=x, columns=y)
posterior = joint * likelihood

marginal_A = marginal(posterior, axis=0)
marginal_B = marginal(posterior, axis=1)

# print(prior.mean())
plot([prior, marginal_A, marginal_B])

