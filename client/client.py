
import requests
import keyboard

url = 'http://10.0.0.6:5000/motor_control'

keys = ['Right', 'Up', 'Down', 'Left', 'Ctrl+c']

def main():
    keystrokes = []
    while True:
        for key in keys:
            if keyboard.is_pressed(key):
                keystrokes.append(key)
        
        if len(keystrokes) > 0:
            print(keystrokes)
            try:
                requests.post(url, data={'data': keystrokes})
            except:
                print("Error: could not send data to robot.")
            keystrokes = []

if __name__ == "__main__":
    main()
