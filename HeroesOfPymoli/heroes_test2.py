import numpy as np

lines = np.genfromtxt("purchase_data.csv", delimiter=",", dtype=None)
my_dict = dict()
for i in range(len(lines)):
   my_dict[lines[i][0]] = lines[i][1]

print(my_dict[1])