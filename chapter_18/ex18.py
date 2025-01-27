from scipy import stats
from empiricaldist import Pmf
import inspect
import numpy as np
import sys
sys.path.append("/Users/seong-gyeongjun/Downloads/Baysian_Practice")
import my_util.plot as plot
from scipy.stats import multinomial, dirichlet



def make_gamma_dist(alpha, beta):
    dist = stats.gamma(alpha, scale=1/beta)
    dist.alpha = alpha
    dist.beta = beta
    return dist

def update_gamma(prior, data):
    k, t = data
    alpha = prior.alpha + k
    beta = prior.beta + t
    return make_gamma_dist(alpha, beta)

def make_beta(alpha, beta):
    dist = stats.beta(alpha, beta)
    dist.alpha = alpha
    dist.beta = beta
    return dist
def update_beta(prior, data):
    k, t = data
    alpha = prior.alpha + k
    beta = prior.beta + t - k
    return make_beta(alpha, beta)

# data = 3, 2, 1
# n = np.sum(data)
# ps = 0.4, 0.3, 0.3
#
# print(multinomial.pmf(data, n, ps))

alpha = 1, 2, 3
dist = dirichlet(alpha)
print(dist.rvs())




