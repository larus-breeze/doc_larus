from can.interfaces.seeedstudio.seeedstudio import SeeedBus
import threading
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from datetime import datetime



class CanGet(threading.Thread):
    temperature = 0.0
    humidity = 0.0
    pressure = 0.0
    voltage = 0.0

    tas = 0.0
    ias = 0.0
    static_pressure = 0.0
    air_density = 0.0

    vario = 0.0
    vario_integrator = 0.0

    wind_direction = 0.0
    wind_speed = 0.0
    wind_direction_average = 0.0
    wind_speed_average = 0.0

    euler_r = 0.0
    euler_n = 0.0
    euler_y = 0.0

    slip_angle = 0.0
    yaw_rate = 0.0
    nick_angle = 0.0

    stop = False
    file = None

    def __init__(self, channel):
        super(CanGet, self).__init__()
        self.bus = SeeedBus(bustype='seeedstudio', channel=channel, bitrate=1000000)
        filename = datetime.utcnow().strftime("%Y%m%d%H%M%S") + '_data.csv'
        self.file = open(filename, 'w')
        self.file.writelines(["Time,Temperature,Humidity,Pressure\n"]) # Write header

    def run(self):
        while True:
            rxMessage = self.bus.recv()
            if rxMessage is not None:
                if rxMessage.arbitration_id == 0x214:
                    self.temperature = (int.from_bytes(rxMessage.data, 'little', signed="True")) / 1000.0

                if rxMessage.arbitration_id == 0x215:
                    self.humidity = (int.from_bytes(rxMessage.data, 'little', signed="False")) / 1000.0

                if rxMessage.arbitration_id == 0x216:
                    self.pressure = (int.from_bytes(rxMessage.data, 'little', signed="False")) / 1000.0

                if rxMessage.arbitration_id == 0x216:
                    line = '{},{},{},{}\n'.format(datetime.utcnow().strftime("%Y%m%d%H%M%S%f"), self.temperature, self.humidity, self.pressure)
                    print(line, end="")
                    self.file.writelines([line])
                    self.file.flush()

                if rxMessage.arbitration_id == 0x101:  # Euler Angles
                    self.euler_r = (int.from_bytes(rxMessage.data[0:2], 'little', signed="True")) / 1000.0 * 180 / 3.1415
                    self.euler_n = (int.from_bytes(rxMessage.data[2:4], 'little', signed="True")) / 1000.0 * 180 / 3.1415
                    self.euler_y = (int.from_bytes(rxMessage.data[4:6], 'little', signed="True")) / 1000.0 * 180 / 3.1415

                if rxMessage.arbitration_id == 0x102:  # Airspeed
                    self.tas = (int.from_bytes(rxMessage.data[0:1], 'little', signed="False"))
                    self.ias = (int.from_bytes(rxMessage.data[2:3], 'little', signed="False"))

                if rxMessage.arbitration_id == 0x103:  # Vario  delivered in mm/s
                    self.vario = (int.from_bytes(rxMessage.data[0:1], 'little', signed="False")) / 1000.0
                    self.vario_integrator = (int.from_bytes(rxMessage.data[2:3], 'little', signed="False")) / 1000.0

                if rxMessage.arbitration_id == 0x108:  # Wind delivered in Speed in km/h,   Direction 1/1000 rad
                    self.wind_direction = (int.from_bytes(rxMessage.data[0:1], 'little', signed="True")) / 1000.0
                    self.wind_speed = (int.from_bytes(rxMessage.data[2:3], 'little', signed="True"))
                    self.wind_direction_average = (int.from_bytes(rxMessage.data[4:5], 'little', signed="True")) / 1000.0
                    self.wind_speed_average = (int.from_bytes(rxMessage.data[6:7], 'little', signed="True"))

                if rxMessage.arbitration_id == 0x109:  # Atmosphere
                    self.static_pressure = (int.from_bytes(rxMessage.data[0:3], 'little', signed="False"))
                    self.air_density = (int.from_bytes(rxMessage.data[4:7], 'little', signed="False"))

                if rxMessage.arbitration_id == 0x10C:  # c_CAN_Id_TurnCoord
                    self.slip_angle = (int.from_bytes(rxMessage.data[0:1], 'little', signed="True")) / 1000.0 * 180 / 3.1415
                    self.yaw_rate = (int.from_bytes(rxMessage.data[2:3], 'little', signed="True")) / 1000.0 * 180 / 3.1415
                    self.nick_angle = (int.from_bytes(rxMessage.data[4:5], 'little', signed="True")) / 1000.0 * 180 / 3.1415

                    #print("Slip angle, Yaw rate, nick angle: ", self.slip_angle, self.yaw_rate, self.nick_angle)

                if rxMessage.arbitration_id == 0x112:  # c_CID_KSB_Vdd; // 0x112
                    self.voltage = (int.from_bytes(rxMessage.data[0:1], 'little', signed="False"))/10.0

                print("Voltage: ", self.voltage,
                      "Euler r n y: ", self.euler_r, self.euler_n, self.euler_y,
                      " Pressure: ", self.static_pressure,
                      " TAS: ", self.tas,
                      " Vario: ", self.vario,
                      " Vario_Integrated: ", self.vario_integrator,
                      " Wind_Direction: ", self.wind_direction,
                      " Wind_Speed: ", self.wind_speed,
                      " Wind_Direction_Average: ", self.wind_direction_average,
                      " Wind_Speed_Average: ", self.wind_speed_average,
                      " Slip Angle: ", self.slip_angle,
                      " Yaw Rate: ", self.yaw_rate,
                      " Nick Angle: ", self.nick_angle
                      )

                #print("Euler r n y: ", self.euler_r, self.euler_n, self.euler_y)

            if self.stop is True:
                try:
                    self.file.close()
                except Exception as e:
                    print(e)
                return

    def stop(self):
        self.stop = True


interface = CanGet('/dev/ttyUSB0')
interface.start()



