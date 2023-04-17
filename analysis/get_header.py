import requests
import re

data_structures_link = 'https://raw.githubusercontent.com/larus-breeze/sw_sensor_algorithms/main/NAV_Algorithms/data_structures.h'
gnss_link = 'https://raw.githubusercontent.com/larus-breeze/sw_sensor_algorithms/main/NAV_Algorithms/GNSS.h'

response_measurement_data = requests.get(data_structures_link).text
response_coordinates = requests.get(gnss_link).text

regex_pattern_measurement_data_t = 'typedef struct(.|\n)* measurement_data_t;.*'
regex_pattern_coordinates_t = 'typedef struct(.|\n)* coordinates_t;.*'

x = (re.search(regex_pattern_measurement_data_t, response_measurement_data))
measurement_data_t = response_measurement_data[x.start(0):x.end()]


x = (re.search(regex_pattern_coordinates_t, response_coordinates))
coordinates_t = response_coordinates[x.start(0):x.end()]


print(measurement_data_t)
#print(coordinates_t)


