Larus Sensor Box
===

    Name                                         larus_sensor_box                   
    Object Id                                    2                                  
    Preffered IDs for Specific Datapoints        0x200 - 0x20f                      
    Preffered IDs for Generic Datapoints         0x600 - 0x60f                      
    Comment                                      Definition of CAN bus datagrams of the Larus Sensor Box

ID 0x200 Roll Angle and Nick Angle (Front-Right-Down System)
---
Name: roll_nick  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   roll_angle               f32       rad                                          
    4   nick_angle               f32       rad                                          

ID 0x201 Heading and Magnetic Declination
---
Name: heading  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   heading                  f32       rad                                          
    4   magnetic_declination     f32       rad                                          

ID 0x202 TAS (True Airspeed) and IAS (Indicated Airspeed)
---
Name: airspeed  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   tas                      f32       m/s                                          
    4   ias                      f32       m/s                                          

ID 0x203 Vario and Vario Avarage
---
Name: vario  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x03

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   vario                    f32       m/s                                          
    4   vario_avarage            f32       m/s                                          

ID 0x204 Wind Direction and Wind Speed
---
Name: wind  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x04

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   wind_direction           f32       rad                                          
    4   wind_speed               f32       m/s                                          

ID 0x205 Avarage Wind Direction and Avarage Wind Speed
---
Name: avarage_wind  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x05

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   avarage_wind_direction   f32       rad                                          
    4   avarage_wind_speed       f32       m/s                                          

ID 0x206 Ambient Pressure and Air Density
---
Name: atmosphere  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x06

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   ambient_pressure         f32       Pa                                           
    4   air_density              f32       kg/m^3                                       

ID 0x207 Acceleration Angle Front and Angle Right
---
Name: acceleration  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x07

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   acceleration_front       f32       rad                                          
    4   acceleration_right       f32       rad                                          

ID 0x208 Turnrate and State
---
Name: turn_rate  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 5 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x08

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   turnrate_to_the_right    f32       rad/s                                        
    4   state                    u8        0 STRAIGHT_FLIGHT                            
                                           1 TRANSITION                                 
                                           2 CIRCLING                                   

ID 0x209 Calculated trift angle
---
Name: trift_angle  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x09

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   trift_angle              f32       rad, positive if track right of heading      

ID 0x20a Stystem State and GIT Tag Decimal
---
Name: system_state  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x0a

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   system_state             u32       status                                       
    4   git_tag_dec              u32       git tag                                      

ID 0x20b Supply Voltage
---
Name: voltage  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x0b

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   voltage                  f32       V                                            

ID 0x600 Heartbeat
---
Name: heartbeat  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   object_id                u16       Enumeration, see CAN Specificatiion          
    2   object_id_generation     u16       Generation of Object Id                      
    4   dev_uid                  u8[4]     DevUid                                       

ID 0x601 Hardware and Firmware Version
---
Name: version  
Object-ID Version: 0  
Type: Data Object  
Interval: if required by Remote Frame  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_version               FwVersion .                                            

ID 0x602 Set System Wide Config Item
---
Name: set_config  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   config_id                u16       Enumeration                                  
                                           0: volume_vario                              
                                           1: mac_cready                                
                                           2: water_ballast                             
                                           3: bugs                                      
                                           4: qnh                                       
    2   config_data              u8[6]     Specific to the item                         
                                           0: volume_vario:       u8 unit db, u8[5] reserved
                                           1: mac_cready:         u8[2] reserved, f32 unit m/s
                                           2: water_ballast:      u8[2] reserved, f32 unit kg
                                           3: bugs:               u8[2] reserved, f32 unit factor
                                           4: qnh:                u8[2] reserved, f32 unit Pa

ID 0xa03 Transfer of Binary Data Blocks
---
Name: blob_upload  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x403

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   upload_state             u3        0 length                                     
                                           1 crc                                        
                                           2 data                                       
                                           3 last data                                  
                                           4 request package                            
    0.3 block_count              u5        Overflowing block counter                    
    1   content                  u8[7]     upload_state 0: u8[3] reserved (=0), u32 blob_length
                                           upload_state 1: u8[3] reserved (=0), u32 crc 
                                           upload_state 2: u8[7] blob data              
                                           upload_state 3: u8[7] blob data              
                                           upload_state 4: u8[3] reserved (=0), u32 requested_block

