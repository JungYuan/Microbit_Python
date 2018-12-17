# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
from random import randint
import music

def my_firework(x, y):
    for ii in range(1, 5):
        display.clear()
        if (x+ii) in range(5):
            display.set_pixel(x+ii, y, 9)
            for jj in range(1, ii+1):
                if (y+jj) in range(5):
                    display.set_pixel(x+ii, y+jj, 9)
                if (y-jj) in range(5):
                    display.set_pixel(x+ii, y-jj, 9)
        if (x-ii) in range(5):
            display.set_pixel(x-ii, y, 9)
            for jj in range(1, ii+1):
                if (y+jj) in range(5):
                    display.set_pixel(x-ii, y+jj, 9)
                if (y-jj) in range(5):
                    display.set_pixel(x-ii, y-jj, 9)
        if (y+ii) in range(5):
            display.set_pixel(x, y+ii, 9)
            for jj in range(1, ii+1):
                if (x+jj) in range(5):
                    display.set_pixel(x+jj, y+ii, 9)
                if (x-jj) in range(5):
                    display.set_pixel(x-jj, y+ii, 9)
        if (y-ii) in range(5):
            display.set_pixel(x, y-ii, 9)
            for jj in range(1, ii+1):
                if (x+jj) in range(5):
                    display.set_pixel(x+jj, y-ii, 9)
                if (x-jj) in range(5):
                    display.set_pixel(x-jj, y-ii, 9)
        sleep(120)
    display.clear()
    return
    
def rand_firwork():
    x = randint(0, 4)
    y = randint(0, 4)
    display.set_pixel(x, y, 9)
    sleep(300)
    my_firework(x, y)
    return
    
    


def play_mygame():
    mx = 2
    my = 2
    hit_count = 0
    music.play(music.POWER_UP)
    zero_t = running_time()
    while (running_time() - zero_t) <= 60000:
        display.set_pixel(mx, my, 5)
        ans_correct = 0
        while ans_correct == 0:
            ans_x = randint(0, 4)
            ans_y = randint(0, 4)
            if not (ans_x == mx and ans_y == my):
                ans_correct = 1
        display.set_pixel(ans_x, ans_y, 9)
        ans_correct = 0
        while ans_correct == 0:
            aa = button_a.get_presses()
            if aa > 0:
                display.set_pixel(mx, my, 0)
                my += aa
                if (my > 4):
                    my %= 5
                display.set_pixel(mx, my, 5)
            aa = button_b.get_presses()
            if aa > 0:
                display.set_pixel(mx, my, 0)
                mx += aa
                if (mx > 4):
                    mx %= 5
                display.set_pixel(mx, my, 5)
            if (mx == ans_x) and (my == ans_y):
                my_firework(mx, my)
                ans_correct = 1
                hit_count += 1
                music.play(music.BA_DING)
            if (running_time() - zero_t) >= 60000:
                ans_correct = 1
    music.play(music.POWER_DOWN)
    return hit_count

fun_mode = 0 
respon_n = 0
while True:
    a_press = button_a.was_pressed()
    b_press = button_b.was_pressed()
    if a_press:
        if b_press:
            fun_mode = 2
            music.play(music.BA_DING)
        else:
            fun_mode = 0
            music.play(music.BA_DING)
    else:
        if b_press:
            fun_mode = 1
            music.play(music.BA_DING)
    
    if fun_mode == 0:
        rand_firwork()
    elif fun_mode == 1:
        display.scroll(str(respon_n))
        fun_mode = 0
    else:
        display.show("S")
        sleep(500)
        display.clear()
        respon_n = play_mygame()
        display.clear()
        display.scroll(str(respon_n))
        fun_mode = 1
        button_a.was_pressed()
        button_b.was_pressed()
    
        
    

    