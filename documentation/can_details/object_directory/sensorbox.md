Larus Sensor Box
===

    Name                     larus_sensor_box                             
    Object Id                2                                            
    Comment                  Definition of CAN bus datagrams of the Larus Sensor Box

ID 0x00 Roll Angle and Nick Angle (Front-Right-Down System)
---
Name: roll_nick  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   roll_angle               f32       rad                                          
    4   nick_angle               f32       rad                                          

ID 0x01 Heading and Magnetic Declination
---
Name: heading  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   heading                  f32       rad                                          
    4   magnetic_declination     f32       rad                                          

ID 0x02 TAS (True Airspeed) and IAS (Indicated Airspeed)
---
Name: airspeed  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   tas                      f32       m/s                                          
    4   ias                      f32       m/s                                          

ID 0x03 Vario and Vario Avarage
---
Name: vario  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   vario                    f32       m/s                                          
    4   vario_avarage            f32       m/s                                          

ID 0x04 Wind Direction and Wind Speed
---
Name: wind  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   wind_direction           f32       rad                                          
    4   wind_speed               f32       m/s                                          

ID 0x05 Avarage Wind Direction and Avarage Wind Speed
---
Name: avarage_wind  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   avarage_wind_direction   f32       rad                                          
    4   avarage_wind_speed       f32       m/s                                          

ID 0x06 Ambient Pressure and Air Density
---
Name: atmosphere  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   ambient_pressure         f32       Pa                                           
    4   air_density              f32       kg/m^3                                       

ID 0x07 Acceleration Angle Front and Angle Right
---
Name: acceleration  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   acceleration_front       f32       rad                                          
    4   acceleration_right       f32       rad                                          

ID 0x08 Turnrate and State
---
Name: turn_rate  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 5 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   turnrate_to_the_right    f32       rad/s                                        
    4   state                    u8        0 STRAIGHT_FLIGHT                            
                                           1 TRANSITION                                 
                                           2 CIRCLING                                   

ID 0x09 Calculated trift angle
---
Name: trift_angle  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 4 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   trift_angle              f32       rad, positive if track right of heading      

ID 0x0a Stystem State and GIT Tag Decimal
---
Name: system_state  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   system_state             u32       status                                       
    4   git_tag_dec              u32       git tag                                      

ID 0x0b Supply Voltage
---
Name: voltage  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   voltage                  f32       V                                            

