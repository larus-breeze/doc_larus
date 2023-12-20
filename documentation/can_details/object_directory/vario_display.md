Vario Displsay
===

    Name                                         vario_displsay                     
    Object Id                                    4                                  
    Preffered IDs for Specific Datapoints        0x280 - 0x28f                      
    Preffered IDs for Generic Datapoints         0x680 - 0x68f                      
    Comment                                      Datagrams of a 57mm, 80mm Vario Display

ID 0x280 Frequency, volume and duty-cycle for the sound output
---
Name: sound  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 6 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   frequency                u16       hertz                                        
    2   duty_cycle               u16       oscilations                                  
    4   volume                   u8        db                                           
    5   continuous               bool      true, false                                  

ID 0x281 Recommended speed between updrafts and Mac Cready value
---
Name: speed_to_fly  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   speed_to_fly             f32       m/s                                          
    4   mac_cready               f32       m/s                                          

ID 0x680 Heartbeat
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

ID 0x681 Hardware and Firmware Version
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

ID 0x682 Set System Wide Config Item
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

ID 0x683 Transfer of Binary Data Blocks
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

