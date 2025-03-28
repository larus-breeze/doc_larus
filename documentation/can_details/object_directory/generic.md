Gneric Data
===

The generic IDs are defined in the same way for all devices. The underlying functions are available regardless of the device. For example, this enables the firmware update of the device or the general option of setting genral parameters such as vario volume. 

The ID range for the generic data is 0x400 to 0x7ff. Up to 16 data points are available for each device. All devices can use their generic functions without having to take other devices into account. 

The data can be easily evaluated by a receiver. If the CAN Id of a datagram is > 0x400, it is a generic datagram that is known system-wide. The exact content can be determined by logical and ID with 0x00f. The ID of the generic datagram is obtained in the range from 0x00 to 0x0f.

Generic ID 0x00 Heartbeat
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

The heartbeat identifies a device. The object ID reveals which functions the device contains. There may be real devices that represent several virtual devices. For example, the Larus Sensbox is active as a sensor box and as a GPS device and therefore occupies the CAN IDs of two devices.

The heartbeat identifies a device. The object ID reveals which functions the device contains. The object ID generation shows the number of extensions of the original definition. Higher generations are backwards compatible, i.e. they have identical functions to the original devices. The appliance UUID uniquely identifies the specific appliance,

There may be real devices that represent several virtual devices. For example, the Larus Sensbox is active as a sensor box and as a GPS device and therefore occupies the CAN IDs of two devices.

Generic ID 0x01 Hardware and Firmware Version
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

Generic ID 0x02 Set System Wide Config Item
---
Name: set_config  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   config_id                u16       <Generic Config Data>                        
                                           0x0000: volume_vario                         
                                           0x0001: mac_cready                           
                                           0x0002: water_ballast                        
                                           0x0003: bugs                                 
                                           0x0004: qnh                                  
                                           0x0005: pilot_weight                         
                                           0x0006: vario_mode_control                   
                                           0x0007: tc_climb_rate                        
                                           0x0008: tc_speed_to_fly                      
                                           .                                            
                                           <Generic Command>                            
                                           .                                            
                                           <Specific Config Data>                       
                                           0x2000: sens_tilt_roll (Sensor Box)          
                                           0x2001: sens_tilt_pitch (Sensor Box)         
                                           0x2002: sens_tilt_yaw (Sensor Box)           
                                           0x2003: pitot_offset (Sensor Box)            
                                           0x2004: pitot_span (Sensor Box)              
                                           0x2005: qnh_delta (Sensor Box)               
                                           0x2006: mag_auto_calib (Sensor Box)          
                                           0x2007: vario_tc (Sensor Box)                
                                           0x2008: vario_int_tc (Sensor Box)            
                                           0x2009: wind_tc (Sensor Box)                 
                                           0x200a: mean_wind_tc (Sensor Box)            
                                           0x200b: gnss_config (Sensor Box)             
                                           0x200c: ant_baselen (Sensor Box)             
                                           0x200d: ant_slave_down (Sensor Box)          
                                           0x200e: ant_slave_right (Sensor Box)         
                                           .                                            
                                           <Specific Command>                           
                                           0x3000: cmd_measure_pos_1 (Sensor Box)       
                                           0x3001: cmd_measure_pos_2 (Sensor Box)       
                                           0x3002: cmd_measure_pos_3 (Sensor Box)       
                                           0x3003: cmd_calc_sensor_orientation (Sensor Box)
                                           0x3004: cmd_fine_tune_calibration (Sensor Box)
                                           0x3005: cmd_reset_cold_start (Sensor Box)

    2   config_data              u8[6]     Specific to the config_id                    
                                           <Generic Config Data>                        
                                           0x0000: volume_vario:       u8 unit db, u8[5] reserved
                                           0x0001: mac_cready:         u8[2] reserved, f32 unit m/s
                                           0x0002: water_ballast:      u8[2] reserved, f32 unit fraction
                                           0x0003: bugs:               u8[2] reserved, f32 unit factor
                                           0x0004: qnh:                u8[2] reserved, f32 unit Pa
                                           0x0005: pilot_weight:       u8[2] reserved, f32 unit kg
                                           0x0006: vario_mode_control  u8: 0 Vario, 1 SpeedToFly, 2 Auto
                                           0x0007: tc_climb_rate:      u8[2] reserved, f32 unit s
                                           0x0008: tc_speed_to_fly:    u8[2] reserved, f32 unit s
                                           .                                            
                                           <Generic Command>                            
                                           .                                            
                                           <Specific Config Data>                       
                                           0x2000: sens_tilt_roll      u8 0 get 1 set, u8 reserved, f32 unit rad
                                           0x2001: sens_tilt_pitch     u8 0 get 1 set, u8 reserved, f32 unit rad
                                           0x2002: sens_tilt_yaw       u8 0 get 1 set, u8 reserved, f32 unit rad
                                           0x2003: pitot_offset        u8 0 get 1 set, u8 reserved, f32 unit Pa
                                           0x2004: pitot_span          u8 0 get 1 set, u8 reserved, f32 unit -
                                           0x2005: qnh_delta           u8 0 get 1 set, u8 reserved, f32 unit Pa
                                           0x2006: mag_auto_calib      u8 0 get 1 set, u8 reserved, f32 0, 1 
                                           0x2007: vario_tc            u8 0 get 1 set, u8 reserved, f32 unit s
                                           0x2008: vario_int_tc        u8 0 get 1 set, u8 reserved, f32 unit s
                                           0x2009: wind_tc             u8 0 get 1 set, u8 reserved, f32 unit s
                                           0x200a: mean_wind_tc        u8 0 get 1 set, u8 reserved, f32 unit s
                                           0x200b: gnss_config         u8 0 get 1 set, u8 reserved, f32 0, 1
                                           0x200c: ant_baselen         u8 0 get 1 set, u8 reserved, f32 unit m
                                           0x200d: ant_slave_down      u8 0 get 1 set, u8 reserved, f32 unit m
                                           0x200e: ant_slave_right     u8 0 get 1 set, u8 reserved, f32 unit m
                                           .                                            
                                           <Specific Command>                           
                                           0x3000: cmd_measure_pos_1             u8[6] reserved
                                           0x3001: cmd_measure_pos_2             u8[6] reserved
                                           0x3002: cmd_measure_pos_3             u8[6] reserved
                                           0x3003: cmd_calc_sensor_orientation   u8[6] reserved
                                           0x3004: cmd_fine_tune_calibration     u8[6] reserved
                                           0x3005: cmd_reset_cold_start          u8[6] reserved

Generic ID 0x03 Transfer of Binary Data Blocks
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

