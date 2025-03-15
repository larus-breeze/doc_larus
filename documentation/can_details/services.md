Services
===

Services can consist of a single datagram or a sequence of datagrams that belong together. Otherwise, situations may arise where, for example, the service provider fails in the middle of the service and the service user gets stuck in the middle of the service. For this reason, the service user must check that the service is being processed continuously to the end. A maximum pause of 100ms between related datagrams is defined as a criterion for this.

System wide Config Items
---
This [service](object_directory/generic.md) allows each device to accept or make system-wide settings. All available data points are listed here.

An example: In a two-seater, the rear pilot resets the MacCready value. The display device forwards this new value to the connected 7" display via NMEA. It also makes this data available on the CAN bus. The front display instrument adopts this date and forwards the information to the front 7" display.

Request Base ID from Master
---
This procedure has already been described in the [start up CAN bus](./start_up.md) section.

Transfer of Binary Data Blocks
---
This service makes it possible to [transfer binary data](object_directory/generic.md) of theoretically up to 4 GB. As it is not specified which data is transferred, this service can only be used as part of a higher-level service. For example, it can be used for a firmware update or for transferring a configuration.

The following example demonstrates the process. The package 'This is a test to show that everything works' is to be transferred.

This results in the following related datagrams:

    can_id: 0x03, dg.upload_state: 0, dg.length: 44
    can_id: 0x03, dg.upload_state: 1, dg.crc: 0x35727b85
    can_id: 0x03, dg.upload_state: 2, dg.block_count: 0, data: b'This is'
    can_id: 0x03, dg.upload_state: 2, dg.block_count: 1, data: b' a test'
    can_id: 0x03, dg.upload_state: 2, dg.block_count: 2, data: b' to sho'
    can_id: 0x03, dg.upload_state: 2, dg.block_count: 3, data: b'w that '
    can_id: 0x03, dg.upload_state: 2, dg.block_count: 4, data: b'everyth'
    can_id: 0x03, dg.upload_state: 2, dg.block_count: 5, data: b'ing wor'
    can_id: 0x03, dg.upload_state: 3, dg.block_count: 6, last_data: b'ks\x00\x00\x00\x00\x00''

Offer Firmware Image
---
A virtual configuration device can offer a new firmware image. If the configuration device has previously listened to the CAN bus, it can determine which firmware images are of interest for this system by listening to the heartbeats. It can now distribute different firmware images one after the other. First, the image is transferred from the configuration device to the target device. There, the compatibility and integrity of the image is checked and only then installed.

It is not part of this specification to make statements about what a firmware image should look like. Specific solutions are possible here, which only need to be known to the device itself and the configuration tool. However, these images should at least contain information on compatibility, versioning and integrity.

The procedure is as follows:
- [Offer firmware update](object_directory/config.md))
- Wait 100 ms. During this time, the interested devices confirm with an RTR without data that they are ready to download a firmware image. All other bus participants can block the data trafer can IDs
- [Service to transfer binary data](./services.md) is triggered
- After completion, the can_reset marker of the master is triggered by RTR without data. This is a signal for all bus participants to reset their CAN filter settings to the default.

The service [offers the image] with a datagram and then uses the .

Offer Configuration Data
---
A virtual configuration device can offer configuration data. If the configuration device has previously listened to the CAN bus, it can determine which configurations are of interest for this system by listening to the heartbeats.

It is not part of this specification to make statements about what a configuration definition should look like. This is open to any suitable solutions. Simple text files can be used in the same way as binary data.

The procedure is as follows:

- [Offer the configuration data](object_directory/config.md)
- Wait 100 ms. During this time, the interested devices confirm with an RTR without data that they are ready to download the configuration data. All other bus participants can block the data trafer can IDs
- [Service to transfer binary data](./services.md) is triggered
- After completion, the can_reset marker of the master is triggered by RTR without data. This is a signal for all bus participants to reset their CAN filter settings to the default.
