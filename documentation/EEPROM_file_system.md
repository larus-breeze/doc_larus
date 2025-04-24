# EEPROM file system for permanent setup data

The design of a file system for the storage of the permanent setup parameters  
needs to meet the following requirements:

  * Simplicity
  * Scalability
  * Support for different data types
  * Minimize FLASH wear out 
  * Safety against data loss and bit errors

The following file format is used:  
Each file (= data set) starts with a 32 bit file descriptor:  

8 bit: **Size** of the data set in 32bit units including descriptor (1..254 32 bit words)

8 bit: **Type** identifier 

16 bit: **Direct data** if applicable (data set size 1)
       or 16bit **checksum** of the complete data set information

If some data set is overwritten, the same file is just written again.  
No deletion is performed. So, when reading, the last data set of the   
wanted file type needs to be found and used.

There is no garbage collection. 

The file system uses two flash blocks. If a flash block has been filled  
up completely, the latest information is copied to the other block and the  
block is then erased using the micro-controllers flash block erase mechanism. 

For the Larus project the following **data types** are used:  

 0. Format for future type extensions (details coded within the file)
 1. Sensor orientation rpy 3 * float32_t angles (rad)
 2. Pitot offset float32_t (Pa)
 3. Pitot span (1.0)
 4. QNH offset (Pa)
 5. Magnetic automatic calibration type: enum within descriptor (16bit) {none, auto1d, auto3d, auto3d+soft-iron-correction}
 6. Magnetic calibration information:  float32_t: 3 * (offset, span), std deviation
 7. Soft iron correction parameters: 22 * float32_t
 8. Vario TC (s)
 9. vario integrator TC (s)
 10. Wind TC (s)
 11. Average wind TC (s)
 12. GNSS configuration: enum within descriptor (16bit): M9N, F9P+F9P, F9P+F9H, ...
 13. GNSS antennas base-lenght
 14. GNSS antennas down parameter
 15. GNSS antennas right parameter
 16. External magnetic sensor calibration parameters: 16 * float32_t (=sensor transfer matrix)

Type 255 is not used (= erased FLASH cell).

Additional data types can be added in the future if necessary.

**Migration path**: 

If the sensor finds the old format it uses the second flash block to write the converted new information.
Then the first flash block is erased.

