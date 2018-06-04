import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

column_name = ['region','country','item_type','sales_channel','order_priority','order_date','oder_id','ship_date','units_sold','unit_price','unit_cost','total_revenue','total_cost','total_profit']

sales = pd.read_csv('100_Sales_Records.csv',names=column_name,header=0)

#print(sales.columns)
#print(sales.iloc[0:10,0:10])

#print(sales['country'].duplicated())

s1 = sales[sales['total_profit']>1000000]
print(s1['item_type'])