GPS
===

    Name                     gps                                          
    Object Id                3                                            
    Comment                  Definition of CAN bus datagrams of a GPS Receiver

ID 0x00 Date and Time
---
Name: date_time  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 7 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   year                     u16       year                                         
    2   month                    u8        month                                        
    3   day                      u8        day                                          
    4   hour                     u8        h                                            
    5   minute                   u8        min                                          
    6   second                   u8        s                                            

ID 0x01 Latitude
---
Name: latitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   latitude                 f64       rad                                          

ID 0x02 Longitude
---
Name: longitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   longitude                f64       rad                                          

ID 0x03 MSL Altitude and Geo Separation
---
Name: altitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   altitude                 f32       m                                            
    4   geo_separation           f32       m                                            

ID 0x04 Ground Track and Ground Speed
---
Name: track_speed  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   gnd_track                f32       rad                                          
    4   gnd_speed                f32       m/s                                          

ID 0x05 Number of Sattelites, Fix valid and Heading valid
---
Name: satellites  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 3 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   number_of_sats           u8        .                                            
    1   sat_fix_valid            bool      .                                            
    2   sat_heading_valid        bool      .                                            

