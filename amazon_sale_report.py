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





# df = sns.countplot(data=data,x="Size" )
# plt.show()

# for bars in df.containers:                                     # shows actual size
    # df.bar_label(bars)
    # plt.savefig("size.png")
    # plt.show()
    
    
    # Note : From above Graph you can see that most people buys Medium (M) size.
    
    

# s_q = data.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

# sns.barplot(x="Size",y="Qty",data=s_q,color='orange')
# plt.show()





 # Courier status :
# sns.countplot(data = data, x="Courier Status",hue="Status",palette='viridis')
# plt.show()


# Note : From above Graph you can see that mostly items are shipped and few are cancelled due to some sort of reasons.
       
       
 


# Checking which product is sold the most :
# data['Category'] = data['Category'].astype(str)

# plt.hist(data = data,x="Category",bins=20,edgecolor='black',color='purple')
# plt.xlabel("Products",fontsize=12)
# plt.ylabel("Quantity",fontsize=12)
# plt.title("Product sold the most",fontsize=15)
# plt.show()


#  Note : From above graph you can see that T-shirts and shirts are the two most sold products. But some other products like shoes,
#         socks , wallet and perfume are not so popular.






# Checking how many retailers and buyers we have :
# dfx = data['B2B'].value_counts()
# ex = [0,0.2]
# plt.pie(dfx,autopct='%1.1f',explode=ex,startangle=180,shadow=True)
# plt.title("Buyers vs Retailers")
# plt.ylabel("Retailer")
# plt.xlabel("Buyer")
# plt.savefig("buyers_retailers.png")
# plt.show()



# Note : From above Graph you can see that 99% are retailers and only 1% are the people who buy products.







# Check that which sizes are available in all categories:
# sns.scatterplot(data = data, x="Category",y="Size",marker="D",c="red")
# plt.xlabel("Category",fontsize=12)
# plt.ylabel("Size",fontsize=12)
# plt.title("Size available for all Categories",fontsize=15)
# plt.savefig("size_category.png")
# plt.show()



# Note : From above Graph you can see that T-shirt and shirt have all sizes available except Free size.
#        Blazzer, Socks and Tousers have not 4XL,5XL,6XL and Free sizes available
#        Wallect, Perfume and Shoes have only Free size available.








# Check top/first 5 states which buys the most products:
top_10 = data['ship-state'].value_counts().head(5)

plt.figure(figsize=(22,6))

sns.countplot(data = data[data['ship-state'].isin(top_10.index)], x ="ship-state",hue="Category")

plt.xlabel("State", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Top 5 States with most number of purchases", fontsize=14)

plt.savefig("top5_states.png")
plt.show()



  # Note : From Above Graph you can see that most buyers are from Maharashtra and Karnataka with products like T-shirt and shirt.
  #        These are the top 5 states  which buy the most number of products. Products like shoes and wallet have least sale.
  
  
  
  
  
  
  
  
  
  # Conclusion : The above Data Analysis reveals that business has significant customer base in Maharashta and mainly services are retailers, 
  #              fulfills order through Amazon , experiences high demand of T-shirts and shirts with Medium size . 
  #              It also reveals the  Category which has the highest sales in each state.
  #              It shows that most products are shipped and few are cancelled due to some reasons.