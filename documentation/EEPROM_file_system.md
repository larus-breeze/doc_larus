# EEPROM file system for permanent setup data

The design of a file system for the storage of the permanent setup parameters  
needs to meet th following requirements:

  * Simplicity
  * Scalability
  * Support for different data types
  * Minimize FLASH wear out 
  * Safety against data loss and bit errors

The following file format is used:  
Each file (=data set) starts with a 32 bit file descriptor:  

8 bit: **Size** of the data set in 32bit units including descriptor (1..254 32 bit words)

8 bit: **Type** identifier 

16 bit: **Direct data** if applicapble (data set size 1)
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
 2. Pressure sensor offsets 3 * float32_t items (Pa): Pitot offset, pitot span, QNH offset
 3. Magnetic automatic calibration type: enum uint32_t none, auto1d, auto3d, auto3d+soft-iron-correction
 3. Magnetic calibration information:  float32_t: 3 * (offset, span), std deviation
 4. Soft iron correction parameters: 22 * float32_t
 5. User-selectable time constants (float32_t (s)): vario tc, vario integrator tc, wind tc, average wind tc
 6. GNSS configuration: uint32_t GNSS type, 3 * float32_t (m): base-lenght, down and right parameters
 7. External magnetic sensor calibration parameters: 16 * float32_t (=sensor transfer matrix)

Type 255 is not used (= erased FLASH cell).

Additional data types can be added in the future if necessary.
