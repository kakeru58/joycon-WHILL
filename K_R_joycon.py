import time
import os
import sys
import whillpy
import whill_data
import pyjoycon
from pyjoycon import device
from pyjoycon import JoyCon, get_L_id, get_R_id
import pygame
# ---- #
# init #
# ---- #
# WHILL
whill = whillpy.connect(port='/dev/tty.usbserial-FT1WH33Q')
# JoyCon


class MyJoyCon(
    pyjoycon.GyroTrackingJoyCon,
    pyjoycon.ButtonEventJoyCon,
):
    pass


t = 100

flag = 0
ids = get_R_id()
joycon = MyJoyCon(*ids)

while True:
    input = joycon.get_status()
    x, y = 0, 0
    if flag == 0:
        if input["accel"]["x"] >= 2000:  # back
            x = -1
        elif input["accel"]["x"] <= -1100:  # front
            x = 1
        if input["accel"]["y"] >= 2000:  # right
            y = -1
        elif input["accel"]["y"] <= -2000:  # left
            y = 1
        pygame.time.wait(int(1000 / 60))
        for event_type, status in joycon.events():
            if event_type == "b" and status == 1:
                flag = 1
            elif event_type == "x" and status == 1:
                if t < 100:
                    t = t + 5
            elif event_type == "y" and status == 1:
                if t > 5:
                    t = t - 5
    elif flag == 1:
        if input["analog-sticks"]["right"]["vertical"] <= 1500:  # back
            x = -1
        elif input["analog-sticks"]["right"]["vertical"] >= 2000:  # front
            x = 1
        if input["analog-sticks"]["right"]["horizontal"] >= 2900:  # right
            y = 1
        elif input["analog-sticks"]["right"]["horizontal"] <= 1200:  # left
            y = -1
        pygame.time.wait(int(1000 / 60))
        for event_type, status in joycon.events():
            if event_type == "b" and status == 1:
                flag = 0
            elif event_type == "x" and status == 1:
                if t < 100:
                    t = t + 5
            elif event_type == "y" and status == 1:
                if t > 0:
                    t = t - 5

    whill.move(straight=int(x * t), turn=int(y * t))
    time.sleep(0.01)
