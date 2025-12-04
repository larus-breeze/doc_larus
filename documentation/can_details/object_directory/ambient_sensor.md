Ambient Sensor
===

    Name                                         ambient_sensor                     
    Object Id                                    5                                  
    Preffered IDs for Specific Datapoints        0x2d0 - 0x2df
    Preffered IDs for Generic Datapoints         0x6d0 - 0x6df
    Comment                                      sensor for temperature and humidity

A ambient sensor provides data for temperature and humidity. The ID assignment shall be carried out according to the procedure described even if there is only one ambient sensor in the system. This is to ensure specification (object) extentions without the risk for address conflicts.

ID 0x2d0 temperature and humidity
---
Name: temperature_humidity  
Object-ID Version: 0  
Type: Data Object  
Interval: 10000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   temperature              f32       °C                                        
    4   humidity                 f32       %                                                                    

ID 0x6d0 Heartbeat and other generic data points are defined in [this specification](generic.md).
---
