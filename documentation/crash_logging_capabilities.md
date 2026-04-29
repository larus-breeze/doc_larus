# Crash-Logging Capabilities of the Larus Sensor 
The Larus team has developed a sensor module to acquire data from Global Navigation Satellite System, an Inertial Measurement unit and Pitot and static pressure sensors. The sensor data are combined to provide all essential information for cockpit instruments like the variometer, a AHRS (Artificial Horizon) and the navigation computer. The sampling-rate is 10Hz for the GNSS and 100Hz for the other sensors. The three-dimensional Accelerometer has a range of +/- 160 m/s². The maximum rotation-rate for the gyros is 2000 degrees/s. 

The Larus sensor can log its inputs to a micro-SD storage card. The micro-SD is written approximately two times per second. If required the logged data can be used to investigate the flight history in general and especially the details of an accident. 

The writing of the micro-SD will very probably be interrupted when a crash occurs due to a power failure. It would be possible to add a FRAM memory module to record the sensor data at 100Hz. 
With this extra memory the Larus sensor could basically log the information up to the last 10ms in case of a crash. 
