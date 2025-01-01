Larus Sensor Box
===

    Name                                         larus_sensor_box                   
    Object Id                                    2                                  
    Preffered IDs for Specific Datapoints        0x120 - 0x12f                      
    Preffered IDs for Generic Datapoints         0x520 - 0x52f                      
    Comment                                      Definition of CAN bus datagrams of the Larus Sensor Box

ID 0x120 Roll Angle and Nick Angle (Front-Right-Down System)
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

ID 0x121 Yaw Angle and Turn Rate
---
Name: yaw_turn_rate  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   yaw                      f32       rad                                          
    4   turn_rate                f32       rad/s                                        

ID 0x122 TAS (True Airspeed) and IAS (Indicated Airspeed)
---
Name: airspeed  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   tas                      f32       m/s                                          
    4   ias                      f32       m/s                                          

ID 0x123 Vario and Vario Avarage
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

ID 0x124 Wind Direction and Wind Speed
---
Name: wind  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x04

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   wind_direction           f32       rad                                          
    4   wind_speed               f32       m/s                                          

ID 0x125 Avarage Wind Direction and Avarage Wind Speed
---
Name: avarage_wind  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x05

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   avarage_wind_direction   f32       rad                                          
    4   avarage_wind_speed       f32       m/s                                          

ID 0x126 Ambient Pressure and Air Density
---
Name: atmosphere  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x06

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   ambient_pressure         f32       Pa                                           
    4   air_density              f32       kg/m^3                                       

ID 0x127 G Force and Vertical G Force
---
Name: g_force  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x07

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   g_force                  f32       m/s^2                                        
    4   vertical_g_force         f32       m/s^2                                        

ID 0x128 Calculated Slip Angle and Pitch Angle
---
Name: slip_and_pitch_angle  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x08

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   slip_angle               f32       rad, positive if track right of heading      
    4   pitch_angle              f32       rad                                          

ID 0x129 Circle Mode and Supply Voltage
---
Name: fly_state_and_supply_voltage  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x09

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   circle_mode              u32       0 STRAIGHT_FLIGHT                            
                                           1 TRANSITION                                 
                                           2 CIRCLING                                   
    4   supply_voltage           f32       V                                            

ID 0x520 Heartbeat
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

ID 0x521 Hardware and Firmware Version
---
Name: version  
Object-ID Version: 0  
Type: Data Object  
Interval: if required by remote frame request, check exact id  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_version               FwVersion .                                            

ID 0x522 Set System Wide Config Item
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
                                           5: pilot_weight                              
                                           6: vario_mode_control                        
                                           7: tc_climb_rate                             
                                           8: tc_speed_to_fly                           
    2   config_data              u8[6]     Specific to the item                         
                                           0: volume_vario:       u8 unit db, u8[5] reserved
                                           1: mac_cready:         u8[2] reserved, f32 unit m/s
                                           2: water_ballast:      u8[2] reserved, f32 unit fraction
                                           3: bugs:               u8[2] reserved, f32 unit factor
                                           4: qnh:                u8[2] reserved, f32 unit Pa
                                           5: pilot_weight:       u8[2] reserved, f32 unit kg
                                           6: vario_mode_control  u8: 0 Vario, 1 SpeedToFly, 2 Auto
                                           7: tc_climb_rate:      u8[2] reserved, f32 unit s
                                           8: tc_speed_to_fly:    u8[2] reserved, f32 unit s

ID 0x523 Transfer of Binary Data Blocks
---
Name: blob_upload  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x03

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   upload_state             u3        0 type_of_transmission                       
                                           1 length                                     
                                           2 crc                                        
                                           3 data                                       
                                           4 last data                                  
                                           5 ack_transmission                           
    0.3 block_count              u5        block counter                                
    1   content                  u8[7]     upload_state 0: u8[3] reserved (u8=0), u32 type_of_transmission
                                           upload_state 1: u8[3] reserved (u8=0), u32 blob_length
                                           upload_state 2: u8[3] reserved (u8=0), u32 crc
                                           upload_state 3: u8[7] blob data              
                                           upload_state 4: u8[7] blob data              
                                           upload_state 5: u8[3] reserved (=0), u32 requested_block
                                           _                                            
                                           Type of transmission:                        
                                           0 NMEA GPS data                              
                                           1 NMEA Flarm data                            
                                           2 Larus configuration data                   
                                           3 Larus firmware image                       

