import pandas as pd
import numpy as np

# watch first half hour of class!

df = pd.read_csv("purchase_data.csv")

df.head()

#Homework notes:
# df.groupby('SN').agg({'Price:{'sum'},'Purchase ID':'count'})
# summary.columns = [' '.join(col).strip() for col in summary.columns.value]}
# summary.sort_values(by='Price_sum',ascending=False.head(7))

# out = df.groupby('Age Range').agg({"Price:": "sum", "SN":"nunique"})
# out['Avg Total per Person'] = out.Price / out.SN #rowwise operation here

#most profitable
df.groupby(['Item Name', 'Item ID']).agg({"Purchase ID":"count","Price": ["sum","min"]
})

popular.columns = ['_'.join(col).strip() for col in popular.columns.values]

