import time
import os
import sys
import whillpy
import whill_data
import pyjoycon
from pyjoycon import device
from pyjoycon import JoyCon, get_L_id
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
ids = get_L_id()
joycon = MyJoyCon(*ids)

while True:
    input = joycon.get_status()
    x, y = 0, 0
    if input["analog-sticks"]["left"]["vertical"] <= 1800:  # back
        x = -1
    elif input["analog-sticks"]["left"]["vertical"] >= 2100:  # front
        x = 1
    if input["analog-sticks"]["left"]["horizontal"] >= 2900:  # right
        y = 1
    elif input["analog-sticks"]["left"]["horizontal"] <= 1000:  # left
        y = -1
    pygame.time.wait(int(1000 / 60))
    for event_type, status in joycon.events():
        if event_type == "right" and status == 1:
            exit()
        elif event_type == "up" and status == 1:
            if t < 100:
                t = t + 5
        elif event_type == "down" and status == 1:
            if t > 0:
                t = t - 5

    whill.move(straight=int(x * t), turn=int(y * t))
    time.sleep(0.001)
