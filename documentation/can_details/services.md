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
