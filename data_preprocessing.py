import pandas as pd
import numpy as np
data={
    'Age': [22, 25, 47, 35, 52, 46, 58, 23, 40, 120],
    'Salary': [25000, 30000, 50000, 40000, 60000, None, 80000, 27000, 45000, 100000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi', 'Mumbai', 'Delhi']
}
df=pd.DataFrame(data)
print(df)
print("==================================")
##df['Salary']= df['Salary'].isna()
##print(df)
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
print(df)
print("==================================")

df_filtered=df[(df['Salary']>50000) & (df['City']=='Delhi')]
print(df_filtered)


#### data analytics using maltplotlib
x=[23,43,23,56,43,78,21,78,56,89]
y=[100,200,300,200,400,600,450,540,890,670]
##import malplotlib.pyplot as pl
##pl.bar(x,y,color='red')
##pl.title("test")
##pl.xlabel("this is x asix")
##pl.ylabel("this is y axis")
##pl.show()
df['Age_Category'] = df['Age'].apply(
    lambda x: 'Young' if x < 30 else 'Adult' if x < 50 else 'Senior'
)
print(df['Age_Category'])

import pandas as pd

df1 = pd.DataFrame({
    'Monthly_Salary': [18000, 25000, 32000, 45000, 70000, 90000]
})

bins = [0, 30000, 60000, 100000]
labels = ['Low', 'Medium', 'High']

df1['Salary_Level'] = pd.cut(
    df['Monthly_Salary'],
    bins=bins,
    labels=labels
)

print(df1)
