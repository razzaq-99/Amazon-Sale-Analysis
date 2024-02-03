import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


data = pd.read_csv("Amazon Sale Report.csv",encoding="unicode_escape")

# print(data)
# print(data.info())


print(data.drop(['New','PendingS'],axis=1,inplace=True))     # drop unrelated or blank colums.
# print(data.info())

# print(data.isnull().sum())                                       # Checking null values
print(data.dropna(inplace=True))                                   # Dropped null values 

# data['ship-postal-code'] = data['ship-postal-code'].astype('int')      # converting data type of ship_postal_code
# print(data['ship-postal-code'].dtype)


# data['Date'] = pd.to_datetime(data['Date'])                            # converting data type of Date
# print(data['Date'].dtype)


# df = data.rename(columns={'Qty':'Quantity'})                         # renaming the coloumn of Qty
# print(df.columns)
# print(df)





df = sns.countplot(data=data,x="Size" )
# plt.show()

for bars in df.containers:                                     # shows actual size
    df.bar_label(bars)
    plt.savefig("size.png")
    plt.show()
    
    
    # Note : From above Graph you can see that most people buys Medium (M) size.
    
    
    



    