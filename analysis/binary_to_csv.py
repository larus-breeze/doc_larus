#!/user/bin/env python3
from load_to_df import LoadLarus2Df
import sys

# Howto execute:
# python3 binary_to_csv ../flightdata/230430_090724.f37
#
# Process only the first 5000 values
# python3 binary_to_csv ../flightdata/230430_090724.f37 5000
file = sys.argv[1]
data = LoadLarus2Df(file)
df = data.df

limit = None
if len(sys.argv) > 2:
    limit = int(sys.argv[2])

# Export as CSV file:
if limit:
    # Export only the first lines until the given limit
    df.loc[0:limit].to_csv(file+'data.csv')
else:
    df.to_csv(file+'data.csv')

