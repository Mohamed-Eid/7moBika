import time
import wmi
import playsound


w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
sensors = w.Sensor()


def playSound():
    playsound.playsound('7mo.mp3', True)


def main():
    while True:
        for sensor in sensors:
            if sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
                print("GPU: {}".format(sensor.Value))
                if sensor.Value > 64:
                    playSound()
                    return
        time.sleep(1)


main()
