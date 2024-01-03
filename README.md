# Overview
Larus project and system documentation including helper scripts to process flight log data. Here is a system description [System description](documentation/Larus_Beschreibung.pdf)

# System Components Overview
## Main Sensor
- Processing of all sensor signals, computation of vario signals, computation of AHRS and wind
- https://github.com/larus-breeze/hw_sensor
- https://github.com/larus-breeze/sw_sensor

## Frontend Display (including audio)
- Work in progress, comming soon.


# Directories:
- helper: scripts to monitor the live CAN-Bus data.
- analysis: scripts to visualize and convert flight log data.
- [CAN Specificatin](documentation/can_spec.md) 
