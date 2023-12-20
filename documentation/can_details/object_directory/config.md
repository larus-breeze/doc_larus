Virtual Config Device
===

    Name                                         virtual_config_device              
    Object Id                                    1                                  
    Preffered IDs for Specific Datapoints        0x3f0 - 0x3ff                      
    Preffered IDs for Generic Datapoints         0x7f0 - 0x7ff                      
    Comment                                      Config and maintain system         

ID 0x3f0 Offer Firmware Image
---
Name: sw_update  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x00

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_versin                FwVersion .                                            

ID 0x3f1 Offer Configuration Data
---
Name: device_config  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_versin                FwVersion .                                            

