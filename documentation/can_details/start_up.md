Start up CAN bus
===

Initially, the system is in an unconfigured state. All devices initialize their hardware and start the respective application. The device that represents the virtual master now starts to send its heartbeat.

All other devices wait until they receive the heartbeat from the virtual master. The devices that have not yet been configured ans start to request a base device ID from the master. The procedure is as follows:
- Wait 0..200 ms (random time with µ-second resolution)
- Generate a random number P between 0 and 63
- Calculate the CAN bus ID for the request: can_id = 0x402 + (P << 4)
- [Request a base ID](object_directory/generic.md#id-0x02-request-a-base-id-from-the-master) from the master 
- Wait 10 ms
- [Receive base ID](object_directory/master.md#id-0x01-response-to-the-request-for-a-base-id)? yes: ready, no: start from the beginning 

The process is shown again below as Python pseudo code

```python
# Start her after initializing hardware and software. We are in unconfigured state. 

# Wait for the heartbeat of the master
while True:
    if heartbeat_master_recieved():
        break
    delay_us(10_000) # wait 10 ms

# Get base_id
while True:
    # Wait 0..200 ms
    delay_time = random(0, 200_000)
    delay_us(delay_time)

    # Generate base-id request
    p = random(0, 64)
    can_id = 0x402 + (p << 4)
    # PRIO_MEDIUM = 1, DEV_UID is calculated from the UID of the stm32 chip
    can_dg = RequestBaseIdDg(can_id, PRIO_MEDIUM, DEV_UID)
    can_send(can_dg)

    # Receive answer from master and stop waiting, if base_id received
    delay_us(10_000)
    can_dg = can_recieve(id=0x001)
    if (can_dg is not None) and (can_dg.uid() == DEV_UID):
        base_id = can_dg.base_id()
        break 

# Continue, we are now in the configured state with base_id and can communicate as required.
```
Conflicts can occur when obtaining the base ID because we randomly use CAN bus IDs that could also be used by other devices. The procedure described reduces the probability on the one hand by the random waiting time and on the other hand by the random selection of a base ID for the generically defined base ID request datagram. In the unlikely event of a conflict, the process is repeated.

The devices must constantly monitor that the master is still active. If this is no longer the case, the device reverts to the "unconfigured" state after 3 seconds and will attempt to obtain a base ID again.
