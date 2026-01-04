Magnetic Sensor
===

    Name                                         magnetic_sensor
    Object Id                                    6                                  
    Preffered IDs for Specific Datapoints        0x070 - 0x07f
    Preffered IDs for Generic Datapoints         0x470 - 0x47f
    Comment                                      external sensor for 3 axix magnetic raw data

A magnetic sensor provides 3 axis magnetic data with 100Hz. This data is used from the sensor instead of the internal magnetic data.  data for temperature and humidity.

ID 0x070 magnetic gain factor 
---
Name: magnetic data gain factor 
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   gain                     f32       LSB/μT     


ID 0x071 magnetic data  
---
Name: magnetic data  
Object-ID Version: 0  
Type: Data Object  
Interval: 10 ms  
Length: 6 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   x                        i16       gain via magnetic gain factor  
    1   y                        i16       gain via magnetic gain factor    
    2   z                        i16       gain via magnetic gain factor    


ID 0x470 Heartbeat and other generic data points are defined in [this specification](generic.md).
---
