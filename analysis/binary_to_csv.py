#!/user/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from docutils.nodes import description

elements_f37 = [
"acc x","acc y","acc z","gyro x",
"gyro y","gyro z","mag x","mag y",
"mag z","pitot","static p","temp",
"ubatt","pos N","pos E","pos DWN",
"vel N","vel E","vel DWN","acc N",
"acc E","acc DWN","track GNSS","speed GNSS",
"relpos N","relpos E","relpos D","rel HDG",
"speed acc","Lat 1","Lat 2","Long 1",
"Long 2","ymdh","minsec sat fixtype",
"nano","geo_sep dummy",
]

elements_f92 = [
"acc x","acc y","acc z","gyro x","gyro y","gyro z","mag x","mag y",
"mag z","pitot","static p","temp","ubatt","pos N","pos E","pos DWN",
"vel N","vel E","vel DWN","acc N","acc E","acc DWN","track GNSS","speed GNSS",
"relpos N","relpos E","relpos D","rel HDG",
"speed acc","Lat 1","Lat 2","Long 1","Long 2","ymdh","minsec sat fixtype",
"nano","geo_sep dummy","IAS","TAS","vario uncomp","vario","vario pressure","speed comp TAS",
"speed comp INS","vario integrator","wind N","wind E","wind D","wind avg N","wind avg E","wind avg D",
"circle mode","nav acc N","nav acc E","nav acc D","nav ind N","nav ind E","nav ind D","nav corr N",
"nav corr E","nav corr D","gyro corr F","gyro corr R","gyro corr D",
"q0","q1","q2","q3","roll","nick","yaw","acc vertical",
"turn rate","slip angle","nick angle","G_load",
"acc_F","acc_R","acc_D","gyro_F","gyro_R","gyro_D","P-altitude","SAT-MAG Hdg",
"QNH","Density","sat fix type","avg. Headwind",
"avg. crosswind","wind_N","wind_E","mag disturbance"
]

# Put the file name you want to convert here:
file = "230304_073330.f37"

if '.f92' in file:
    elements = elements_f92
elif '.f37' in file:
    elements = elements_f37
else:
    print('Error, not supported')
    exit()

# Create a data description for the raw data file format. Assume 32 bit float for each value.
description = []
for i in range(0, len(elements)):
    description.append((elements[i], 'f4'))

# Create a pandas dataframe
dt = np.dtype(description)
data = np.fromfile(file, dtype=dt, sep="")
df = pd.DataFrame(data)
print(df)

# Export as CSV file:
df.loc[0:500000].to_csv(file+'data.csv')

