Virtual Config Device
===

    Name                     virtual_config_device                        
    Object Id                1                                            
    Comment                  Config and maintain system                   

ID 0x00 Offer Firmware Image
---
Name: sw_update  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_versin                FwVersion .                                            

ID 0x01 Offer Configuration Data
---
Name: device_config  
Object-ID Version: 0  
Type: Service  
Interval: if required  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   hw_version               HwVersion .                                            
    4   fw_versin                FwVersion .                                            

