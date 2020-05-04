import time
import sys
from time import sleep
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os


Intro = ("Welcome back <3 \n")

for char in Intro:
    sleep(0.04)
    sys.stdout.write(char)
    sys.stdout.flush()

Enter_Key = input("Enter ON/OFF Key: ")

for char in Enter_Key:
    sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()


Kill_Key = input("\nEnter Kill Switch Key: ")

for char in Kill_Key:
    sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()


Button_Selection = input("Mouse button, Left(1) or Right(2) Click? \n")
Button_Selection = int(Button_Selection)
if Button_Selection == 1:
    print("Left Gotcha")
    button = Button.left
else:
    Button_Selection == 2
    print("Right Gotcha")
    button = Button.right

# Main Code

delay = ("\nNow how fast do you want the click speed: ")

for char in delay:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

delay = float(input())


Reminder = (("\nRemember \"") + str(Enter_Key) + ("\" Is the ON/OFF Macro Key, and \"") + str(Kill_Key) + ("\" is the Kill Key.\n"))

for char in Reminder:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

Done = ("\nYou're all good to go\n\n")

for char in Done:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

start_stop_key = KeyCode(char=Enter_Key)
exit_key = KeyCode(char=Kill_Key)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("AutoClick Activated")
        os.system("aplay On.wav&")
        self.running = True

    def stop_clicking(self):
        print("AutoClick Disabled")
        os.system("aplay Off.wav&")
        self.running = False

    def exit(self):
        self.stop_clicking()
        print("Autoclicker Shutting Down")
        os.system("aplay Kill.wav&")
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
