Start up CAN bus
===

Initially, the system is in an unconfigured state. All devices initialize their hardware and start the respective application. There is no master instance in the system. Up to 62 virtual devices can be used. 

There are two alternatives for how a device can participate in the CAN bus.
- The first is that a device works in the classic way with fixed CAN Ids. Such devices are fully integrated into the system as long as they adhere to this specification. However, such devices may only be operated once on the CAN bus, as otherwise CAN bus ID conflicts would occur.
- The second option is to work with dynamic IDs. This section describes how the negotiation of the dynamic ID address works. Such devices calculate all their CAN bus IDs from a reference address, the heartbeat. There are no restrictions on the number of participants for these devices.

1 Create a list of the Devices used in the background
---
The device activates the CAN bus receiver and keeps a list of active virtual devices on the basis of the heartbeats in the background. Based on this list and the knowledge of the heartbeat addresses that are still free, the device selects its address area at the end of the startup process.

2 Separation of the competing participants
---
The CAN bus ID range from 0x000 to 0x00f is reserved for the startup process. A device that wants to secure an ID (or several IDs) during the startup process starts at ID 0x00f. It sends a remote transmission request (RTR) without data to this address to announce its participation. It will work its way down in the process step by step (CAN bus ID 0x000). When it has reached the bottom, it reserves the desired virtual device numbers.

The process is iterative:

    a. Set the current CAN bus ID to 0x00f
    b. Send an RTR on the current CAN bus ID
    c. Wait a random time in the range of 34..67 ms
    d. Check whether other participants have sent an RTR in the two places below. 
    e. If other participants were found, continue with b.
    f. If the current CAN bus address == 0x002, end the loop and continue with the overall process
    g. If no other participants were found, reduce the current CAN bus address by 1 and continue with b.

Below is the same process as pseudo code:
```python
# Start her after initializing hardware and software. We are in unconfigured state. 

current_can_id = 0x01f

while current_can_id > 0x012:
    # send RTR
    can_send_rtr(current_can_id)

    # wait 34...67 ms
    delay_time = random(34_000, 67_000)
    delay_us(delay_time)

    # Reduce the current_can_id if no disruptive traffic is observed below
    if can_receive(id=current_can_id - 1) or can_receive(id=current_can_id - 2):
        continue
    else:
        current_can_id -= 1

# The separation process is now finished, go on...
```

3 Reserve the required Address Area
---
It is now known that it is not the turn of any other device and that exclusive access CAN bus resources is therefore possible. The Address Areas already used in the system are also known from the list created in the background. This fulfils all the prerequisites for reserving one or more Address Areas.

The device now selects suitable Address Area and sends an RTR to their heartbeat addresses to announce the requirement.

4 Confirm and switch to normal Operation
---
After one second, the device checks once again that no complete heartbeats have been sent on the Area used. If no heartbeats have been received on the corresponding Area, the Area can be used and the device now sends its heartbeats every second.

If the heartbeat of another device was received on a reserved Area, This area is abandoned and the entire process must be run through from the beginning.

Remarks
---
- The defined process initially leads to a dead time pause of around 800 ms. After this dead time, the virtual device numbers are assigned at intervals of approximately 100 ms. A fully equipped system with 62 subscribers can thus be safely put into operation in less than 10s.
- Confirmation of the selected area is used for safety. If everything always ran correctly, this step would not be necessary. It will be extremely rare for a area that has already been selected to have to be cancelled again.
- The procedure has been given the highest priority in order to prioritise the start up phase.
- The process works downwards with increasing priority. This means that in the event of conflicts between the IDs, the lower ones take priority, thus ensuring the separation process.
- No UID is required to carry out this procedure, so no conflicts can arise between two identical UIDs (very unlikely case).
- The process is designed to ensure that the devices involved react within 1 ms. This is easily feasible for controller-based solutions based on real-time systems. If a device has poorer real-time performance, more than two slots must be kept free:
  - Real-time capability < 1 ms: Keep two slots free
  - Real-time capability < 35 ms: Keep three slots free
  - Real-time capability < 70 ms: Keep four slots free
  - Real-time capability < 100 ms: Keep five slots free
- It is possible to mix devices with variable base IDs and fixed IDs. The prerequisite for this is that these devices must not be connected to the bus more than once. A preferred ID range is provided for each profile. The devices with fixed addresses work in accordance to the defined scheme, creating a closed system with a uniform structure. Devices with fixed IDs can be identified on the heartbeat in exactly the same way as those with variable IDs.
