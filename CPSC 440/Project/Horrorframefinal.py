import time
from tkinter import RIGHT
import RPi.GPIO as GPIO
import keyboard
import subprocess as sp
import os
import random as rand
import threading
import pygame as pg
import sys


def main():
    video = [
        "omxplayer",
        "filename",
        "-o",
        "both",
        "--win",
        "0 0 1920 1080",
        "--aspect-mode",
        "fill",
        "--no-osd",
        "--orientation",
        "180",
        "--vol",
        "-600",
    ]

    GPIO.setmode(GPIO.BCM)

    pirpin = 4

    GPIO.setup(4, GPIO.IN)

    print("Motion sensor alarm (CTRL-C to exit!")

    time.sleep(0.2)

    print("Ready!!!")
    x = 0
    rand_list = [1, 2, 3, 4, 5]
    showImage()
    while x == 0:
        print(exit_command)
        if exit_command == 1:
            print("In the city of California!")
            break
        i = GPIO.input(pirpin)
        if i == 0:
            # print("No intruders", i)
            time.sleep(0.1)
        elif i == 1:
            # print("Intruder detected", i)
            value = rand.choice(rand_list)

            if value == 1:
                # scarefile =  os.path.join(main_dir, "1")
                scareFile = "/home/pi/Horror_Frame_Project/1V.mp4"
                video[1] = scareFile
                print(video[1])
                thevideo = sp.Popen(video)
                while thevideo.poll() is None:
                    time.sleep(0.1)

            elif value == 2:
                # scarefile =  os.path.join(main_dir, "2")

                scareFile = "/home/pi/Horror_Frame_Project/2V.mp4"
                video[1] = scareFile
                print(video[1])
                thevideo = sp.Popen(video)
                while thevideo.poll() is None:
                    time.sleep(0.1)

            elif value == 3:
                # scarefile =  os.path.join(main_dir, "1")
                scareFile = "/home/pi/Horror_Frame_Project/3V.mp4"
                video[1] = scareFile
                print(video[1])
                thevideo = sp.Popen(video)
                while thevideo.poll() is None:
                    time.sleep(0.1)

            elif value == 4:
                # scarefile =  os.path.join(main_dir, "1")
                scareFile = "/home/pi/Horror_Frame_Project/4V.mp4"
                video[1] = scareFile
                print(video[1])
                thevideo = sp.Popen(video)
                while thevideo.poll() is None:
                    time.sleep(0.1)

            elif value == 5:
                # scarefile =  os.path.join(main_dir, "1")
                scareFile = "/home/pi/Horror_Frame_Project/5V.mp4"
                video[1] = scareFile
                print(video[1])
                thevideo = sp.Popen(video)

                while thevideo.poll() is None:
                    time.sleep(0.1)
            i = 0


def showImage():
    # filename = "image.png"
    # with Image.open(filename) as image:
    # width, height = image.size
    os.system(
        "sudo fbi -T 1 -d /dev/fb0 -noverbose -once /home/pi/Horror_Frame_Project/image.png"
    )


if __name__ == "__main__":
    global exit_command
    exit_command = 0
    t1 = threading.Thread(target=main, args=())
    t1.start()
    while True:
        print("hi")
        if keyboard.read_key() == "a":
            print("Hello World!")
            exit_command = 1
            t1.join()
            os.system("sudo killall -9 fbi")

            sys.exit()
            break

