# Entry
Larus project and system documentation including helper scripts to process flight log data. A system description can be found here: [System description](documentation/Larus_Beschreibung.pdf)

# System Components
## Sensor
- Processing of all sensor signals, computation of vario signals, computation of AHRS and wind. 
- https://github.com/larus-breeze/hw_sensor
- https://github.com/larus-breeze/sw_sensor
- The sensor can be connected to the XCSOAR Fork Opensoar which has a Larus device driver implemented: https://github.com/August2111/OpenSoar Binaries can be found here: https://opensoar.de/releases/

## Frontend Display (comming soon)
- A 3D printed 57mm enclosure with a 2" transflective display including sound generation, powered by RUST and a STM32H743.
- Connected to the sensor via a CAN Bus.

# Directories
- helper: scripts to monitor the live CAN-Bus data.
- analysis: scripts to visualize and convert flight log data.
- [CAN Specificatin](documentation/can_spec.md) 
