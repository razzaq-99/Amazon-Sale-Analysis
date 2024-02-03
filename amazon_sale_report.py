import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


data = pd.read_csv("Amazon Sale Report.csv",encoding="unicode_escape")

# print(data)
# print(data.info())


# print(data.drop(['New','PendingS'],axis=1,inplace=True))         # drop unrelated or blank colums.
# print(df.info())

# print(data.isnull().sum())                                       # Checking null values
print(data.dropna(inplace=True))