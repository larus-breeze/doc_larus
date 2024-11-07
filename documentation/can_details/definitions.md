Data Types and other Definitions
===

Endianness
---
The Endianness for all data types is 'little-endian'. A little-endian system stores the least-significant byte first, at the smallest address.


Preferred Standard Data Types
---
The following data types are used as far as possible. 

    Unsigned Integers       u8, u16, u32, u64
    Signed Integers         i8, i16, i32, i64
    Bool                    true, false         u8, true = 1, false = 0
    Floating Point Numbers  f32, f64            f32::NAN [0, 0, 0xc0, 0x7f]
                                                f64::NAN [0, 0, 0, 0, 0, 0, 0xf8, 0x7f]
    Byte Arrays             u8[N]

Defined Data Types
---

    HwVersion:
        Manufacturer    u8[0]  Enumeration
        Major           u8[1]     
        Minor           u8[2]  Hw with same major and minor is firmware compatible
        Patch           u8[3]    

    FwVersion
        Major           u8[0]
        Minor           u8[1]     
        Patch           u8[2]
        Buildindex      u8[3]    

Data Types for Special Cases
---

    Unsigned Integers       u1, u2, u3, ... u64
    Signed Integers         i1, i2, i3, ... i64

Cyclic redundancy check
---
If the specification refers to a CRC that is not specified in more detail, use this one:

Uses CRC-32 (Ethernet, STM32) polynomial: 0x4C11DB7  
X32 + X26 + X23 + X22 + X16 + X 12 + X11 + X10 +X8 + X7 + X5 + X4 + X2+ X + 1

Calculation with Python:

```Python
def crc(data: bytes) -> int:
    crc=0xffffffff
    buf = bytearray()
    for b in data:
        buf.insert(0, b)
        if len(buf) == 4:
            for val in buf:
                crc ^= val << 24
                for _ in range(8):
                    crc = crc << 1 if (crc & 0x80000000) == 0 else (crc << 1) ^ 0x104c11db7
            buf = bytearray()
    return crc
```

Device Unique ID (UID)
---
The UID should be unique in the system so that the devices can be clearly distinguished. It is a 32-bit number that can be created, by generating a CRC using the controller-specific data.

Manufacturer and Hardware Versions
---
    Manufacturer

    1       Larus
    2       Air Avionics


    Hardware Releases

    Manufacturer    Name of Device      HwVersion
    ---------------------------------------------
    Larus           Sensorbox MK1, MK2  1.1.1.0
    Larus           Audiobox            1.2.1.0
    Larus           Frontend 57 V1      1.3.1.0
    Larus           Frontend 57 V2      1.3.2.0
    AirAvionics     AD57 v1             2.1.1.0
    AirAvionics     Ad57 v2             2.1.2.0
