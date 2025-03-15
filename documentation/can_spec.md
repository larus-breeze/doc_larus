DRAFT! In advance
===

A glance under the cover of the instruments in a modern glider reveals an impressive tangle of cables. The wiring of the electronic components is complex and prone to errors. Components from different manufacturers work poorly together and the technologies used (especially IGC RS 232) are outdated and inefficient.

Inexpensive technologies are available today that solve such problems. The CAN bus theoretically makes it possible to connect all electronic devices. This makes a system conceivable that places all information and control commands on the bus and would therefore be available for all components. Sensors such as the GPS receiver would only need to be installed in one place. All connected devices could access all data.

The CAN bus is used by various manufacturers. However, there is no suitable, universally valid and open specification that can be used regardless of the manufacturer. This paper attempts to show a way to achieve this. Everyone is invited to use and improve this technology.

System description
---
[Requirements](can_details/requirements.md)  
[Terms and Basics](can_details/terms_and_basics.md)  
[Start up](can_details/start_up.md)  
[Normal Operation](can_details/normal_operation.md)  
[Services](can_details/services.md)

General Information
---
[Data Types and other Definitions](can_details/definitions.md)  
[Arbitration Services](can_details/object_directory/arbitration.md)  
[Virtual Config Device](can_details/object_directory/config.md)  

Object Directory
---
[Larus Sensorbox](can_details/object_directory/sensorbox.md)  
[Generic GPS Device](can_details/object_directory/gps.md)  
[Vario Display](can_details/object_directory/vario_display.md)    
[Generic Data](can_details/object_directory/generic.md)    
