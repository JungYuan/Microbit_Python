import microbit as mBit
from random import randint

def point_control(x, y, step_x, step_y):
    mBit.display.set_pixel(x, y, 0)
    x += step_x
    y += step_y
    cyc = 0
    if cyc == 1:
        nl = 4
        pl = 0
    else:
        nl = 0
        pl = 4
    if x < 0 :
        x = nl
    elif x > 4:
        x = pl
    if y < 0 :
        y = nl
    elif y > 4:
        y = pl
    mBit.display.set_pixel(x, y, 9)
    return x,y

def new_point(x, y):
    rept = 1
    while rept == 1:
        nx = randint(0, 4)
        ny = randint(0, 4)
        if (nx == x) and (ny == y):
            rept = 1
        else:
            rept = 0
    mBit.display.set_pixel(nx, ny, 5)
    return nx, ny

acc_x = 0
acc_y = 0
def gesture_control():
    global x, y, acc_x, acc_y
    react_point = 200
    acc_x += int(mBit.accelerometer.get_x()/200)
    acc_y += int(mBit.accelerometer.get_y()/200)
    if acc_x > react_point:
        acc_x = 0
        x, y = point_control(x, y, 1, 0)
    elif acc_x < (-1*react_point):
        acc_x = 0
        x, y = point_control(x, y, -1, 0)
    if acc_y > react_point:
        acc_y = 0
        x, y = point_control(x, y, 0, 1)
    elif acc_y < (-1*react_point):
        acc_y = 0
        x, y = point_control(x, y, 0, -1)




score = 0
while (1 == 1):
    x = 2
    y = 4
    cx = 0
    cy = 0
    game_start = 0
    mBit.display.scroll(str(score), wait=False, loop=True)
    #while not(mBit.button_a.is_pressed() and mBit.button_b.is_pressed()) :
    while not(mBit.accelerometer.was_gesture("shake")):
        pass
    mBit.button_a.get_presses()
    mBit.button_b.get_presses()
    mBit.display.scroll("Start")
    game_start = 1
    point_control(x, y, cx, cy)
    score = 0
    correct = True
    t0 = mBit.running_time()
    while (game_start == 1):
        if correct:
            correct = False
            ax, ay = new_point(x, y)
        '''  control method by buttons
        if mBit.button_a.get_presses() > 0:
            x,y = point_control(x, y, 1, 0)
        if mBit.button_b.get_presses() > 0:
            x,y = point_control(x, y, 0, 1)
        '''
        #''' control by accelerometer
        gesture_control()
        #'''
        if mBit.running_time()-t0 > 30000:
            game_start = 0
        if (x == ax) and (y == ay):
            score += 1
            correct = True
            mBit.display.show(mBit.Image.HEART)
            mBit.sleep(100)
            mBit.display.clear()
            point_control(x, y, 0, 0)

