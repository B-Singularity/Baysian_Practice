from scipy.stats import poisson
from empiricaldist import Pmf
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def make_poisson_pmf(lam, qs):
    ps = poisson(lam).pmf(qs)
    pmf = Pmf(ps, qs)
    pmf.normalize()
    return pmf

def update_poisson(pmf, data):
    k = data
    lams = pmf.qs
    likelihood = poisson(lams).pmf(k)
    pmf *= likelihood
    pmf.normalize()

lam = 1.4
goals = np.arange(10)
pmf_goals = make_poisson_pmf(lam, goals)
#
# # 시각화
# plt.figure(figsize=(8, 5))
# plt.bar(pmf_goals.index, pmf_goals.values, color='skyblue', edgecolor='black', alpha=0.7)
# plt.xlabel('Number of Goals')
# plt.ylabel('Probability')
# plt.title('Poisson PMF: λ = 1.4')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

alpha = 1.4
qs = np.linspace(0, 10, 101)
ps = gamma(alpha).pdf(qs)
prior = Pmf(ps, qs)
prior.normalize()
lams = prior.qs
k = 4
france = prior.copy()
update_poisson(france, 4)


# # 시각화
# plt.figure(figsize=(8, 5))
# plt.plot(france.index, france.values, marker='o', color='blue', label='PMF')
# plt.xlabel('Number of Goals')
# plt.ylabel('Probability')
# plt.title('Poisson PMF: λ = 1.4')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.show()

