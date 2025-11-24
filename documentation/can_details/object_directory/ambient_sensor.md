Ambient Sensor
===

    Name                                         ambient_sensor                     
    Object Id                                    5                                  
    Preffered IDs for Specific Datapoints        0x290 - 0x29f                      
    Preffered IDs for Generic Datapoints         0x690 - 0x69f                      
    Comment                                      sensor for temperature and humidity

A ambient sensor provides data for temperature and humidity. Only one ambient sensor can exist in a CAN bus system. 

ID 0x290 temperature and humidity
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

ID 0x690 Heartbeat and other generic data points are defined in [this specification](generic.md).
---
