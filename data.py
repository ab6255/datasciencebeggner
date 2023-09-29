import pandas as pd

df=pd.read_csv('sales.csv')
df.head()
# demisions seen in datafram
df.shape
#bottom five row
df.tail(10)
#seen columans name
df.columns
df['Sales']

#select multiple coloum
df[['Sales','Quantity']]


df.tail(63)
import pandas as pd
df=pd.read_csv('sales.csv')
df.head()
df.iloc[:5]
#select row by there position

df.iloc[:,:4]
#select coloum by there position
df[df['Quantity']==2]
#calculate mode
import pandas as pd
data=pd.read_csv('Sales.csv')
data.head()
#sales_data =data['Ship_Mode'].mode()
Sales_data=data['Product ID'].mode()

# calculate mean = sum of quantites/number of quantiter
data_new=data['Quantity'].mean()
print('Quantity.mean')
data_new=pd.read_csv('profit.csv')
data_new.head()
mean_data_new=data_new['fixed_costs_for_b2b_sales'].mean()
print(mean_data_new)
data_new=pd.read_csv ('profit.csv').mode()
print(id)
import pandas as pd
data=pd.read_csv("profit.csv")
data.head(6)
profit_data=data['total cost'].median()
print(profit_data)
#calculating quantities.remember are1/4th of quartiles.
Q1=data['total cost'].quantile(0.25)
Q2=data['total cost'].quantile(0.5)
Q3=data['total cost'].quantile(0.75)
Q4=data['total cost'].quantile(1)

print('First Quartile',Q1)
print('second Quartile',Q2)
print('Third Quartile',Q3)
print('Fourth Quartile',Q4)
# best to mesure the tedence  is median
#spred sheet
#spread of data descibe how similar .range is the best to calculate dara lies
#samll-large/2 difrence
max_data = data['total cost'].max()



min_data = data['total cost'].min()
Range_data= max_data - min_data
print(Range_data)
 # calculating IQR requires calculating 1st and 3 quartiles
Q1=data['total cost'].quantile(0.25)
Q2=data['total cost'].quantile(0.75)
IQR = Q3 -Q1
print(IQR)
#iqr=inter quantile range
#varence
import pandas as pd
data=pd.read_csv('9 variance.csv')
data.head()
# step to calculate variance
#calculate mean
#calculate the distance of mean each for element
#calculate square distance
#take average of square distance
mean=data['total revanu'].mean()
difference=data['total revanu'] -mean
squared_difference=difference **2
variance=squared_difference.mean()
print(variance)
var_data=data['total revanu'].var(ddof =0)
standard_deviation=variance **(1/2)
standard_deviation
#sdandard deviation

std= data['total revanu'].std(ddof=0)
std
print(var_data)




