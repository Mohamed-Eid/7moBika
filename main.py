import time
import wmi
import playsound
import PySimpleGUI as sg
import threading
import pythoncom
from win10toast import ToastNotifier


def A7naHntero():
    toast = ToastNotifier()
    toast.show_toast(
        "حمو بيكا",
        "إحنا هنيطيرو ولا إيه ؟؟",
        duration=20,
        icon_path="A7naHntero.ico",
        threaded=True,
    )
    playsound.playsound('7mo.mp3', True)


def updateTemp(window, threshold=64):
    print('threshold : '+str(threshold))
    pythoncom.CoInitialize()
    while True:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        sensors = w.Sensor()
        for sensor in sensors:
            if sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
                print("GPU: {}".format(sensor.Value))
                window.write_event_value('UpdateTemp', sensor.Value)
                if sensor.Value > int(threshold):
                    A7naHntero()
                    return
        time.sleep(1)


def gui():

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        #
        [sg.Text('GPU TEMP : ' + str(0), key='temp')],
        [sg.Text('Your GPU temp threshold'),
         sg.InputText(64, key='threshold')],
        [sg.Button('Start'), sg.Button('Stop')]
    ]

    # Create the Window
    window = sg.Window('Window Title', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Stop':  # if user closes window or clicks cancel
            break
        elif event == 'Start':
            threading.Thread(target=updateTemp, args=(
                window, values['threshold']), daemon=True).start()
        elif event == 'UpdateTemp':
            print('Got a message back from the thread: ', values[event])
            window['temp'].update('GPU TEMP : ' + str(values[event]))
    window.close()


if __name__ == '__main__':
    gui()
    print('Exiting Program')
