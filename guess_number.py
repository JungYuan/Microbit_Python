# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import random as rd

def button_input(x, y):
    aa = int((x+y)/2)
    while not (button_a.is_pressed() and button_b.is_pressed()):
        if button_a.is_pressed() :
            aa +=1
        if button_b.is_pressed():
            aa -=1
        display.scroll(str(aa))
        
    return aa

def guess_number():
    correct_answer = rd.randint(1,100)
    correct = 0
    max_v = 100
    min_v = 0
    gus_times = 0
    while correct == 0 :
        gus_times += 1
        display.show(str(gus_times))
        sleep(1000)
        #ss = "please input"+str(min_v)+"~"+str(max_v)+"("+str(gus_times)+"): "
        #print(ss) 
        # u_ans = int(input())
        u_ans = button_input(min_v, max_v)
        if (u_ans > min_v) and (u_ans < max_v):
            if (u_ans == correct_answer):
                print("Congraduration ! You are right !")
                while not (button_a.is_pressed() and button_b.is_pressed()):
                    display.show(Image.HAPPY)
                    sleep(1000)
                    display.show(str(gus_times))
                    sleep(1000)
                correct = 1
            elif (u_ans < correct_answer):
        
                min_v = u_ans
                display.show(Image.ARROW_N)
            else:
                max_v = u_ans
                display.show(Image.ARROW_S)
        else:
            print("input number is not in range !")
            display.show(Image.SAD)
        sleep(1000)
        
while True:
    guess_number()