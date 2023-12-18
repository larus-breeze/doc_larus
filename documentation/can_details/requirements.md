Requirements
===

RQ1 Measurement and Operating Values
---
It should be possible to transmit all measurement and operating values from all devices on the CAN bus at any time

RQ2 Adjust System Settings
---
It must be possible to change all system-wide defined settings from any device in a defined manner. Examples of such settings are McCready value, volume of the vario, radio frequency, etc. 

RQ3 Software Update
---
The system must allow software updates via the CAN bus. The process must be specified uniformly for all devices.

RQ4 Upload and Download of Configurations
---
The system must allow configuration data to be loaded to and from the devices. These processes must be specified uniformly for all devices.

RQ5 Number of Bus Participants
---
Up to 60 devices should be supported on the CAN bus

RQ6 Behaviour in Normal Operation
---
During normal operation, all devices should be able to communicate at all times without collisions occurring.

RQ7 Real-Time Requirements
---
Real-time requirements must be clearly defined. While devices based on microcontrollers can cope well with a maximum response time of 1 ms, devices with operating systems such as Android, Windows or Linux cannot fulfil such real-time requirements. However, as such systems participate, it must be possible to utilise all the functions of the system with a maximum response time of up to 100ms.

RQ8 Device Types and Dealing with Conflicts
---
It must be possible to operate several devices with identical software on one CAN bus. It must be generally defined how any ID conflicts are to be handled.

RQ9 Start-up Phase
---
There may be a start-up phase to resolve possible conflicts before entering normal operation This phase may last a maximum of 10 seconds.

RQ10 Device Identification
---
There must be a procedure that can be used to determine which devices are active on the bus within 5 seconds during normal operation.

RQ11 Hardware and Software Version
---
Hardware and software versions must be communicated in a standardised manner.

RQ12 Bus Participants
---
Communication via the CAN bus must be able to be recognised by systems based on a microcontroller in the same way as by complex systems based on Android, Linux or Windows.

RQ13 Testability
---
It should be possible to reproduce and test all processes using a test script on a host PC. 
 