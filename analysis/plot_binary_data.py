#!/user/bin/env python3
from dataformats import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Put the file names you want to plot here:
files = ["../flightdata/20220714090230.f50.f123"]

for file in files:
    if file.endswith('.f105'):
        elements = elements_f105
    elif file.endswith('.f107'):
        elements = elements_f107
    elif file.endswith('.f110'):
        elements = elements_f110
    elif file.endswith('.f120'):
        elements = elements_f120
    elif file.endswith('.f123'):
        elements = elements_f123
    else:
        print('Format, not supported')
        exit()

    print(len(elements))

    # Create a data description for the raw data file format. Assume 32 bit float for each value.
    description = []
    for i in range(0, len(elements)):
        description.append((elements[i], 'f4'))

    # Create a pandas dataframe
    dt = np.dtype(description)
    data = np.fromfile(file, dtype=dt, sep="")
    df = pd.DataFrame(data)

    # Select the timeframe in the data
    #df = df[460000:560000]

    # Prepare the data
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
    axis[0, 0].plot(roll_deg, "b--", alpha=0.5, linewidth=0.5)
    axis[0, 0].legend(["roll angle"], loc="lower left")
    axis[0, 0].grid()
    par1 = axis[0, 0].twinx()
    par1.plot(df['wind avg N'], "r-", linewidth=0.5)
    par1.plot(df['wind avg E'], "g-", linewidth=0.5)
    par1.plot(df['wind N'], "r--", linewidth=0.5, alpha=0.6)
    par1.plot(df['wind E'], "g--", linewidth=0.5, alpha=0.6)
    par1.legend(['wind avg N', 'wind avg E', 'wind N', 'wind E'], loc="lower right")

    # Wind direction and speed instantaneous and average
    axis[0, 1].plot(windDirectionAvg, "b-", label='Average', alpha=1, linewidth=0.5)
    axis[0, 1].plot(windDirectionInst, "b--", label='Instantaneous', alpha=1, linewidth=0.5)
    axis[0, 1].plot(heading, "g-", label='Instantaneous', alpha=1, linewidth=0.7)
    axis[0, 1].grid()
    par1 = axis[0, 1].twinx()
    par1.plot(windSpeedAvg, "r-", label='Average', alpha=1, linewidth=0.5)
    par1.plot(windSpeedInst, "r--", label='Instantaneous', alpha=1, linewidth=0.5)
    axis[0, 1].legend(["average wind direction", "inst wind direction", "heading"], loc="lower left")
    par1.legend(["average wind speed", "inst wind speed"], loc="lower right")

    # Turn rate and circle mode
    axis[1, 0].plot(df['turn rate'], "b--", alpha=1, linewidth=0.5)
    axis[1, 0].legend(["turn rate"], loc="lower left")
    axis[1, 0].grid()
    par1 = axis[1, 0].twinx()
    par1.plot(df['circle mode'], "y-", linewidth=0.5)
    par1.legend(["circle mode"], loc="lower right")

    # Vario Signal, and height
    axis[1, 1].plot(df['TAS'], "b-", alpha=1, linewidth=0.5)
    axis[1, 1].legend(["TAS"], loc="lower left")
    axis[1, 1].grid()
    par1 = axis[1, 1].twinx()
    par1.plot(- df['pos DWN'], "b--", alpha=1, linewidth=0.5)
    par1.legend(["pos UP"], loc="lower right")

plt.show()



