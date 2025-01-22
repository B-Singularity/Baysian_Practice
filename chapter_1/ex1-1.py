import pandas as pd

gss_bayes_csv = r"C:\Users\SSAFY\Downloads\sung\ThinkBayes2\data\gss_bayes.csv"

def prob(A):
    return A.mean()

def condition(proposition, given):
    return prob(proposition[given])

gss = pd.read_csv(gss_bayes_csv, index_col=0)
banker = (gss['indus10'] == 6870)
female = (gss['sex'] == 2)
male = gss['sex'] == 1
liberal = gss['polviews'] <= 3
democrat = gss['partyid'] <= 1
selected = female[banker]
print(condition(banker, female))
print(condition(female, banker))

