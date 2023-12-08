Virtual Master Device
===

    Name                     virtual_master_device                        
    Object Id                0                                            
    Comment                  System Organizer                             

ID 0x01 Response to the Request for a Base ID
---
Name: assign_base_id  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   base_id                  u8        Base ID, range 1..63                         
    1   reserved                 u8[3]     .                                            
    4   device_uid               u8[4]     Unique ID of the device                      

ID 0x02 No data, marker; request to reset all filters
---
Name: can_reset  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 0 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------

