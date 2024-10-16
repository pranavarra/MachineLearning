import numpy as np
import pandas as pd

def makeData(rows, columns, start=0, end=100, headers=None, multFactor=None):
    fakeData = np.random.randint(low=start, high=end, size=(rows, columns))
    
    if(headers==None):
        headers = []
        for i in range(columns):
            columns[i] = "Column " + str(i)
    
    dataFrame = pd.DataFrame(data=fakeData, columns=headers)
    
    return dataFrame

data = makeData(rows=20, columns=2, start=0, end=100, headers=["Miles", "Mass(in some units)"])

print("Fake Data: ", data)

