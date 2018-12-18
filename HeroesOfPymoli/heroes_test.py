import os
import csv
import pandas as pd
import numpy as np

csvpath = os.path.join("purchase_data.csv")
df = []
dic = {}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        # df.append(row)
        for k,v in dic:
            k = row[0]
            v = row[1]

    # print(df[5])
    print(dic)






        # if row[0] not in dic.keys():
        #     dic[row[0]]=1
        # else:
        #     dic[row[0]]+=1