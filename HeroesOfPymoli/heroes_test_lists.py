import os
import csv
import pandas as pd
import numpy as np

csvpath = os.path.join("purchase_data.csv")
df = []
purchase_ID = []
SN = []
age = []
gender = []
item_ID = []
item_Name = []
price = []

with open(csvpath, "r") as csvfile:
   csvreader = csv.reader(csvfile,delimiter=",")
   next(csvreader)
   for row in csvreader:
      df.append(row)
      purchase_ID.append(row[0])
      SN.append(row[1])
      age.append(row[2])
      gender.append(row[3])
      item_ID.append(row[4])
      item_Name.append(row[5])
      price.append(row[6])
      




print(purchase_ID[6])
print(SN[6])
print(age[6])
print(gender[6])
print(item_ID[6])
print(item_Name[6])
print(price[6])
print(df[6])
   