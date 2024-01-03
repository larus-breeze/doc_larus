# Entry
Larus project and system documentation including helper scripts to process flight log data. A system description can be found here: [System description](documentation/Larus_Beschreibung.pdf)

# System Components
## Main Sensor
- Processing of all sensor signals, computation of vario signals, computation of AHRS and wind
- https://github.com/larus-breeze/hw_sensor
- https://github.com/larus-breeze/sw_sensor

## Frontend Display (comming soon)
- A 3D printed 57mm enclosure with a 2" transflective display including sound generation, powered by RUST and a STM32H743.

# Directories
- helper: scripts to monitor the live CAN-Bus data.
- analysis: scripts to visualize and convert flight log data.
- [CAN Specificatin](documentation/can_spec.md) 
