Magnetic Sensor
===

    Name                                         magnetic_sensor
    Object Id                                    6                                  
    Preffered IDs for Specific Datapoints        0x070 - 0x07f
    Preffered IDs for Generic Datapoints         0x470 - 0x47f
    Comment                                      external sensor for 3 axix magnetic raw data

A magnetic sensor provides 3 axis magnetic induction data with 100Hz. The data are used within the sensor replacing the internal magnetic data.

ID 0x070 magnetic data  
---
Name: magnetic data  
Object-ID Version: 0  
Type: Data Object  
Interval: 10 ms  
Length: 6 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   x                        i16       75LSB / μT  
    1   y                        i16       75LSB / μT  
    2   z                        i16       75LSB / μT  

ID 0x470 Heartbeat and other generic data points are defined in [this specification](generic.md).
---
