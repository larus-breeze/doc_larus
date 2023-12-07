Vario Displsay
===

    Name                     vario_displsay                               
    Object Id                4                                            
    Comment                  Datagrams of a 57mm, 80mm Vario Display      

ID 0x00 Frequency, volume and duty-cycle for the sound output
---
Name: sound  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 5 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   frequency                u16       hertz                                        
    2   duty_cycle               u16       oscilations                                  
    4   volume                   u8        db                                           

ID 0x01 Recommended speed between updrafts and Mac Cready value
---
Name: speed_to_fly  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   speed_to_fly             f32       m/s                                          
    4   mac_cready               f32       m/s                                          

