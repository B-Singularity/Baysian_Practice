from scipy.stats import gaussian_kde
from empiricaldist import Pmf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def read_data(filename):
    df = pd.read_csv(filename, index_col=0, skiprows=[1])
    return df.dropna().transpose()

def kde_from_sample(sample, qs):
    kde = gaussian_kde(sample)
    ps = kde(qs)
    pmf = Pmf(ps, qs)
    pmf.normalize()
    return pmf

def prob_overbid(sample_diff):
    return np.mean(sample_diff > 0)

df2011 = read_data(r'C:\Users\SSAFY\Downloads\sung\ThinkBayes2\data\showcases.2011.csv')
df2012 = read_data(r'C:\Users\SSAFY\Downloads\sung\ThinkBayes2\data\showcases.2012.csv')

df = pd.concat([df2011, df2012], ignore_index=True)
qs = np.linspace(0, 80000, 81)
prior1 = kde_from_sample(df['Showcase 1'], qs)
#
# plt.figure(figsize=(8, 5))
# plt.plot(prior1.index, prior1.values, marker='o', color='blue', label='PMF')
# plt.xlabel('Number of Goals')
# plt.ylabel('Probability')
# plt.title('Poisson PMF: λ = 1.4')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.show()

sample_diff1 = df['Bid 1'] - df['Showcase 1']
sample_diff2 = df['Bid 2'] - df['Showcase 2']

qs = np.linspace(-40000, 20000, 61)
kde_diff1 = kde_from_sample(sample_diff1, qs)
kde_diff2 = kde_from_sample(sample_diff2, qs)
mean_diff1 = sample_diff1.mean()
std_diff1 = sample_diff1.std()

error_dist1 = norm(0, std_diff1)
# error = -100
# print(error_dist1.pdf(error))

# guess1 = 23000
# error1 = guess1 - prior1.qs
# likelihood1 = error_dist1.pdf(error1)
# posterior1 = prior1 * likelihood1
# posterior1.normalize()
# print(prior1.mean(), posterior1.mean())

guess2 = 38000
error2 = guess2 - prior1.qs
likelihood2 = error_dist1.pdf(error2)
posterior2 = prior1 * likelihood2
posterior2.normalize()
print(posterior2.mean())

#
# plt.figure(figsize=(8, 5))
# plt.plot(prior1.index, prior1.values, posterior1.index, posterior1.values, marker='o', color='blue', label='PMF')
# plt.xlabel('Number of Goals')
# plt.ylabel('Probability')
# plt.title('Poisson PMF: λ = 1.4')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.show()