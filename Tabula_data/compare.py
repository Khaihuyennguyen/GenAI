import pandas as pd
import numpy as np
import scipy
from scipy.stats import ks_2samp
from statsmodels.distributions.empirical_distribution  import ECDF

# 1: prepare the data
dataset = 'insurance_compare.csv'
url = "https://raw.githubusercontent.com/VincentGranville/Main/main/" + dataset
df = pd.read_csv(url)

# Note for insurance_compare dataset only
if dataset == 'insurance_compare.csv':
    df = df.drop('region', axis=1)
    df = df.dropna(axis='columns')
print(df.head())

data_real = df.loc[df['Data'] == 'Real']
data_real = data_real.drop('Data', axis=1)
data_real = data_real.to_numpy()
print(data_real)


# need to transpose the data

r_corr = np.corrcoef(data_real.T)
print(len(r_corr))

# Prepare the test
ltests = df.Data.unique().tolist()
print(df.head())
print(ltests)
popped_item = ltests.pop(0) # remove real data from tests
print(ltests)