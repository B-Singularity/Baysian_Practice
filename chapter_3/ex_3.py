from empiricaldist import Pmf
import numpy as np

def update_dice(pmf, data):
    hypos = pmf.qs
    likelihood = 1 / hypos
    impossible (data > hypos)
    likelihood[impossible] = 0
    pmf *= likelihood
    pmf.normalize()

# hypos = [6, 8, 12]
# prior = Pmf(1/3, hypos)
# likelihood1 = 1/6, 1/8, 1/12
# likelihood2 = 0, 1/8, 1/12

# posterior = prior * likelihood1
# posterior.normalize()
# posterior *= likelihood2
# posterior.normalize()

# hypos = [6, 8, 12]
# prior = Pmf(1/3, hypos)
# likelihood1 = 1/6, 1/8, 1/12
# likelihood2 = 1/6, 1/8, 1/12
# likelihood3 = 1/6, 1/8, 1/12
# likelihood4 = 0, 1/8, 1/12
# posterior = prior * likelihood1
# posterior.normalize()
# posterior *= likelihood2
# posterior.normalize()
# posterior *= likelihood3
# posterior.normalize()
# posterior *= likelihood4
# posterior.normalize()
