#!/user/bin/env python3
from load_to_df import LoadLarus2Df
import numpy as np
import matplotlib.pyplot as plt
import sys

# Howto execute:
# python3 plot_wind.py ../flightdata/230414_085440.f37.f110
file = sys.argv[1]
data = LoadLarus2Df(file)
df = data.df

# Prepare the data
t = df.index / 100.0 / 60.0   # 100Hz ticks to minutes for the time axis
windDirectionAvg = np.arctan2( - df['wind avg E'], - df['wind avg N']) / 2 / np.pi * 360
windDirectionInst = np.arctan2( - df['wind E'], - df['wind N']) / 2 / np.pi * 360
windSpeedAvg = np.sqrt(np.square(df['wind avg E']) + np.square(df['wind avg N']))
windSpeedInst = np.sqrt(np.square(df['wind E']) + np.square(df['wind N']))
heading = df['yaw'] / 2 / np.pi * 360
roll_deg = df['roll'] / 2 / np.pi * 360
nav_ind_abs = np.sqrt(np.square(df['nav ind mag N'])*np.square(df['nav ind mag N'] + df['nav ind mag E'])*np.square(df['nav ind mag E']) + df['nav ind mag D'])*np.square(df['nav ind mag D'])

# Plot the data:
figure, axis = plt.subplots(2, 2, sharex=True)
figure.suptitle("File: " + file)
plt.autoscale(enable=True, axis='y')

# Wind N / E instantaneous and average
axis[0, 0].plot(t, roll_deg, "b--", alpha=0.5, linewidth=0.5)
axis[0, 0].legend(["roll angle"], loc="lower left")
axis[0, 0].grid()
par1 = axis[0, 0].twinx()
par1.plot(t, df['wind avg N'], "r-", linewidth=0.5)
par1.plot(t, df['wind avg E'], "g-", linewidth=0.5)
par1.plot(t, df['wind N'], "r--", linewidth=0.5, alpha=0.6)
par1.plot(t, df['wind E'], "g--", linewidth=0.5, alpha=0.6)
par1.legend(['wind avg N', 'wind avg E', 'wind N', 'wind E'], loc="lower right")

# Wind direction and speed instantaneous and average
axis[0, 1].plot(t, windDirectionAvg, "b-", label='Average', alpha=1, linewidth=0.5)
axis[0, 1].plot(t, windDirectionInst, "b--", label='Instantaneous', alpha=1, linewidth=0.5)
axis[0, 1].plot(t, heading, "g-", label='Instantaneous', alpha=1, linewidth=0.7)
axis[0, 1].grid()
par1 = axis[0, 1].twinx()
par1.plot(t, windSpeedAvg, "r-", label='Average', alpha=1, linewidth=0.5)
par1.plot(t, windSpeedInst, "r--", label='Instantaneous', alpha=1, linewidth=0.5)
axis[0, 1].legend(["average wind direction", "inst wind direction", "heading"], loc="lower left")
par1.legend(["average wind speed", "inst wind speed"], loc="lower right")

# Turn rate and circle mode
axis[1, 0].plot(t, df['turn rate'], "b--", alpha=1, linewidth=0.5)
axis[1, 0].legend(["turn rate"], loc="lower left")
axis[1, 0].grid()
axis[1, 0].set_xlabel('t [minutes]')
par1 = axis[1, 0].twinx()
par1.plot(t, df['circle mode'], "y-", linewidth=0.5)
par1.legend(["circle mode"], loc="lower right")

# TAS and height
axis[1, 1].plot(t, df['TAS'], "b-", alpha=1, linewidth=0.5)
axis[1, 1].legend(["TAS"], loc="lower left")
axis[1, 1].grid()
axis[1, 1].set_xlabel('t [minutes]')
par1 = axis[1, 1].twinx()
par1.plot(t, - df['pos DWN'], "b--", alpha=1, linewidth=0.5)
par1.legend(["pos UP"], loc="lower right")

plt.show()



