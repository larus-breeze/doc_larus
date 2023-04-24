#!/user/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

elements_f105 = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'pitot',
                 'static p', 'temp', 'ubatt', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN', 'acc N',
                 'acc E', 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG',
                 'speed acc', 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'nano',
                 'geo_sep+dummy', 'IAS', 'TAS', 'vario uncomp', 'vario', 'vario pressure', 'speed comp TAS',
                 'speed comp INS', 'vario integrator', 'wind N', 'wind E', 'wind D', 'wind avg N', 'wind avg E',
                 'wind avg D', 'circle mode', 'nav acc N', 'nav acc E', 'nav acc D', 'nav ind N', 'nav ind E',
                 'nav ind D', 'nav corr N', 'nav corr E', 'nav corr D', 'gyro corr F', 'gyro corr R', 'gyro corr D',
                 'q0', 'q1', 'q2', 'q3', 'roll', 'nick ', 'yaw', 'acc vertical', 'turn rate', 'slip angle',
                 'nick angle', 'G_load', 'nav acc mag N', 'nav acc mag E', 'nav acc mag D', 'nav ind mag N',
                 'nav ind mag E', 'nav ind mag D', 'roll mag', 'nick mag', 'yaw mag', 'q1mag', 'q2mag', 'q3mag',
                 'q4mag', 'acc_F', 'acc_R', 'acc_D', 'gyro_F', 'gyro_R', 'gyro_D', 'press_alt', 'SAT-MAG Hdg',
                 'QFF', 'Density', 'satfix', 'headwiind', 'crosswind', 'wind_N', 'wind_E', 'mag_disturbance']

elements_f107 = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'pitot',
                 'static p', 'temp', 'ubatt', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN', 'acc N',
                 'acc E', 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG',
                 'speed acc', 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'nano',
                 'geo_sep dummy', 'IAS', 'TAS', 'vario uncomp', 'vario', 'vario pressure', 'speed comp TAS',
                 'speed comp INS', 'vario integrator', 'wind N', 'wind E', 'wind D', 'wind avg N', 'wind avg E',
                 'wind avg D', 'circle mode', 'q0', 'q1', 'q2', 'q3', 'roll', 'nick ', 'yaw', 'acc vertical',
                 'turn rate', 'slip angle', 'nick angle', 'G_load', 'Pressure-altitude', 'Air Density',
                 'Magnetic Disturbance', 'nav acc N', 'nav acc E', 'nav acc D', 'nav ind N', 'nav ind E', 'nav ind D',
                 'nav corr N', 'nav corr E', 'nav corr D', 'gyro corr F', 'gyro corr R', 'gyro corr D', 'nav acc mag N',
                 'nav acc mag E', 'nav acc mag D', 'nav ind mag N', 'nav ind mag E', 'nav ind mag D', 'roll mag',
                 'nick mag', 'yaw mag', 'q1mag', 'q2mag', 'q3mag', 'q4mag', 'acc_F', 'acc_R', 'acc_D', 'gyro_F',
                 'gyro_R', 'gyro_D', 'SAT-AHRS-Heading', 'QFF', 'sat fix type', 'avg. Headwind', 'avg. crosswind',
                 'wind_N', 'wind_E', 'inst wind N', 'inst wind E']

elements_f110 = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'pitot',
                 'static p', 'temp', 'ubatt', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN', 'acc N',
                 'acc E', 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG',
                 'speed acc', 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'nano',
                 'geo_sep dummy', 'IAS', 'TAS', 'vario uncomp', 'vario', 'vario pressure', 'speed comp TAS',
                 'speed comp INS', 'vario integrator', 'wind N', 'wind E', 'wind D', 'wind avg N', 'wind avg E',
                 'wind avg D', 'circle mode', 'q0', 'q1', 'q2', 'q3', 'roll', 'nick ', 'yaw', 'acc vertical',
                 'turn rate', 'slip angle', 'nick angle', 'G_load', 'Pressure-altitude', 'Air Density',
                 'Magnetic Disturbance', 'nav acc N', 'nav acc E', 'nav acc D', 'nav ind N', 'nav ind E',
                 'nav ind D', 'nav corr N', 'nav corr E', 'nav corr D', 'gyro corr F', 'gyro corr R',
                 'gyro corr D', 'nav acc mag N', 'nav acc mag E', 'nav acc mag D', 'nav ind mag N', 'nav ind mag E',
                 'nav ind mag D', 'roll mag', 'nick mag', 'yaw mag', 'q1mag', 'q2mag', 'q3mag', 'q4mag', 'acc_F',
                 'acc_R', 'acc_D', 'gyro_F', 'gyro_R', 'gyro_D', 'SAT-AHRS-Heading', 'QFF', 'sat fix type',
                 'avg. Headwind', 'avg. crosswind', 'wind_N', 'wind_E', 'inst wind N', 'inst wind E', 'speed_comp_1',
                 'speed_comp_2', 'speed_comp_3']

elements_f120 = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'Lowcost acc x',
                 'Lowcost acc y', 'Lowcost acc z', 'Lowcost gyro x', 'Lowcost gyro y', 'Lowcost gyro z',
                 'Lowcost mag x', 'Lowcost mag y', 'Lowcost mag z', 'pitot', 'static p', 'abs p', 'temp',
                 'abs sens t', 'ubatt', 'OAT', 'Humidity', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN',
                 'acc N', 'acc E', 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG',
                 'speed acc', 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'nano',
                 'geo_sep dummy', 'IAS', 'TAS', 'vario uncomp', 'vario', 'vario pressure', 'speed comp TAS',
                 'speed comp INS', 'vario integrator', 'wind N', 'wind E', 'wind D', 'wind avg N', 'wind avg E',
                 'wind avg D', 'circle mode', 'q0', 'q1', 'q2', 'q3', 'roll', 'nick ', 'yaw', 'acc vertical',
                 'turn rate', 'slip angle', 'nick angle', 'G_load', 'Pressure-altitude', 'Air Density',
                 'Magnetic Disturbance', 'nav acc N', 'nav acc E', 'nav acc D', 'nav ind N', 'nav ind E', 'nav ind D',
                 'nav corr N', 'nav corr E', 'nav corr D', 'gyro corr F', 'gyro corr R', 'gyro corr D', 'nav acc mag N',
                 'nav acc mag E', 'nav acc mag D', 'nav ind mag N', 'nav ind mag E', 'nav ind mag D', 'roll mag',
                 'nick mag', 'yaw mag', 'q1mag', 'q2mag', 'q3mag', 'q4mag', 'acc_F', 'acc_R', 'acc_D', 'gyro_F',
                 'gyro_R', 'gyro_D', 'SAT-AHRS-Heading', 'QFF', 'sat fix type', 'avg. Headwind', 'avg. crosswind',
                 'wind_N', 'wind_E', 'inst wind N', 'inst wind E']

elements_f123 = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'Lowcost acc x',
                 'Lowcost acc y', 'Lowcost acc z', 'Lowcost gyro x', 'Lowcost gyro y', 'Lowcost gyro z',
                 'Lowcost mag x', 'Lowcost mag y', 'Lowcost mag z', 'pitot', 'static p', 'abs p', 'temp', 'abs sens t',
                 'ubatt', 'OAT', 'Humidity', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN', 'acc N', 'acc E',
                 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG', 'speed acc',
                 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'nano', 'geo_sep dummy', 'IAS',
                 'TAS', 'vario uncomp', 'vario', 'vario pressure', 'speed comp TAS', 'speed comp INS',
                 'vario integrator', 'wind N', 'wind E', 'wind D', 'wind avg N', 'wind avg E', 'wind avg D',
                 'circle mode', 'q0', 'q1', 'q2', 'q3', 'roll', 'nick ', 'yaw', 'acc vertical', 'turn rate',
                 'slip angle', 'nick angle', 'G_load', 'Pressure-altitude', 'Air Density', 'Magnetic Disturbance',
                 'nav acc N', 'nav acc E', 'nav acc D', 'nav ind N', 'nav ind E', 'nav ind D', 'nav corr N',
                 'nav corr E', 'nav corr D', 'gyro corr F', 'gyro corr R', 'gyro corr D', 'nav acc mag N',
                 'nav acc mag E', 'nav acc mag D', 'nav ind mag N', 'nav ind mag E', 'nav ind mag D', 'roll mag',
                 'nick mag', 'yaw mag', 'q1mag', 'q2mag', 'q3mag', 'q4mag', 'acc_F', 'acc_R', 'acc_D', 'gyro_F',
                 'gyro_R', 'gyro_D', 'SAT-AHRS-Heading', 'QFF', 'sat fix type', 'avg. Headwind', 'avg. crosswind',
                 'wind_N', 'wind_E', 'inst wind N', 'inst wind E', 'speed_comp_1', 'speed_comp_2', 'speed_comp_3']



# Put the file names you want to plot here:
#files = ["flightdata/1476cdc_20220601_Wind_30.f50.f120", "flightdata/1476cdc_20220724_STGT.f50.f120", "flightdata/1276cdc_20220918120730_hang.f50.f120"]
#files = ["flightdata/1476cdc_20220724_STGT.f50.f120", "flightdata/1476cdc_20220724_STGT.f50_compass.f120"]
#files = ["flightdata/1476cdc_20230311_flug.f37.f107", "flightdata/92c366_20230311_flug.f37.f107"]
#files = ["../flightdata/20220714090230.f50.f123", "../flightdata/20220724_STGT.f50.f123"]
#files = ["../flightdata/20220724_STGT.f50.f123"]
files = ["../flightdata/230414_085440.f37.f110"]


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

    #'nav ind mag N', 'nav ind mag E', 'nav ind mag D'

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



