# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music

my_select = 0
while True:
    if my_select == 1:
        music.play(music.ODE)
    if my_select == 2:
        music.play(music.RINGTONE)
    if my_select == 3:
        music.play(music.BIRTHDAY)
    my_select = 0
    if button_a.was_pressed():
        my_select = 1
        sleep(200)
    if button_b.was_pressed():
        my_select = 2
        sleep(200)
    if button_a.is_pressed() and button_b.is_pressed():
        my_select = 3
        