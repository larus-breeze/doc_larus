# LARUS Protocol **Version 0.1.1**

This document describes the LARUS serial port protocol, as realized in [sw_sensor_algorithm 2023-08-18](https://github.com/larus-breeze/sw_sensor_algorithms/blob/17e8b49139d2c820dce6f02208cf5205ff22e62a/Output_Formatter/NMEA_format.cpp).

The Larus sensor system can provide more information than the sensors that have been used in former navigation computers for gliders. Therefore the protocols need to be extended to be able to transfer new messages.

## Specification

NMEA specification in short form [see also NMEA Revealed](https://gpsd.gitlab.io/gpsd/NMEA.html) by Eric S. Raymond:

Data is transmitted in serial async, 1 start-bit, 8 data-bits, 1 stop-bit, no parity. Data-bits are in least-significant-bit order. An NMEA sentence consists of a start delimiter, followed by a comma-separated sequence of fields, followed by the character '*', the checksum and an end-of-line marker <CR><LF>. The checksum is the representation of two hexadecimal characters of an XOR of all characters in the sentence between – but not including – the $ and the * character.

The start delimiter is normally '$'. The first field of a sentence is called the "tag" and normally consists of a two-letter talker ID followed by a three-letter type code. Sentences are terminated by a <CR><LF> sequence. Maximum sentence length, including the $ and <CR><LF> is 82 bytes.

The Larus Flight Information Sensor System for Gliders provides essential information for glider navigation like

- Position and Time (Just the standard GPS stuff)
- Attitude and Heading (AHRS)
- GNSS/INS-based ultra-fast variometer and DSP-filtered average variometer
- Real-time wind measurement
- Air-density measurement

For the GNSS position, regular NMEA 0183 sentences are used

  1. $GPRMC Recommended Minimum Navigation Informatioin
  2. $GPGGA Global Positioning System Fix Data
  3. $HCHDT True Heading

For the aircraft attitude, wind, and air density information, some supplementary data points were included. 
The additions can be found in the protocol around the `$PLARx` NMEA sentences. 
The `x` is 

  1) `W` when wind information is being sent
  2) `A` when attitude information is sent
  3) `D` for the instant air density
  4) `B` for battery voltage
  5) `V` for climb rate (vario), pressure altitude and true air speed (TAS)

## Regular NMEA 0183 Sentences

### $GPRMC Recommended Minimum Navigation Informatioin

           1         2 3          4 5          6 7     8     9        12 13
           |         | |          | |          | |     |     |        |  |
    $GPRMC,hhmmss.ss,a,xxxx.xxxxx,a,xxxx.xxxxx,a,xxx.x,xxx.x,ddmmyy,,,a*hh<CR><LF>

    Example:
    $GPRMC,134943.69,A,4829.57602,N,1026.79034,E,057.0,081.9,170623,,,A*67

Minimum navigation informatioin

  1) Universal Time Coordinated (UTC) hhmmss.ss
  2) Status, V = Navigation receiver warning
  3) Latitude
  4) N or S
  5) Longitude
  6) E or W
  7) Speed over ground, knots
  8) Track made good, degrees true
  9) Date, ddmmyy
  10) Magnetic Variation, degrees (empty)
  11) E or W (empty)
  12) Signal integrity (A -> autonomous mode)
  13) Checksum

### $GPGGA Global Positioning System Fix Data

           1         2          3 4          5 6 7  8   9      10 11  12  15
           |         |          | |          | | |  |   |      |  |   |   |
    $GPGGA,hhmmss.ss,xxxx.xxxxx,a,xxxx.xxxxx,a,x,xx,x.x,xxxx.x,a,xx.x,a,,*hh<CR><LF>

    Example:
    $GPGGA,134943.69,4829.57602,N,1026.79034,E,1,24,1.0,2702.7,M,47.3,M,,*61

Global Positioning System Fix Data, Time, Position and fix related data for a GPS receiver

  1) Universal Time Coordinated (UTC)  hhmmss.ss
  2) Latitude
  3) N or S (North or South)
  4) Longitude
  5) E or W (East or West)
  6) GPS Quality Indicator,
     0 - fix not available,
     1 - GPS fix,
     2 - Differential GPS fix
  7) Number of satellites in view, 00 - 12
  8) Horizontal Dilution of precision
  9) Antenna Altitude above/below mean-sea-level (geoid) 
  10) Units of antenna altitude, meters
  11) Geoidal separation, the difference between the WGS-84 earth
     ellipsoid and mean-sea-level (geoid), "-" means mean-sea-level
     below ellipsoid
  12) Units of geoidal separation, meters
  13) Age of differential GPS data, time in seconds since last SC104
     type 1 or 9 update, null field when DGPS is not used (empty)
  14) Differential reference station ID, 0000-1023 (empty)
  15) Checksum

### $HCHDT True Heading

           1    2  3
           |    |  |
    $HCHDT,xx.x,a,*hh<CR><LF>

    Examples:
    $HCHDT,69.2,T*14

Report true heading:

  1) Heading Degrees
  2) T = True
  3) Checksum

## Propietary Larus NMEA sentences

### $PLARW Wind

           1   2  3 4 5
           |   |  | | |
    $PLARW,xxx,xx,a,a*hh<CR><LF>

    Examples:
    $PLARW,288,29,I,A*69
    $PLARW,288,29,A,A*61

This sentence gives information about the both the average and instantaneous wind. The different fields have the following meaning:
 
  1) Wind Angle, 0 to 360 degrees
  2) Wind Speed, kph
  3) (A)verage or (I)nstantaneous wind
  4) Status, A = Data Valid
  5) Checksum

### $PLARA Attitude

           1    2   3    4
           |    |   |    |  
    $PLARA,xx.x,x.x,xx.x*hh<CR><LF>

    Example:
    $PLARA,27.5,4.0,69.2*45

This sentence gives information about the current attitude. The different fields have the following meaning:

  1) Roll angle (degrees, positive while turning right)
  2) Pitch angle (degrees, positive when nose up)
  3) Yaw angle (degrees, true heading)
  4) Checksum

### $PLARD Instant air density

           1      2 3
           |      | |  
    $PLARD,xxxx.x,a*hh<CR><LF>

    Example:
    $PLARD,922.54,M*10

This sentence gives information about the instant air density at the current altitude. The different fields have the following meaning:

  1) Instant air density in g/m^3.
  2) a = (M)easured or (E)stimated
  3) Checksum

### $PLARB Battery Voltage

           1     2
           |     |  
    $PLARB,xx.xx*hh<CR><LF>
    
    Example:
    $PLARB,12.33*4C

This block gives the measured voltage:

  1) Volatage in volts
  2) Checksum

### $PLARV Climb Rate (Vario), Pressure Altitude and True Air Speed (TAS)

           1    2    3    4  5
           |    |    |    |  |
    $PLARV,x.xx,x.xx,xxxx,xx*hh<CR><LF>
    
    Example:
    $PLARV,1.46,2.98,2608,90*5C

This sentence fives climb rate (vario), pressure altitude and true air speed (TAS):

  1) Climb rate (vario) in m/s
  2) Averaged climb rate (avg vario) in m/s
  3) Pressure altitude in m
  4) TAS in kph
  5) Checksum
