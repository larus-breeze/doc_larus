# Overview
System documentation and helper scripts to process the flight log data.

# System Components Overview
## Main Sensor
- Processing of all sensor signals, computation of vario signals, computation of AHRS and wind
- https://github.com/larus-breeze/hw_sensor
- https://github.com/larus-breeze/sw_sensor


## Frontend Display
- TODO: describe frontend display system


## Utility Board 
- Blue Pill or (optionally) F4 based utility module to generate the vario audio sound. Can additionally sense temperature and humidity. Can optionally and additionally handle a flap position sensor, micro switches to detect "gear down" , "brakes out", "flaps above neutral", and a little detached board carrying an array of LEDs to indicate the current and optimal flaps setting 
- https://github.com/larus-breeze/hw_utility
- https://github.com/larus-breeze/sw_utility

# Documentation & Utility content here:
- helper: Scripts e.g. to monitor the live CAN-Bus data.
- documentation: system design and documentation files 
- analysis: scripts to visualize and convert flight log data.
