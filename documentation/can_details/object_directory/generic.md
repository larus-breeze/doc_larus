Generic Datapoints and Services
===

    Name                     generic_datapoints_and_services              
    Object Id                .                                            
    Comment                  Generic CAN bus datagrams, usable for any device

ID 0x00 Show who you are, that you live and where you live
---
Name: heartbeat  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   object_id                u16       Enumeration, see CAN Specificatiion          
    2   object_id_generation     u16       Generation of Object Id                      
    4   dev_uid                  u8[4]     DevUid                                       

ID 0x01 Hardware and Firmware Version
---
Name: version  
Type: Data Object  
Interval: if required by Remote Frame  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_version               FwVersion .                                            

ID 0x02 Set System Wide Config Item
---
Name: set_config  
Type: Service  
Interval: if required  
Length: 8 Bytes

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

ID 0x03 Request a Base ID from the Master
---
Name: request_base_id  
Type: Service  
Interval: at start-up  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   desired_priority         u8        0 Low                                        
                                           1 Medium                                     
                                           2 High                                       
    1   reserved                 u8[3]     .                                            
    4   device_uid               u8[4]     Unique ID of the device                      

ID 0x04 Transfer of Binary Data Blocks
---
Name: blob_upload  
Type: Service  
Interval: if required  
Length: 8 Bytes

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

