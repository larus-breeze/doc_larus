#!/user/bin/env python3
import numpy as np
import pandas as pd
from dataformats import *
import matplotlib.pyplot as plt
#from docutils.nodes import description


# Put the file name you want to convert here:
file = "../flightdata/230430_090724.f37"
#file = "../flightdata/20220724_STGT.f50"

if '.f92' in file:
    elements = elements_f92
elif '.f37' in file:
    elements = data_f37
elif '.f50' in file:
    elements = elements_f50
else:
    print('Error, not supported')
    exit()

# Create a data description for the raw data file format. Assume 32 bit float for each value.
description = []
for i in range(0, len(elements)):
    description.append((elements[i][0], elements[i][1]))

# Create a pandas dataframe
dt = np.dtype(description)
data = np.fromfile(file, dtype=dt, sep="")
df = pd.DataFrame(data)
print(df)

# Export as CSV file:
#df.loc[0:500000].to_csv(file+'data.csv')
df.to_csv(file+'data.csv')

