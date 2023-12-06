Normal Operation
===

Identification of interesting communication partners
---
The device is now in the "configured" state and continuously checks that the heartbeats from the master are still being received. If this is no longer the case, the device reverts to the "unconfigured" state and continues as described in the Start up CAN bus section.

The next step is to clarify which partners are available on the CAN bus. This can be easily determined by evaluating their [heartbeats](object_directory/generic.md#id-0x00-show-who-you-are-that-you-live-and-where-you-live), as these are sent on the known, generically defined CAN bus IDs. In the heartbeat, the partners communicate which functions and data points they provide (object ID and version). 

Coninous Operation
---
The device memorises the partners of interest and continuously monitors whether they are still active and sending heartbeats. If the heartbeat of a communication partner fails for longer than 3 seconds, it is deleted from the list and alternatives are searched for.

The device is now configured and recognises its communication partners. It is fully integrated into the communication process and can send and receive data as required. There are no conflicts as the ID ranges were clearly assigned during start-up.

Heartbeat
---
Each device sends a [heartbeat](object_directory/generic.md#id-0x00-show-who-you-are-that-you-live-and-where-you-live) every second. This datagram contain informations about datapoints and functions this device provides. The address ranges of this device can also be derived:
- Generic range can_id ... can_id + 0x00f
- Specific range (can_id - 0x400) ... (can_id - 0x400 + 0x00f)

The object_id specifies the available functions and data. All devices are listed in the [object directory](../can_spec#object-directory). The devices now know their potential communication partners and their functions. The Hartbeat telegram alternately contains the hardware version, the firmware version and the unique device ID (UID).

Special situations
---
Special situations may arise during operation. For example, the device may need to be re-parameterised or new firmware may be provided. These functions are provided by the virtual configuration device. As this device only exists once in the system and its CAN bus ID is known a priori, it can be communicated with directly without any further steps.
