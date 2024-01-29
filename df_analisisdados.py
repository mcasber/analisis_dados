import pandas as pd
import numpy as np 

df = pd.read_csv('C:\\Users\\Mariano\\basedados.csv',sep=",",header=0)

#print(df.info())
print(df.head(3))         
#print(type(df))
#print(df.iloc[9,10])#acces for index
#print(df['2'])#accedo por name column
#df2= df[df['7']>0.17]
#print(df2)
#print(df.describe())

df['suma'] = df.apply (lambda x : x['2']+x['3']+x['4']+x['5']+x['6']+x['7']+x['8']+x['9']+x['10']+x['11']+x['12'], axis=1)
print(df.head(3))
