GPS
===

    Name                                         gps                                
    Object Id                                    3                                  
    Preffered IDs for Specific Datapoints        0x140 - 0x14f                      
    Preffered IDs for Generic Datapoints         0x540 - 0x54f                      
    Comment                                      Definition of CAN bus datagrams of a GPS Receiver

A GPS device provides data for navigation. Several GPS devices can exist in a CAN bus system. The ID assignment is carried out according to the procedure described in the specification. The first GPS device works with the specific IDs 0x140...0x14f and the generic IDs 0x540..0x54f.

ID 0x140 Date and Time
---
Name: date_time  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 7 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   year                     u16       year                                         
    2   month                    u8        month                                        
    3   day                      u8        day                                          
    4   hour                     u8        h                                            
    5   minute                   u8        min                                          
    6   second                   u8        s                                            

ID 0x141 Latitude
---
Name: latitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   latitude                 f64       rad                                          

ID 0x142 Longitude
---
Name: longitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   longitude                f64       rad                                          

ID 0x143 MSL Altitude and Geo Separation
---
Name: altitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x03

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   altitude                 f32       m                                            
    4   geo_separation           f32       m                                            

ID 0x144 Ground Track and Ground Speed
---
Name: track_speed  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x04

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   gnd_track                f32       rad                                          
    4   gnd_speed                f32       m/s                                          

ID 0x145 Number of Sattelites and Sat Fix Type
---
Name: satellites  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 2 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x05

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   number_of_sats           u8        .                                            
    1   fix_type                 u8        0 no_gps                                     
                                           1 2d_fix                                     
                                           2 3d_fix                                     
                                           3 rtk                                        

ID 0x540 Heartbeat and other generic data points are defined in [this specification](generic.md).
---