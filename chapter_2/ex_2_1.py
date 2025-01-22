import pandas as pd
from fractions import Fraction

def update(table):
    """사후확률을 계산함"""
    table['unnorm'] = table['prior'] * table['likelihood']
    prob_data = table['unnorm'].sum()
    table['posterior'] = table['unnorm'] / prob_data
    return prob_data

# table = pd.DataFrame(index=['Bowl 1', 'Bowl 2'])
# table['prior'] = 1/2, 1/2
# table['likelihood'] = 3/4, 1/2
# table['unnorm'] = table['prior'] * table['likelihood']
# prob_data = table['unnorm'].sum()
# table['posterior'] = table['unnorm'] / prob_data

table2 = pd.DataFrame(index=[6, 8, 12])
table2['prior'] = Fraction(1, 3)
table2['likelihood'] = Fraction(1, 6), Fraction(1, 8), Fraction(1, 12)
prob_data = update(table2)

table3 = pd.DataFrame(index=['Door 1', 'Door 2', 'Door 3'])
table3['prior'] = Fraction(1, 3)
table3['likelihood'] = Fraction(1, 2), 1, 0
update(table3)

table4 = pd.DataFrame(index=['Coin 1', 'Coin 2'])
table4['prior'] = Fraction(1, 2)
table4['likelihood'] = Fraction(1, 2), 1
update(table4)

table5 = pd.DataFrame(index=['(M, M)', '(M, F)', '(F, M)', '(F, F)'])
table5['prior'] = Fraction(1, 4)
table5['likelihood'] = 0, Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)
update(table5)

table6 = pd.DataFrame(index=['door1', 'door2', 'door3'])
table6['prior'] = Fraction(1, 3)
table6['likelihood'] = 0, 0, 1

table7 = pd.DataFrame(index=['1994', '1996'])
table7['prior'] = Fraction(1, 2)
table7['likelihood'] = 0.2 * 0.2, 0.1 * 0.14
update(table7)

print(table7)

