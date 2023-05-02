#!/user/bin/env python3
import numpy as np
import pandas as pd
from dataformats import *
import sys

# Howto execute:
# python3 ../flightdata/230430_090724.f37
#
# Process only the first 5000 values
# python3 ../flightdata/230430_090724.f37 5000

file = sys.argv[1]
limit = None
if len(sys.argv) > 2:
    limit = int(sys.argv[2])

if file.endswith('.f37'):
    elements = data_f37
elif file.endswith('.f50'):
    elements = data_f50
else:
    print('Error, file format not supported')
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
if limit:
    # Export only the first lines until the given limit
    df.loc[0:limit].to_csv(file+'data.csv')
else:
    df.to_csv(file+'data.csv')

