Vario Displsay
===

    Name                                         vario_displsay                     
    Object Id                                    4                                  
    Preffered IDs for Specific Datapoints        0x280 - 0x28f                      
    Preffered IDs for Generic Datapoints         0x680 - 0x68f                      
    Comment                                      Datagrams of a 57mm, 80mm Vario Display

The vario display shows the values of the Larus sensor box. It also offers additional information such as speed to fly or a thermal assistant. The values are shown on an LCD display or output acoustically via a loudspeaker. The device can function as a vario display, also as a display of the artificial horizon or flarm display.

Several such devices can be installed. The ID assignment is carried out according to the procedure described in the specification. The first GPS device works with the specific IDs 0x280...0x28f and the generic IDs 0x680..0x68f.

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

ID 0x281 Voltage measured by device an PCB temperature
---
Name: volt_temp  
Object-ID Version: 0  
Type: Data Object  
Interval: 1000 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x01

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   voltage                  f32       V                                            
    4   temperature              f32       °C                                           

ID 0x282 avg climb rate and thermal climb rate only sent when virtual master
---
Name: avg_climb_rates  
Object-ID Version: 0  
Type: Data Object  
Interval: 100 ms  
Length: 8 Bytes  
Dynamic Id: Id(Heartbeat) - 0x400 + 0x02

    No  Datapoint                Type      Unit / Comment                               
    --------------------------------------------------------------------------------------------
    0   avg_climb_rate           f32       m/s                                          
    4   thermal_climb_rate       f32       m/s                                          

ID 0x680 Heartbeat and other generic data points are defined in [this specification](generic.md).
---