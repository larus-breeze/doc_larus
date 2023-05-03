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
heading = df['yaw'] / 2 / np.pi * 360
roll_deg = df['roll'] / 2 / np.pi * 360
nav_ind_abs = np.sqrt(np.square(df['nav ind mag N'])*np.square(df['nav ind mag N'] + df['nav ind mag E'])*np.square(df['nav ind mag E']) + df['nav ind mag D'])*np.square(df['nav ind mag D'])

figure, axis = plt.subplots()
figure.suptitle("Magnetic induction from: " + file)
plt.autoscale(enable=True, axis='y')

axis.plot(nav_ind_abs, "b", alpha=1.0, linewidth=1)
axis.legend(["nav ind abs"], loc="lower left")
axis.grid()
par1 = axis.twinx()
par1.plot(df['nav ind mag N'], "r-", linewidth=0.5)
par1.plot(df['nav ind mag E'], "g-", linewidth=0.5)
par1.plot(df['nav ind mag D'], "y-", linewidth=0.5)
par1.legend(['nav ind mag N', 'nav ind mag E', 'nav ind mag D'], loc="lower right")

figure, axis = plt.subplots()
figure.suptitle("Raw magnetic values from: " + file)
plt.autoscale(enable=True, axis='y')

axis.plot(nav_ind_abs, "b", alpha=1.0, linewidth=1)
axis.legend(["nav ind abs"], loc="lower left")
axis.grid()
par1 = axis.twinx()
par1.plot(df['mag x'], "r-", linewidth=0.5)
par1.plot(df['mag y'], "g-", linewidth=0.5)
par1.plot(df['mag z'], "y-", linewidth=0.5)
par1.legend(['mag x', 'mag y', 'mag z'], loc="lower right")

plt.show()



