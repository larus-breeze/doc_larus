GPS
===

    Name                                         gps                                
    Object Id                                    3                                  
    Preffered IDs for Specific Datapoints        0x220 - 0x22f                      
    Preffered IDs for Generic Datapoints         0x620 - 0x62f                      
    Comment                                      Definition of CAN bus datagrams of a GPS Receiver

ID 0x220 Date and Time
---
Name: date_time  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
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

ID 0x221 Latitude
---
Name: latitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   latitude                 f64       rad                                          

ID 0x222 Longitude
---
Name: longitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 4 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   longitude                f64       rad                                          

ID 0x223 MSL Altitude and Geo Separation
---
Name: altitude  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x03

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   altitude                 f32       m                                            
    4   geo_separation           f32       m                                            

ID 0x224 Ground Track and Ground Speed
---
Name: track_speed  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x04

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   gnd_track                f32       rad                                          
    4   gnd_speed                f32       m/s                                          

ID 0x225 Number of Sattelites, Fix valid and Heading valid
---
Name: satellites  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 3 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x05

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   number_of_sats           u8        .                                            
    1   sat_fix_valid            bool      .                                            
    2   sat_heading_valid        bool      .                                            

ID 0x620 Heartbeat
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

ID 0x621 Hardware and Firmware Version
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

ID 0x622 Set System Wide Config Item
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
    2   config_data              u8[6]     Specific to the item                         
                                           0: volume_vario:       u8 unit db, u8[5] reserved
                                           1: mac_cready:         u8[2] reserved, f32 unit m/s
                                           2: water_ballast:      u8[2] reserved, f32 unit kg
                                           3: bugs:               u8[2] reserved, f32 unit factor
                                           4: qnh:                u8[2] reserved, f32 unit Pa
                                           5: pilot_weight:       u8[2] reserved, f32 unit kg

ID 0x623 Transfer of Binary Data Blocks
---
Name: blob_upload  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) + 0x03

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

