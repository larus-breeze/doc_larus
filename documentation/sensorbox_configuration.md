Procedure from the User's Perspective
===

The configuration of the Sensobox using the Paremeter on the SD card has so far been a hurdle to the use of Larus. A simple procedure is to be established for the interaction between the sensor box and the front end. From the user's point of view, this should proceed as follows:

1. **Only for devices with DGNSS:** The lateral position of the slave sensor must be set on the front end beforehand (ANT_SLAVE_RIGHT).
2. The glider is brought onto a flat surface, tail dolly is removed and the left wing is put down. Measurement_1 is then triggered at the front end.
3. Now the right wing of the glider is put down and then measurement_2 is triggered at the front end.
4. The surfaces are straightened and a measurement_3 is taken. The inclination of the fuselage should correspond to the inclination at best l/d ratio.
5. The cmd_calc_sensor_orientation is triggered. The sensor box calculates on the basis of the measurements the installation position and saves the values. The sensor box is now ready for the first flight, during which the configuration is completed.
6. Fly straight ahead for 10 seconds at the speed of the best l/d ratio and then trigger command cmd_fine_tune_calibration.

The sensor box optimizes the calibration and saves the values

---
Detailed Description of the Procedure:
===

Setting ANT_SLAVE_RIGHT via the "Sensorbox Advanced Menu", see below

Measurement_1 (on the ground)
- The frontend sends the command CMD_MEASURE_POS_1 to the sensor box
- The sensor box measures and saves the values

Measurement_2 (on the ground)
- The front end sends the CMD_MEASURE_POS_2 command to the sensor box
- The sensor box measures again and saves the values

Measurement_3 (on the ground)
- The front end sends the command CMD_MEASURE_POS_3 to Sensorbox
- The sensor box measures again 

Cmd_calc_sensor_orientation (on the ground)
- The fronted sends the command CMD_CALC_SENSOR_ORIENTATION
- The sensor box calculates the values for the sensor orientation and overwrites the existing configuration (SensTilt_Roll, SensTilt_Pitch and SensTilt_Yaw). Please note that the Sens_Tilt_Pitch is estimated, as the flight attitude differs from the position on the field.

Cmd_fine_tune_calibration (in the air)
- The fronted sends the command CMD_FINE_TUNE_CALIBRATION
- The sensor box fine-tunes the configuration values accordingly
- If a DGNSS device is used, the distance between the two sensors and the height difference are measured and also saved (ANT_BASELEN, ANT_SLAVE_DOWN). 

---
Sensorbox Advanced Menu
===

In a “Sensorbox-Advanced-Menu” it should also be possible to view and set the following values:

Pressure Calibration
- Pitot_Offset
- Pitot_Span
- QNH-delta

Preferences
- Mag_Auto_Calib
- Vario_TC
- Vario_Int_TC
- Wind_TC
- Mean_Wind_TC

Sensor Orientation
- SensTilt_Roll
- SensTilt_Pitch
- SensTilt_Yaw

GNSS Type
- GNSS_CONFIG

D-GNSS Configuration
- ANT_BASELEN
- ANT_SLAVE_DOWN
- ANT_SLAVE_RIGHT

---
How does this work?
===

After measurement 1, 2 and3 , the sensor box knows where the bottom is and it knows the area between the vectors. Together with the right-thumb rule, the software also knows where the front is. The position of the horizon is also known.

The pitch is not yet defined, as it depends on the angle of attack of the glider. But such a glider is positioned on the runway in such a way that it can take off. This means that the angle of attack must lie within a narrowly defined range. It may also be useful to distinguish between flap planes and fixed-wing planes. Here the angle of incidence will differ slightly. With an assumed angle of attack on the ground, you could therefore estimate a pitch setting that is accurate to within a few degrees.

In flight, the speed for the best glide is flown and the pitch is fine-tuned at the touch of a button.
