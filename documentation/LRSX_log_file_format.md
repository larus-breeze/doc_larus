# Larus LRSX log file format specification

The design of a log file format needs to meet the following requirements:

  * Simplicity
  * Scalability
  * Support for different data types and data blocks
  * Safety against data transmission errors

A LRSX log file contains blocks of data with different length.  
The first 32bit object of such a block is the block identifier:

  * **Identifier** 8 bits (LSB) 
  * **Length** of the record including the identifier itself in 32bit units
  * **16bit CRC** checksum of the complete record including ID and size
  * If ID=length=255 the following block has an extended length  
    described by a 32bit length filed and a extended 32bt identifier.

The data content itself can be any piece of information in 32bit chunks including
unsigned or signed 32bit objects, 32bit float objects and longer structures like 
64bit double precision numbers.

# Presently the Larus Log Files use the following **IDs**:


| **ID**|**Length**|**Description**                                                  |
|-------|----------|-----------------------------------------------------------------|
| 1  | 1 |      **LRSX file format** version, presently 1
| 10    |   32+4+32|   **System Info** Firmware GIT tag, Hardware ID, Firmware SHA256|
| 11| variable | **EEPROM-Emulation file** with all configration data
| 12 | variable | EEPROM-Emulation file single record
| 13 | 1 |     Runtime **event** marker                                              | 
| 14 | 1 |      Sensor **status** word                                               |
| 15 | 1 |      **Flight event**  (mag calibration done, air density calculated ...) |

<u> Periodic Larus Sensor data recorded with 100 Hz: </u>


| **ID**|**Length**|**Description**                                  |
|-------|----------|-------------------------------------------------|
| 20 | 13 |     **Basic sensor data**: acceleration, gyro, induction, pressures, voltage |
| 21 | 3 |       **External magnetometer** data |

<u> GNSS data recorded when updated (presently 10Hz or 13.33.. Hz): </u>


| **ID**|**Length**|**Description**                                  |
|-------|----------|-------------------------------------------------|
|30 | 13 |     **GNSS data** position, velocity, time, sat number etc |
31  | 17|     **D-GNSS data**, adding relative position and relative heading |

<u> Microphone data recorded with 4 Hz (sensors with a microphone only): </u>


| **ID**|**Length**|**Description**                                  |
|-------|----------|-------------------------------------------------|
| 35 | 27 |      **Microphone data**: IGC ENL, noise levels and third-octave spectrum |

> **Record layout of ID 35 (Microphone data)**
>
> Levels are 250 ms RMS values in dBFS,
> 0 dBFS = sine with full-scale peak (ICS-43434: 94 dB SPL = -26 dBFS).
> The record time is given by its position between the 100 Hz records.
>
> | **Word**|**Type**|**Content**                                    |
> |---------|--------|-----------------------------------------------|
> | 0     | uint32 | record counter, +1 per record since power-on (shows gaps) |
> | 1     | uint32 | ENL 0..999 (IGC), 1 s window, 10 = no noise, 0 = unserviceable |
> | 2     | uint32 | status: bit 0 no signal (constant samples: microphone missing or faulty), bits 16..31 number of 16 ms sample blocks lost (not processed in time) since power-on, saturating at 65535 |
> | 3     | float  | level after the ENL band-pass, see firmware documentation |
> | 4     | float  | broadband level: RMS of the full band |
> | 5     | float  | peak sample level: largest absolute raw sample, 0 = full scale (clipping) |
> | 6..26 | float  | third-octave bands, centers 1000 Hz * 2^(k/3), k = -16..4 (nominal 25, 31.5, 40 ... 2000, 2500 Hz) |

<u> Reserved for future crash dump or debugging files: </u>


| **ID**|**Length**|**Description**                                  |
|-------|----------|-------------------------------------------------|
| 40 | 16      | **Processor Registers** for crash dump |
| 41 | 4kbytes | **RTOS trace data** (extended record)|
| 42 | var     | **System state vector** variables |
| 43 | var     | **FLASH content** (dump) (extended record) |

