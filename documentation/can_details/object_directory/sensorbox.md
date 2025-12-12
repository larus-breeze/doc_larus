Larus Sensor Box
===

    Name                                         larus_sensor_box                   
    Object Id                                    2                                  
    Preffered IDs for Specific Datapoints        0x120 - 0x12f                      
    Preffered IDs for Generic Datapoints         0x520 - 0x52f                      
    Comment                                      Definition of CAN bus datagrams of the Larus Sensor Box

The Larus sensor box provides various sensor data such as wind direction and speed or instantaneous rise/fall. There is a maximum of one Larus sensor box in a CAN bus system.

ID 0x120 Roll Angle and Pitch Angle (Front-Right-Down System)
---
Name: roll_pitch  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   roll_angle               f32       rad                                          
    4   pitch_angle              f32       rad                                          

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
    0   yaw                      f32       rad   equals true heading                    
    4   turn_rate                f32       rad/s projected on a horizontal plane in NED system

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

ID 0x128 Apperent vertical angles, Roll and Pitch
---
Name: apperent_roll_and_pitch  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x08

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   roll_angle               f32       rad, apperent roll, filtered                 
    4   pitch_angle              f32       rad, apperent pitch, filtered                

ID 0x129 Supply Voltage and Circle Mode
---
Name: fly_state_and_supply_voltage  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 5 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x09

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   supply_voltage           f32       V                                            
    4   circle_mode              u8        0 STRAIGHT_FLIGHT                            
                                           1 TRANSITION                                 
                                           2 CIRCLING                                   
                                           3 ON GROUND                                   

ID 0x12a System State and Git Tag
---
Name: system_state_and_git_tag  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x0a

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   system_state             u32       Bit field                                            
                                           0x0000_0001 GNSS_AVAILABLE
                                           0x0000_0002 D_GNSS_AVAILABLE

                                           0x0000_0004 GNSS_VELOCITY_ACCURACY_BAD
                                           0x0000_0008 MAGNETIC_DISTURBANCE_BAD

                                           0x0000_0010 MTI_SENSOR_AVAILABE
                                           0x0000_0080 MS5611_STATIC_AVAILABLE
                                           0x0000_0200 PITOT_SENSOR_AVAILABLE
                                           0x0000_0400 AMBIENT_AIR_SENSOR_AVAILABLE
                                           0x0000_0800 EXTERNAL_MAGNETOMETER_AVAILABLE

                                           0x0001_0000 HORIZON_NOT_AVAILABLE

    4   git_tag                  u32       tag                            

ID 0x12b GNSS and AHRS Data Quality
---
Name: sensor_health
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes
Dynamic Id: Id(Heartbeat) - 0x400 + 0x0b

    No  Datapoint                Type      Unit / Comment
    --------------------------------------------------------------------------------------------
    0   magnetic_disturbance     f32       Magnetic disturbance 0..2 (lower is better)
    1   speed_accuracy           f32       Speed accuracy as reported by GNSS receiver 0..inf. (lower is better)
´

ID 0x12f Send config value on request
---
Name: config_value  
Object-ID Version: 0  
Type: Data Object  
Interval: 0 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x0f

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   config_id                u32       .                                            
    4   config_value             f32, u32  Specific to the config_id                    
                                           0x2000: sens_tilt_roll      f32 unit rad     
                                           0x2001: sens_tilt_pitch     f32 unit rad     
                                           0x2002: sens_tilt_yaw       f32 unit rad     
                                           0x2003: pitot_offset        f32 unit Pa      
                                           0x2004: pitot_span          f32 unit -       
                                           0x2005: qnh_delta           f32 unit Pa      
                                           0x2006: mag_auto_calib      f32 0 OFF 1 ON 2 WITH_SOFT_IRON_COMPENSATION
                                           0x2007: vario_tc            f32 unit s       
                                           0x2008: vario_int_tc        f32 unit s       
                                           0x2009: wind_tc             f32 unit s       
                                           0x200a: mean_wind_tc        f32 unit s       
                                           0x200b: gnss_config         f32 0 SGNSS 1 DGNSS
                                           0x200c: ant_baselen         f32 unit m       
                                           0x200d: ant_slave_down      f32 unit m       
                                           0x200e: ant_slave_right     f32 unit m       
                                           0x200f: vario_press_tc      f32 unit s       

ID 0x520 Heartbeat and other generic data points are defined in [this specification](generic.md).
---
