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


            if self.stop is True:
                try:
                    self.file.close()
                except Exception as e:
                    print(e)
                return

    def stop(self):
        self.stop = True


interface = CanGet('COM20')
interface.start()
drawInterval = 0.2


def animate(i):
    global x
    global min_temperature
    global max_temperature
    global min_humidity
    global max_humidity
    global min_pressure
    global max_pressure

    if interface.temperature < min_temperature:
        min_temperature = interface.temperature

    if interface.temperature > max_temperature:
        max_temperature = interface.temperature

    if interface.humidity < min_humidity:
        min_humidity = interface.humidity

    if interface.humidity > max_humidity:
        max_humidity = interface.humidity

    if interface.pressure < min_pressure:
        min_pressure = interface.pressure

    if interface.pressure > max_pressure:
        max_pressure = interface.pressure

    x += drawInterval
    data_temperature.append((x, interface.temperature))
    data_humidity.append((x, interface.humidity))
    data_pressure.append((x, interface.pressure))
    ax.relim()
    ax.autoscale_view()
    line.set_data(*zip(*data_temperature))
    line1.set_data(*zip(*data_humidity))
    line2.set_data(*zip(*data_pressure))

    ax.set_xlim(x-100, x)
    ax.set_ylim(min([min_temperature, min_humidity]) - 5,max([max_temperature, max_humidity]) + 5)

    axis.set_ylim(min_pressure - 100, max_pressure + 100)


fig, ax = plt.subplots()
min_temperature = interface.temperature
max_temperature = interface.temperature
min_humidity = interface.humidity
max_humidity = interface.humidity
min_pressure = interface.pressure
max_pressure = interface.pressure
x = 0

data_temperature = deque([(x, interface.temperature)], maxlen=500)
data_humidity = deque([(x, interface.humidity)], maxlen=500)
data_pressure = deque([(x, interface.pressure)], maxlen=500)

ax.set_ylim(-20, 100)
line, = plt.plot(*zip(*data_temperature), c='red')
line.set_label('Temperature')
line1, = plt.plot(*zip(*data_humidity), c='blue')
line1.set_label('rel Humidity')
ax.legend(loc='upper left')
ax.set_xlabel('[s]')

axis = ax.twinx()
axis.set_ylim(95000, 110000)
line2, = plt.plot(*zip(*data_pressure), c='black')
line2.set_label('abs Pressure')
axis.legend(loc='upper right')

ani = animation.FuncAnimation(fig, animate, interval=(drawInterval*1000))
plt.show()

interface.stop()