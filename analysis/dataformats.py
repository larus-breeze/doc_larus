#!/user/bin/env python3

# Measurement logfiles
elements_f37 = ["acc x","acc y","acc z","gyro x","gyro y","gyro z","mag x","mag y","mag z","pitot","static p","temp",
                "ubatt","pos N","pos E","pos DWN","vel N","vel E","vel DWN","acc N","acc E","acc DWN","track GNSS",
                "speed GNSS","relpos N","relpos E","relpos D","rel HDG","speed acc","Lat 1","Lat 2","Long 1","Long 2",
                "ymdh","minsec sat fixtype","nano","geo_sep dummy"]

elements_f50 = [ 'acc x', 'acc y', 'acc z', 'gyro x','gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'Lowcost acc x',
                 'Lowcost acc y', 'Lowcost acc z', 'Lowcost gyro x', 'Lowcost gyro y', 'Lowcost gyro z',
                 'Lowcost mag x', 'Lowcost mag y', 'Lowcost mag z', 'pitot', 'static p', 'abs p', 'temp',
                 'abs sens t', 'ubatt', '', '', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN', 'acc N',
                 'acc E', 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG',
                 'speed acc', 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'xx', 'yy']


# Processed data logfiles
elements_f92 = [ "acc x","acc y","acc z","gyro x","gyro y","gyro z","mag x","mag y", "mag z","pitot","static p",
                 "temp","ubatt","pos N","pos E","pos DWN", "vel N","vel E","vel DWN","acc N","acc E","acc DWN",
                 "track GNSS","speed GNSS","relpos N","relpos E","relpos D","rel HDG","speed acc","Lat 1","Lat 2",
                 "Long 1","Long 2","ymdh","minsec sat fixtype","nano","geo_sep dummy","IAS","TAS","vario uncomp",
                 "vario","vario pressure","speed comp TAS","speed comp INS","vario integrator","wind N","wind E",
                 "wind D","wind avg N","wind avg E","wind avg D","circle mode","nav acc N","nav acc E","nav acc D",
                 "nav ind N","nav ind E","nav ind D","nav corr N","nav corr E","nav corr D","gyro corr F",
                 "gyro corr R","gyro corr D","q0","q1","q2","q3","roll","nick","yaw","acc vertical","turn rate",
                 "slip angle","nick angle","G_load","acc_F","acc_R","acc_D","gyro_F","gyro_R","gyro_D","P-altitude",
                 "SAT-MAG Hdg","QNH","Density","sat fix type","avg. Headwind","avg. crosswind","wind_N","wind_E",
                 "mag disturbance"]

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

# Format with datatypes
"""
#Helper for generation
# dtypes  int32_t  = i4,  int8_t = i1, uint16_t = u2,  f4 = float, f8 = double

data_f37 = '['
for element in elements_f37:
    data_f37 += '(\"{}\", \"f4\"), '.format(element)
data_f37 += ']'
print(data_f37)

"""

data_f37 = [("acc x", "f4"), ("acc y", "f4"), ("acc z", "f4"), ("gyro x", "f4"), ("gyro y", "f4"), ("gyro z", "f4"),
            ("mag x", "f4"), ("mag y", "f4"), ("mag z", "f4"), ("pitot", "f4"), ("static p", "f4"), ("temp", "f4"),
            ("ubatt", "f4"), ("pos N", "f4"), ("pos E", "f4"), ("pos DWN", "f4"), ("vel N", "f4"), ("vel E", "f4"),
            ("vel DWN", "f4"), ("acc N", "f4"), ("acc E", "f4"), ("acc DWN", "f4"), ("track GNSS", "f4"),
            ("speed GNSS", "f4"), ("relpos N", "f4"), ("relpos E", "f4"), ("relpos D", "f4"), ("rel HDG", "f4"),
            ("speed acc", "f4"),
            ("Lat", "f8"), ("Long", "f8"),
            ("year", "u1"),
            ("month", "u1"),
            ("day", "u1"),
            ("hour", "u1"),
            ("minute", "u1"),
            ("second", "u1"),
            ("sat number", "u1"),
            ("sat fix type", "u1"),
            ("nanoseconds", "u4"),
            ("geo separation dm", "i2"),
            ("dummy", "u2")]

