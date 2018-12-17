# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music

import neopixel
my_variable = 0
LED_Length = 60
np = neopixel.NeoPixel(pin2, LED_Length)

def FlashR2L(Nled, r, g, b):
    for i in range(Nled):
        np[i] = (r, g, b)
        np.show()
        sleep(25)
    sleep(500)
    for i in range(Nled):
        np[i] = (0, 0, 0)
    np.show()
    sleep(100)
    
def FlashL2R(Nled, r, g, b):
    for i in range(Nled):
        np[Nled-i-1] = (r, g, b)
        np.show()
        sleep(25)
    sleep(500)
    for i in range(Nled):
        np[i] = (0, 0, 0)
    np.show()
    sleep(100)
    
def FlashStop(Nled, r, g, b):
    for ii in range(2):
        for i in range(Nled):
            np[i] = (r, g, b)
        np.show()
        sleep(300)
        for i in range(Nled):
            np[i] = (0, 0, 0)
        np.show()
        sleep(200)
    
while True:
    til_x = accelerometer.get_x()
    if button_a.was_pressed() or til_x < -500:
        music.play(music.BA_DING)
        for ii in range(20):
            FlashL2R(LED_Length, 60, 35, 0)
    elif button_b.was_pressed() or til_x > 500:
        music.play(music.BA_DING)
        for ii in range(20):
            FlashR2L(LED_Length, 60, 35, 0)
    else:
        FlashStop(LED_Length, 50, 0, 0)
        sleep(150)
        