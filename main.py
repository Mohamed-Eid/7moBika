import time
import wmi
import playsound


w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
sensors = w.Sensor()
gpu_temp = 0


def playSound():
    playsound.playsound('7mo.mp3', True)


def main():
    while True:
        for sensor in sensors:
            if sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
                gpu_temp = sensor.Value
                print("GPU: {}".format(gpu_temp))
                playSound()
                return
        time.sleep(1)


main()
