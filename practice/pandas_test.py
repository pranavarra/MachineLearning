import numpy as np
import pandas as pd

data = np.array([[1,2], [7, 11], [-2, 34]])

print(data)

columns = ["temperature", "activity"]

df = pd.DataFrame(data=data, columns=columns)

df["adjusted"] = (df["temperature"]) + np.random.random(size= len(df["temperature"]))*10

print("The heads of the columns are: ", df.head()) # These are the column names

#print(df)

