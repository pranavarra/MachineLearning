#This is a file that makes fake data

import numpy as np
import pandas as pd

def makeData(rows, columns, start=0, end=100, headers=None):
    fakeData = np.random.randint(low=start, high=end, size=(rows, columns))
    
    if(headers==None):
        headers = []
        for i in range(columns):
            columns[i] = "Column " + str(i)
    
    dataFrame = pd.DataFrame(data=fakeData, columns=headers)
    
    return dataFrame
